#
#  File Name: MergeClient.py
#
#  Runs on the 2nd Pi
#
#  Notes: Before running, DO THE FOLLOWING! -  
#  
#  Distribute the task to 2 Raspberry Pis.  To do so we first have to set 
#   the IP addresses of each Raspberry Pi.
#
#  For the first Pi, type this in the command line, configuring its IP address 
#    to 192.168.1.1, and this Pi will act as the Server in the network.
#   sudo ifconfig eth0 192.168.1.1 broadcast 192.168.1.255 netmask 255.255.255.0
#
#  For the second Pi, type this in the command line, configuring its IP address 
#   to 192.168.1.2, and this Pi will act as the Client.
#  sudo ifconfig eth0 192.168.1.2 broadcast 192.168.1.255 netmask 255.255.255.0
#
#  Start the 1st Pi (MergeServer.py)
#   When the line "Waiting for client..." is printed on the 1st Pi's command 
#   line, run the following code on the second Pi.
#

import socket
import MergeSort

HOST = '192.168.1.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


#Receives arraystring in chunks
arraystring = ''
print 'Receiving data...'

while 1:
   data = s.recv(4096) #Receives data in chunks
   #print data
   arraystring += data #Adds data to array string
   if ']' in data: #When end of data is received
      break

array = eval(arraystring)
print 'Data received, sorting array... '


#Sorts the array which it is allocated
array = MergeSort.mergesort(array)
print 'Array sorted, sending data...'


#Converts array into string to be sent back to server
arraystring = repr(array)
s.sendall(arraystring) #Sends array string
print 'Data sent.'

s.close() 

