# -*- coding: utf-8 -*-
"""
@author: derobest

brief : used to compare concurrent and non concurrent modes

args : 

Return :
    
Raises : 
    
"""

import subprocess
import threading
import os
    
def publishing():
    iterations=500#00

    #concurrent mode
    subprocess.call( ['python','queue_publish_read.py','-s {}'.format(iterations),'-c'])# Subprocess pour éviter d'ouvrir des console à chaque envoi
    #non concurrent mode
#    subprocess.call( ['python','queue_publish_read.py','-s {}'.format(iterations)])# Subprocess pour éviter d'ouvrir des console à chaque envoi
        

def runReader(readerId, sleep):
    print ("Run reader#{}".format(readerId))
    #concurrent mode
    os.system("python queue_publish_read.py -r -c -d {}".format(sleep))
    #non concurrent mode
#   os.system("python queue_publish_read.py -r -d {}".format(sleep))
           
               
#main        
#mq_publish_thread = threading.Thread(target=publishing)
mq_receive_thread1 = threading.Thread(target=runReader,args=[1,0.1])
mq_receive_thread2 = threading.Thread(target=runReader,args=[2,0.1])

#mq_publish_thread.start()    
mq_receive_thread2.start()
mq_receive_thread1.start()
publishing()
print ("Main done")
