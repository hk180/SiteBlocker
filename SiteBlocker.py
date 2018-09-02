import platform
import datetime

default = open(r"defaulthostfile.txt","r")
defaultcontent = default.read()
hostfile = open(r"hosts.txt","w+")
hostfile.write(defaultcontent)
hostfile.close()

platform1 = platform.system()   #to get windows/linunx

#reading list of website to block from input file
file1 = open(r"websitelist.txt","r")
inputlist = file1.readlines()
#print(sitelist)
inputs = []
sitelist = []
starttime = []
endtime = []
count = 0
for items in inputlist:
    count += 1
    inputs.append(items.split(" "))
    sitelist.append(inputs[count-1][0])
    starttime.append(inputs[count-1][1])
    endtime.append(inputs[count-1][2])
#print(inputs)
#print(sitelist)
#print(hours)
#print(minutes)
#to get system time
now = datetime.datetime.now()


change = 0
flag = 0
try:
    if platform1 == 'Windows':
        #hostfile = open(r"C:\Windows\System32\drivers\etc\hosts.txt","a")
        hostfile = open(r"hosts.txt","a")
    else:
        hostfile = open(r"/etc/hosts","a")
    for items in sitelist:

        if int(starttime[flag]) < now.hour and int(endtime[flag]) > now.hour:
            hostfile.write("\n127.0.0.1  " + items)
            change += 1
        else:
            pass
        flag += 1

except:
    print("unable to open host file")

hostfile.close()

if change == 0:
    hostfile = open(r"hosts.txt","w+")
    hostfile.write(defaultcontent)
    hostfile.close()

