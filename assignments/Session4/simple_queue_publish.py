# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest
"""

"""
brief :  publish message on RabbitMQ (amqp cloud)
queue is durable

args : to be used with command line
By default, non concurrency mode.
    -c : to activate concurrency mode (persistent messages)
    -m : message sent to the queue
        
Return :
    
Raises : 
"""

import pika
import os
import argparse

parser = argparse.ArgumentParser(description='parse rabbit')
parser.add_argument("-c", "--concurrency", action = 'store_true', help ='set this option to switch to persistent mode' )
parser.add_argument("-m", "--message", type = str )
args = parser.parse_args() 

import amqp
amqp_url = amqp.key
#print(amqp_url);

##PRODUCER simple_queue_publish.py
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15

payload_message="Hello presentation"
if args.message:
    payload_message = args.message
    
connection = pika.BlockingConnection(params) ## ouverture connection

channel= connection.channel()## ouverture canal

channel.queue_declare(queue='presentation',durable=True)##queue non durable On peut créer une durable depuis la console Rabbit
if args.concurrency:
    print("Concurrency is on")
    msg=channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=payload_message,
                          properties=pika.BasicProperties(delivery_mode=2)# persistent message
                          )
else:
    msg=channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=payload_message)
    
print("[x] sent '",payload_message,"'")
connection.close()