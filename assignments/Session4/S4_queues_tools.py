# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest

Brief : Run multithreads programs : 1 publisher, 2 readers
using simple_queue_publish.py and simple_queue_read.py

Args : 
number of "iterations" parameter to be set up
sleep in second for each reader thread (parameter on position two)

Return : 
print logs

    
Raises : 
    
"""

import subprocess
import threading
import os
    
def publishing():
    iterations=10#00

    for i in range(iterations):
        #os.system('start python simple_queue_publish.py -c -m "Hello presentation : message #{}"'.format(i))
        subprocess.call( ['python','simple_queue_publish.py','-c','-m "Hello presentation : message #{}"'.format(i)])# Subprocess pour éviter d'ouvrir des console à chaque envoi
        print ("Publish#{}".format(i))
        

def runReader(readerId, sleep):
    print ("Run reader#{}".format(readerId))
    os.system("python simple_queue_read.py -c -s {}".format(sleep))
           
               
#main        
mq_publish_thread = threading.Thread(target=publishing)
mq_receive_thread1 = threading.Thread(target=runReader,args=[1,10])
mq_receive_thread2 = threading.Thread(target=runReader,args=[2,1])

#mq_publish_thread.start()    
mq_receive_thread2.start()
mq_receive_thread1.start()
publishing()
print ("Main done")

"""
Question 5 Answer is :
Rabbit dispatchs messages evenly between the 2 consumers, even if one of the consumer is slower to process messages

Question 6 Answer is:
If I stop one of the two consumers, the pending messages (even and odd) are processed by the second consumer, still running.
The pending messages hold an "unacked" status, they are processed by the second consumer after a timeout delay.

Question 7 Answer is: 
The messages are loadbalanced. With prefetch count = 1 , rabbit doesn't dispatch a new message to the consumer until it has processed the previous one.
The fastest reader will process more messages than the slower ones. it is more efficient.

Question 9 Answer is:
The performance gap between the two approaches depends on the task duration.
If the duration is low (sleep = 0), non concurrent mode is faster because load balancing (concurrent mode)  is time consuming.
On the other side, the concurrent mode is getting more interesting with sleep delay. The longer the task is, the more advantageous the concurrent mode is.
 Example with 500 messages published    :
 Concurrent mode without sleep : 12,6s
 Concurrent mode with sleep 100ms : 30s
 Non Concurrent mode without sleep : 1s
 Non Concurrent mode with sleep 100ms : 57s 

"""