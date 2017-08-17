**MULTI-THREADED PORT SCANNER**
================================
Majority of communications over the internet happens using TCP. 
Webserver normally resides on TCP port 80, 
Email-server on port 25
FTP server on port 21

Mostly port scanning is brutally slow, so we can therefore use scanning to drastically improve our speed. 
There are thousands of possible ports. If it is taking 5-15 seconds per port to scan, then it cannot scan more than 10 ports in a minutes, so it is therefore not processing intensive. therefore we use MULTI-THREADING to solve this problem,

Threading
=========
Probably one of the largest drawbacks to python programming language is that it is single threaded. This means that python will only run on a single thread naturally as compared to C# and JAVA. It doesnt make use of the processor very well, you might have a large computational task, and you will find out that it is taking a very long time, while the processor might be below 7% or even less.
There are a quite few solutions to this problem, like threading, multiprocessing, and GPU programming. All of these are possible with python,
Threading is making use of idle processes, to give the appearance of parallel programming. 
in threading we need to import

*threading -- this is for threading
*queue -- this is going to help us make the queue
*time -- this is to simulate some idle time with time.sleep() function

Thread Lock definition:
=======================
The Idea of thread-locking is to prevent simultaneous modification of a variable. e.g 10+2+3, without thread lock, it can give you 12 or 13, this is because one process may be adding 10+2 and another one is adding 10+3. A lock will force the variable to wait until the variable is unlocked in order to access or modify it. Another use of lock is to aid in input/output(i/o).

Does Open port means You are Vulnerable
=======================================
No, it is a common misconception, the truth is that all websites have open ports, but each port is expecting a specific socket.
for example a ship that is supposed to be bring 50 crates of coffee, but has instead brought over 50 crates of swordfish, Immmediately Red flags will be thrown.the same is true with port and sockets. The socket/ship can be denied.


SOCKET FUNCTIONS
================
1) syntax for creating a socket
sock = socket.socket(socket_family, socket_type)

2) Socket Family: here Address family version 4 or Ipv4
AF_INET

3) Socket type: TCP connection
SOCK_STREAM

4) sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
To create a stream socket of family Ipv4 and Tcp connection type

5) Socket type UDP connections
SOCK_DGRAM

6) to translate a host to ipv4 address format:
gethostbyname("host")

7) to get the host name of the machine itself:
socket.gethostname()

8) to get the fully qualfied domain name:
socket.getfqdn("8.8.8.8")

























