# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:42:42 2018

@author: derobest
"""

"""
brief : publish or read messages
queue is durable
Number of unacknowledged messages checked, only one message dispatched to a reader at a time.


args : 
By default, non concurrency mode.
-c : to activate concurrency mode (persistent messages and acknowledgment is turned on)
-d : sleep to simulate delays (default = 0)
-r : read mode, infinite loop
-s : send/publish n messages (default 1) 

Return :
Log process duration in ms
Raises : 


"""


import pika
import os
import time
##dans le cas d'un lancement  depuis une ligne de commande : 
## python mycript.py ou python mycript.py --receive python mycript.py sendmany 3
import argparse


##queue_publish_read
parser = argparse.ArgumentParser(description='parse rabbit')
parser.add_argument("-r", "--receive", action = 'store_true', help ='set this option to switch to receive mode' )
parser.add_argument("-s", "--sendmany",type=int,default=1)
parser.add_argument("-c", "--concurrency", action = 'store_true', help ='set this option to switch to persistent mode' )
parser.add_argument("-d", "--sleep", type=float, default=0, help ='set this sleep n seconds after processing a message')

args = parser.parse_args()

###CONNECTION
import amqp
amqp_url = amqp.key
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15

connection = pika.BlockingConnection(params) ## ouverture connection
channel= connection.channel()
channel.queue_declare(queue='presentation',durable=True)##queue non durable On peut créer une durable depuis la console Rabbit


if not args.receive:  # PUBLISH MODE
    for i in range(args.sendmany):
        if args.concurrency:
            print("Concurrency is on")        
            msg=channel.basic_publish(exchange='', 
                                  routing_key='presentation',
                                  body='hello presentation {}'.format(i),
                                  properties=pika.BasicProperties(delivery_mode=2)# persistent message
                                  )
        else:
            print("Concurrency is off")        
            msg=channel.basic_publish(exchange='', 
                                  routing_key='presentation',
                                  body='hello presentation{}'.format(i))

        print("[x] sent 'hello presentation'")
        
    connection.close()
        
else: # READER MODE
    cpteur = 0
    def callback(ch,method,properties,body):
        print("Received");
        global cpteur 
        cpteur = cpteur + 1;
        print(cpteur)
        if args.concurrency:
            print(" [x] Message processed,acknowledgement (to delete message from the queue)")
            ch.basic_ack(delivery_tag = method.delivery_tag)
        if args.sleep and args.sleep>0:
            print("entering sleep for (s):{}".format(args.sleep))
            time.sleep(args.sleep)
        global millis
        millisnew = int(round(time.time() * 1000))
        print("Elpased since start={} ms".format(millisnew - millis))
    
    channel.basic_qos(prefetch_count=1)#load balancing
    channel.basic_consume(callback,queue='presentation',no_ack= not args.concurrency)   
    millis = int(round(time.time() * 1000))
    print("Waiting for message. To exit press CTRL+C")
    channel.start_consuming()
