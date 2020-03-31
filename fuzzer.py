#!/usr/bin/python

import socket

buffer = ['A']
counter = 100
while len(buffer) <= 10:
  buffer.append('A'*counter)
  counter = counter + 100

try:
  for string in buffer:
    print 'Fuzzing App with %s bytes' % len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('127.0.0.1',9999))
    s.recv(1024)
    s.send(string + '\r\n')
    s.close()

except:
  print 'Could not connect to application, you may have crashed it'
  
