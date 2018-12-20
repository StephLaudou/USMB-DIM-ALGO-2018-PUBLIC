# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest
"""

"""
brief : Message broadcasting
Publisher script
Send 10 messages with a fanout mode
Exchange name  = posts

args : 

Return :
    
Raises : 
"""

import pika
import os
import time
import amqp
amqp_url = amqp.key
#print(amqp_url);
  

url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15


connection = pika.BlockingConnection(params) ## ouverture connection

channel= connection.channel()## ouverture canal

channel.exchange_declare(exchange='posts', exchange_type='fanout')# on y declare un echange de type fanout qui s'appelle posts

for i in range(10):
    bodyMessage = "message #{}".format(i)
    channel.basic_publish(exchange='posts', routing_key='', body=bodyMessage)
    print("[x] sent post #", i)
    time.sleep(5) # sleeps for 5 seconds
    
connection.close()


"""
a single publisher sends messages / no subscriber registered
=> the messages are discarded because no consumer is listening

a single publisher sends messages / 2 subscribers registered
=> both subscribers receive all messages

a single publisher sends messages / one subscriber already registered and second one connects
=>  the first subscriber will get every messages while the second one will receive the message sent as of the connection time.


"""