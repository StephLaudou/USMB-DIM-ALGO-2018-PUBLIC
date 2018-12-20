# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest
"""

"""
brief : Message routing
User monitoring
args : 

Return :
    
Raises : 
"""


##"Consumer  simple_queue_read.py
import pika
import os
import amqp
amqp_url = amqp.key

#print(amqp_url);
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15

connection = pika.BlockingConnection(params)
channel= connection.channel()
channel.exchange_declare(exchange='caramail', exchange_type='direct')
channel.queue_declare(queue='presentation', durable=True)
channel.queue_bind(exchange='caramail', queue='presentation', routing_key='presentation')

cpteur = 0
usersList = []

def callback(ch,method,properties,body):
    username = body.decode();
    print("[x] Received %r" % username)
    global usersList    
    if username not in usersList:
        usersList.append(username)
    else:
        print("User already seen : message skipped")
    print("Users List : ", usersList)
        
channel.basic_consume(callback,queue='presentation',no_ack=True)  

print("Waiting for message. To exit press CTRL+C")
channel.start_consuming() ## sorte de boucle infinie

