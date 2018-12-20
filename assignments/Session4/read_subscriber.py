# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest
"""

"""
brief : Message broadcasting
Reader/ subscriber script
Connection to "posts" exchange

args : 

Return :
    
Raises : 
"""


import pika
import os

import amqp
amqp_url = amqp.key

#print(amqp_url);
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15

connection = pika.BlockingConnection(params) # on recupere la connexion au service de queueing

channel = connection.channel() # on prend son channel

channel.exchange_declare(exchange='posts', exchange_type='fanout') # on y declare un echange de type fanout qui s'appelle posts

result = channel.queue_declare(exclusive=True) # on a besoin d'une queue sans nom défini et réservée pour notre reader elle sera supprimée à la déconnexion

queue_name = result.method.queue # on recupere le nom de la queue générée 

channel.queue_bind(exchange='posts', queue=queue_name) # fait le lien avec l'echange posts du publisher et la queue

cpteur = 0

def callback(ch,method,properties,body):
    #print("Received");
    global cpteur 
    cpteur = cpteur +1;
    print(cpteur)  
    print("[x] Received %r" % body)     
    

channel.basic_consume(callback,queue=queue_name,no_ack=True)  # parametrage des modalités de consommation

print("Waiting for message. To exit press CTRL+C")
channel.start_consuming() ## sorte de boucle infinie en attente de messages a consommer

