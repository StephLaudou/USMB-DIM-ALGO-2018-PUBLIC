# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest
"""

"""
brief : Message routing
using direct exchange type and a single exchange named caramail

args : 
-s : send the user name to the monitoring program
no args : post a message
-r : create subscribers

Return :
    
Raises : 
"""

import pika
import os
import argparse

parser = argparse.ArgumentParser(description='parse rabbit')
parser.add_argument("-s", "--signin", type=str )
parser.add_argument("-r", "--reader", action = 'store_true' )

args = parser.parse_args()

import amqp
amqp_url = amqp.key
#print(amqp_url);


url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15


connection = pika.BlockingConnection(params) ## ouverture connection

channel= connection.channel()## ouverture canal

if not args.reader and (not args.signin or args.signin == ""): # mode post    
    channel.exchange_declare(exchange='caramail', exchange_type='direct')
    channel.basic_publish(exchange='caramail', routing_key='posts', body="un message de post")
    print("[x] sent post ")

elif args.reader: # mode reader
    channel.exchange_declare(exchange='caramail', exchange_type='direct') # on y declare un echange de type direct qui s'appelle caramail
    result = channel.queue_declare(exclusive=True) # on a besoin d'une queue réservée pour notre reader
    queue_name = result.method.queue # on recupere le nom de la queue obtenue 
    channel.queue_bind(exchange='caramail', queue=queue_name, routing_key='posts') # fait le lien avec le routage posts de caramail
    
    def callback(ch,method,properties,body):
        print("[x] Received %r" % body)     
    
    channel.basic_consume(callback,queue=queue_name,no_ack=True)  # parametrage des modalités de consommation

    print("Waiting for message. To exit press CTRL+C")
    channel.start_consuming() ## sorte de boucle infinie en attente de messages a consommer

else: # mode presentation / signin
    channel.exchange_declare(exchange='caramail', exchange_type='direct')
    channel.queue_declare(queue='presentation', durable=True)
    channel.basic_publish(exchange='caramail',routing_key='presentation',  body=args.signin)
    print("sent signin to presentation = ", args.signin)

connection.close()