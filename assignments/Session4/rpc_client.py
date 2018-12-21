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
payload_message = 'hello, how fine ?'
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