# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 22:07:26 2018

@author: Stephanie
"""
"""
Brief :  Remote Call Procedure / Client procedure
Send a request to the server on a specific queue (rpc_queue)
Process the server answer 

Args : 
        
Return :
    
Raises : 
Exception raised if the answer doesn't match any existing client correlation_id
        
"""
import pika
import os
import amqp
import uuid
import time
import numpy as np
import msgpack
import msgpack_numpy as m

###establishing connection and declaring the queue to publish request
amqp_url = amqp.key
#print(amqp_url);
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15
connection = pika.BlockingConnection(params)
channel= connection.channel()
channel.queue_declare(queue='rpc_queue')

#Creation de la callback queue anonyme
result = channel.queue_declare(exclusive=True) 
callback_queue = result.method.queue  

#Creation du correlation_id
corr_id = str(uuid.uuid4())

#send request
#payload_message = 'hello, how fine ?'
#payload_message = {'type':0, 'value':'hello, how fine ?' }
payload_message = np.random.random((20,30))
payload_message = msgpack.packb(payload_message, default= m.encode)

channel.basic_publish(exchange='',
                      routing_key='rpc_queue',
                      body=payload_message,
                      properties=pika.BasicProperties(
                            reply_to = callback_queue,
                            correlation_id = corr_id
                              )
                      )
                      
#process response
response=None
def on_response(ch,method,props,body):
    if corr_id == props.correlation_id:
        global response
        response = str(body);
        print('Answer is ',str(response));
    else: 
        raise ValueError('No correlation_id  match');

print('Starting to wait on the response queue')
channel.basic_consume(on_response, 
                      no_ack=True,
                      queue=callback_queue)
while response is None:
    connection.process_data_events()
connection.close()

time.sleep(15) 

"""
Messaging, what kind of message should you manage?

Answers to questions:
1) payload_message = {'type':0, 'value':'hello, how fine ?' }
2) No it crashed with error : TypeError: unhashable type: 'slice'
3) body=str(payload_message) : it works with the dictionary
4) payload_message = np.random.random((20,30)) 
    Thanks to str serialization it also works fine
5) With msgpack comparison of payload size:
    Example:
        Encoded payload size: 4837
        Decoded payload size: 9340
    
    Data is about 40% of original size after encoding. Compression ratio = 1,93
    Note that compression ratio varies depending on the payload_message contents.

    
    
    
"""
