import os
import threading
from queue import Queue
import time
from datetime import datetime
import socket

# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.
clearer = os.system('cls')
print_lock = threading.Lock()

target = 'uilugportal.unilorin.edu.ng' #the target host
ip = socket.gethostbyname(target)

print("-"*80) #to print a long line of dashes 
print("please wait, scanning remote host: ", ip)
print("-"*80)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port {}: OPEN'.format(port))            
                     
        con.close()            
    
    except:
        pass


# The threader thread pulls an worker from the queue and processes it
t1 = time.time()
def threader(): #the Threader processes the worker
    while True:
        # gets a worker from the queue
        
        worker = q.get() #q means Queue instance

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()
    

# Create the queue and threader 
q = Queue()

# how many threads are we going to allow for
for x in range(30):
     t = threading.Thread(target=threader)

     # classifying as a daemon, so they will die when the main dies
     t.daemon = True

     # begins, must come after daemon definition
     t.start()


start = time.time()

# 1000 jobs assigned.
for worker in range(50,100):
    q.put(worker)

# wait until the thread terminates.
q.join()
t2 = time.time()

total = t2-t1
print("Port Successfully scanned in {} ".format(total))
