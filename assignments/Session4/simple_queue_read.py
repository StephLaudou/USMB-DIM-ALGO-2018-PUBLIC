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

import amqp
amqp_url = amqp.key

print(amqp_url);
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15

connection = pika.BlockingConnection(params)

channel= connection.channel()
channel.queue_declare(queue='presentation')

cpteur = 0

def callback(ch,method,properties,body):
    print("Received");
    global cpteur 
    cpteur = cpteur +1;
    print(cpteur)
    #print("[x] Received %r)

channel.basic_consume(callback,queue='presentation',no_ack=True)  ## sorte de boucle infinie

print("Waiting for message. To exit press CTRL+C")
channel.start_consuming()



