# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:39:17 2018

@author: Stephanie
"""

"""
brief :  Remote Call Procedure / Server procedure
Listen to the requests dispatched and send the response back on the specified queue
args : 
        
Return :
    
Raises : 
"""

import pika
import os
import amqp

###establishing connection and declaring the queue
amqp_url = amqp.key
#print(amqp_url);
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15
connection = pika.BlockingConnection(params)
channel= connection.channel()
channel.queue_declare(queue='rpc_queue')

#send the response back
def on_request(ch,method,props,body):
    print('Request is ',str(body));
    response ='Fine and you ?'
    
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     body=str(response),
                     properties=pika.BasicProperties(correlation_id = props.correlation_id)
                     )
    ch.basic_ack(delivery_tag=method.delivery_tag)

#Run
channel.basic_qos(prefetch_count=1)#load balancing if multiple servers
channel.basic_consume(on_request,queue='rpc_queue') #executed when a request is received
print("Waiting for message. To exit press CTRL+C")
channel.start_consuming() ## sorte de boucle infinie