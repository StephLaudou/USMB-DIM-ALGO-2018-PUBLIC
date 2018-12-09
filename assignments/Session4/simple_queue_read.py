# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest
"""

"""
brief : receive messages
infinite loop
args : 

Return :
    
Raises : 
"""


##"Consumer  simple_queue_read.py
import pika
import os
import argparse

parser = argparse.ArgumentParser(description='parse rabbit')
parser.add_argument("-c", "--concurrency", action = 'store_true', help ='set this option to switch to persistent mode' )
args = parser.parse_args()

import amqp
amqp_url = amqp.key

#print(amqp_url);
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15

connection = pika.BlockingConnection(params)

channel= connection.channel()
channel.queue_declare(queue='presentation')

cpteur = 0

def callback(ch,method,properties,body):
    #print("Received");
    global cpteur 
    cpteur = cpteur +1;
    print(cpteur)
    print("[x] Received %r" % body)
    if args.concurrency:
        print(" [x] Message processed,acknoledgement (to delete message from the queue)")
        ch.basic_ack(delivery_tag = method.delivery_tag)
        

channel.basic_consume(callback,queue='presentation',no_ack= not args.concurrency)  

print("Waiting for message. To exit press CTRL+C")
channel.start_consuming() ## sorte de boucle infinie

