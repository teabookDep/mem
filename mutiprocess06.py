#!/usr/bin/python
# encoding=utf-8

# Filename: put_files_hdfs.py
import datetime
import os
import threading

def execCmd(cmd):
    try:
        print("cmd%s start%s" % (cmd,datetime.datetime.now()))
        os.system(cmd)
        print("cmd%s end %s" % (cmd,datetime.datetime.now()))
    except Exception, e:
        print('%s\t fail,because: \r\n%s' % (cmd,e))
 
if __name__ == '__main__':

    # cmd list
    cmds = ['ls /root','pwd',]
    
    #pool
    threads = []
    
    print("exec start %s" % datetime.datetime.now())
 
    for cmd in cmds:
        th = threading.Thread(target=execCmd, args=(cmd,))
        th.start()
        threads.append(th)
         
    # wait for over
    for th in threads:
        th.join()
         
    print("all end: %s" % datetime.datetime.now())
