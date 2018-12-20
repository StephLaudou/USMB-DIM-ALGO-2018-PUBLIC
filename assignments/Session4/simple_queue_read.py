# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest
"""

"""
brief : read messages
queue is durable
Number of unacknowledged messages checked, only one message dispatched to a reader at a time.

args : to be used with command line
By default, non concurrency mode.
    -c : to activate concurrency mode (acknowledgment is turned on)
    -s : sleep to simulate delays (default = 0)

Return : logs
    
Raises : 
"""


##"Consumer  simple_queue_read.py
import pika
import os
import argparse
import time

parser = argparse.ArgumentParser(description='parse rabbit')
parser.add_argument("-c", "--concurrency", action = 'store_true', help ='set this option to switch to persistent mode' )
parser.add_argument("-s", "--sleep", type=int, default=0, help ='set this sleep n seconds after processing a message')
args = parser.parse_args()

import amqp
amqp_url = amqp.key

#print(amqp_url);
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15

connection = pika.BlockingConnection(params)

channel= connection.channel()
channel.queue_declare(queue='presentation',durable=True) #durable=safety parameter in case of Rabbit crash

cpteur = 0

def callback(ch,method,properties,body):
    #print("Received");
    global cpteur 
    cpteur = cpteur +1;
    print(cpteur)  
    print("[x1] Received %r" % body)
    if args.concurrency:
        print(" [x] Message processed,acknowledgement (to delete message from the queue)")
        ch.basic_ack(delivery_tag = method.delivery_tag)
    if args.sleep and args.sleep>0:
            print("entering sleep for (s):{}".format(args.sleep))
            time.sleep(args.sleep)
        
channel.basic_qos(prefetch_count=1)#load balancing
channel.basic_consume(callback,queue='presentation',no_ack= not args.concurrency)   

print("Waiting for message. To exit press CTRL+C")
channel.start_consuming() ## sorte de boucle infinie

