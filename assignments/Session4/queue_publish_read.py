# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:42:42 2018

@author: derobest
"""

"""
brief : send or receive messages

args : 
-r : receive mode, infinite loop
-s n : send n messages (default 1) 

Return :
    
Raises : 


"""


import pika
import os

##dans le cas d'un lancement  depuis une ligne de commande : 
## python mycript.py ou python mycript.py --receive python mycript.py sendmany 3
import argparse


##queue_publish_read
parser = argparse.ArgumentParser(description='parse rabbit')
parser.add_argument("-r", "--receive", action = 'store_true', help ='set this option to switch to receive mode' )
parser.add_argument("-s", "--sendmany",type=int,default=1)
args = parser.parse_args()

###CONNECTION
import amqp
amqp_url = amqp.key
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15

connection = pika.BlockingConnection(params) ## ouverture connection
channel= connection.channel()
channel.queue_declare(queue='presentation')


if not args.receive: 
    for i in range(args.sendmany):
        msg=channel.basic_publish(exchange='', 
                                  routing_key='presentation',
                                  body='hello presentation')
        print("[x] sent 'hello presentation'")
    connection.close()
        
else:
    cpteur = 0
    def callback(ch,method,properties,body):
        print("Received");
        global cpteur 
        cpteur = cpteur + 1;
        print(cpteur)
    #print("[x] Received %r)

    channel.basic_consume(callback,queue='presentation',no_ack=True)  ## sorte de boucle infinie

    print("Waiting for message. To exit press CTRL+C")
    channel.start_consuming()
