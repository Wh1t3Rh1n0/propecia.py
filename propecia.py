#!/usr/bin/env python

import sys
import socket
import threading


usage = """
===========
propecia.py - A multi-threaded class C network scanner.
===========
Created by Michael Allen (http://www.MikeAllen.org)

Based on the original propecia port scanner written by Bind, available here:
    http://packetstormsecurity.com/files/14232/propecia.c.html

Usage: python propecia.py [X.X.X] [Port]

Example: python propecia.py 192.168.0 80 
"""

if len(sys.argv) <= 2:
    print usage
    exit()

ip_prefix = sys.argv[1]
port = int(sys.argv[2])

# Check if a port is open or not.
def test_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((str(ip), int(port)))
        s.close
        print ip
        return True
    except:
        return False


def start_thread(ip, port):
    t = threading.Thread(target=test_port, args=(ip, port))
    t.start()
    
    
for n in range(0,256):
    ip = ip_prefix + "." + str(n)
    start_thread(ip, port)
    
