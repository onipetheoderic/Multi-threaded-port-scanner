from datetime import datetime
import socket
import sys
import threading
import queue as Queue
import os

MAX_THREADS = 70

class Scanner(threading.Thread):
    def __init__(self, inq, outq):
        threading.Thread.__init__(self)
        self.setDaemon(1)
        # queues for (host, port)
        self.inq = inq
        self.outq = outq


    def run(self):
        while 1:
            host, port = self.inq.get()
            sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
            try:
                # connect to the given host:port
                sd.connect((host, port))
            except socket.error:
                # set the CLOSED flag
                self.outq.put((host, port, 'CLOSED'))
            else:
                self.outq.put((host, port, 'OPEN'))
                sd.close()
t1 = datetime.now()
def scan(host, start, stop, nthreads=MAX_THREADS):
    
    clear = os.system('cls')
    ip = socket.gethostbyname(host)

    print("-"*80) #to print a long line of dashes 
    print("please wait, scanning remote host: ", ip)
    print("-"*80)
    toscan = Queue.Queue()
    scanned = Queue.Queue()

    # searchfile = open("tester.txt", "w")
    # poss = open("tester.txt", "r")
    poss = open("pos.txt", "r")
    scanners = [Scanner(toscan, scanned) for i in range(nthreads)]
    for scanner in scanners:
        scanner.start()

    hostports = [(host, port) for port in range(start, stop+1)]
    for hostport in hostports:
        toscan.put(hostport)

    results = {}
    for host, port in hostports:
        while (host, port) not in results:
            nhost, nport, nstatus = scanned.get()
            results[(nhost, nport)] = nstatus
        status = results[(host, port)]
        if status !='CLOSED':
            print('%s:%d %s' %("PORT: ", port, status))
            if port:
                porter = str(port)
                porty = "  " + porter + "  "
                for line in poss:
                    if porty in line:
                        print('\n', line)

            # porter = port
            # searchfile.write(porter)
            
            t2 = datetime.now()
            total = t2 - t1
            print("Port scanning successfull in: ", total)

if __name__ == '__main__':
    host = input("Type in the desired host server: ")
    from_port = int(input("from port: "))
    end_port = int(input("To port: "))
    scan(host, from_port, end_port)


#the if __name__ = '__main__':
#every module in python has a special attribute called __name__.
# here we are creating a new module and executing it as main program so the value of name is set to main
#but if it was imported, let say the module name is my_module, the __name__ would be equal to mymodule and not __main__

#one reason for doing this, is to prevent someone from importing your module and executing the function themselves