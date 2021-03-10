#!/usr/bin/python3
import socket
lastFailed_ipADDR = None
f = open("output1.txt","w")
with open("fileWithIPAddresses","r") as ins:
        for line in ins:
                ipADDR = (line.strip())
                if ipADDR == lastFailed_ipADDR:
                        print (ipADDR+" cached")
                        f.write(ipADDR+"\n")
                        lastFailed_ipADDR = ipADDR
                        continue
                try:
                        ipTuple = socket.gethostbyaddr(ipADDR)
                        print (ipADDR,ipTuple[0])
                        f.write(ipADDR+" "+ipTuple[0]+"\n")
                except:
                        print (ipADDR)
                        f.write(ipADDR+"\n")
                        lastFailed_ipADDR = ipADDR
f.close()
