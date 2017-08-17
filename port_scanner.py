import socket
import os
import sys
from datetime import datetime

#to clear the screen
clearer = os.system('cls')

#Ask for input
remoteServer = input("Enter a remote host to scan: ")
range_start = int(input("From port number: "))
range_end = int(input("To port number: "))
#convert the host-name to its Ip address value
remoteServerIP = socket.gethostbyname(remoteServer)

#to print a nice banner with information on which host we are about to scan

print("-"*60) #to print a loong line of dashes 
print("please wait, scanning remote host", remoteServerIP)
print("-"*60)

#check what time the scan started:
t1 = datetime.now()
# We therefore use the range function to specify ports to scan( e.g between 1 and 2000)

try:
	for port in range(range_start, range_end): # here we are using the range function to specify the the port
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #start an 1pv4 and TCP connection
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print('port {}:  OPEN'.format(port))
		
		sock.close()
except socket.gaierror:
	sys.exit("Hostname could not be resolved. Exiting")

except socket.error:
	print("Couldn't connect to the server")
	sys.exit()

t2 = datetime.now()

# to calculate the difference in the time of execution, to see how long it take to execute the scan
total = t2 - t1
#printing the information to the screen
print("Scanning Completed in: ", total)