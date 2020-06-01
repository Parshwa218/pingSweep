import socket
from datetime import datetime

print("#" *60)

print	("       _                                              ")
print	(" _ __ (_)_ __   __ _   _____      _____  ___ _ __     ")
print   ("| '_ \| | '_ \ / _` | / __\ \ /\ / / _ \/ _ \ '_ \    ")
print	("| |_) | | | | | (_| | \__ \\ V  V /  __/  __/ |_) |   ")                                      
print	("| .__/|_|_| |_|\__, | |___/ \_/\_/ \___|\___| .__/    ")                                                                                                                                                 
print 	("|_|            |___/                        |_|       ")  
print	("							")
print 	("                     Coded By Parshwa Bhavsar         ")


print("#" *60)
                                      

net = input("Enter the IP address: ")
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1
t1 = datetime.now()

def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,135))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
         print (addr , "is live")
         
run1()
t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: " , total)

