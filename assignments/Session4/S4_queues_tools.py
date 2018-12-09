# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:20:33 2018

@author: derobest

brief : 

args : 

Return :
    
Raises : 
    
"""

import subprocess
import sys

DETACHED_PROCESS = 0x00000008

def publishing():
    iterations=1#00

    for i in range(iterations):
        print ("Publish#{}".format(i))
        cmd = [
            sys.executable,
            'python',
            'simple_queue_publish.py',
            '-c'
          ]
        subprocess.Popen(cmd,shell=False,stdin=None,stdout=None,stderr=None,close_fds=True,creationflags=DETACHED_PROCESS)
        

def reading():

    cmd = [
        sys.executable,
        'python',
        'simple_queue_read.py',
        '-c'
      ]
    subprocess.Popen(cmd,shell=False,stdin=None,stdout=None,stderr=None,close_fds=True,creationflags=DETACHED_PROCESS)
    print ("Reader#1 running")
    
    subprocess.Popen(cmd,shell=False,stdin=None,stdout=None,stderr=None,close_fds=True,creationflags=DETACHED_PROCESS)           
    print ("Reader#2 running")
               

publishing()
reading()
print ("Done")