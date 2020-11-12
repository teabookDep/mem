#coding=utf-8

from multiprocessing import Process,Queue,Pool
import multiprocessing
import os, time, random

def initQ(q):
    print("initQ in process",os.getpid())
    with open("numlist.txt", "r") as ins:
        for line in ins:
            q.put(line)        


def read(q):
    print("read in process",os.getpid())
    while True:
        if not q.empty():
            value = q.get(False).strip()
            if value != 'abc' and value != '':
               q.put(value)
            time.sleep(random.random())
        else:
            break

def onetask(q_in,q_out):
    print("q_in size:",q_in.qsize())
    print("onetask in process",os.getpid())
    if not q_in.empty():
        value = q_in.get(False).strip()
        print("onetask:",value)
        #if value != 'abc' and value != '':
        #   q.put(value)
        if value != '' and int(value)%2 != 0:
           q_out.put(value)
        #if int(value)%5 == 0:
        #   time.sleep(600000000)
        time.sleep(random.random())


def Bar(arg):
    print("callback in process",os.getpid())
    print('-->exec done:', arg)

if __name__=='__main__':
    manager = multiprocessing.Manager()
    q1 = manager.Queue()
    q2 = manager.Queue()
    q3 = manager.Queue()
    initQ(q1)
    p = Pool(50)
    while True:
        if not q1.empty():
            pr = p.apply_async(onetask,args=(q1,q2))
        else:
            break
            
    while True:
        if not q2.empty():
            print("q2 size:",q2.qsize())
            pr = p.apply_async(onetask,args=(q2,q3))
        else:
            break
            
    p.close()
    p.join()

    print('所有数据都写入并且读完')