propecia.py
===========

A multi-threaded class C network scanner. Loosely based on propecia.c by Bind.

-----

Created by Michael Allen (http://www.MikeAllen.org)

Based on the original propecia port scanner written by Bind, available here:
    http://packetstormsecurity.com/files/14232/propecia.c.html

Performs a simple TCP port scan on a single port and outputs a list of IP 
addresses with that port open. Simple, effective, and easy to pipe into
other tools of your choosing.

Usage: python propecia.py [X.X.X] [Port]

Example: python propecia.py 192.168.0 80 

-----


