# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest
"""

"""
brief : send one message

args : 

Return :
    
Raises : 
"""

import pika
import os


import amqp
amqp_url = amqp.key
print(amqp_url);

##PRODUCER simple_queue_publish.py
##amqp_url='amqp://wnavpxhz:Ro0VGYzu4vwAaJeHgtILEXCHtFuvpUNQ@flamingo.rmq.cloudamqp.com/wnavpxhz'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15


connection = pika.BlockingConnection(params) ## ouverture connection

channel= connection.channel()## ouverture canal

channel.queue_declare(queue='presentation')##queue non durable On peut créer une durable depuis la console Rabbit
msg=channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body='hello presentation')
print("[x] sent 'hello presentation'")
##print("sent hello presentation")
connection.close()