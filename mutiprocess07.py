#! /usr/bin/env python  

#encoding=utf-8  

import threading
import time
from multiprocessing import Queue
import os
import sys
import subprocess

queue = Queue()

def initQueue():
    global queue
    file_object = open("curllist.txt", "r")
    for line in file_object:
        queue.put(line)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while queue.qsize() > 0:
            cmd = queue.get()
            if cmd.strip() == "testcmd":
                time.sleep(10)
            msg = self.name + '执行了 '+ cmd
            print(msg)
            #os.system(cmd)
            #output = os.popen(cmd)
            #print("output is : ",self.name,output.readlines())
            print("output is : ",subprocess.check_output(cmd))
            time.sleep(0.01)

def main():
    initQueue()
    size = queue.qsize()
    for i in range(size):
        c = Consumer()
        c.start()

if __name__ == '__main__':
    main()
