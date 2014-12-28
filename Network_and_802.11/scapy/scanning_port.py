#!/usr/bin/env python

__author__ = "bt3"

import sys
from scapy.all import *


DEST = '192.168.1.25'

def scan_port():
    packet=IP(dst=DEST)/TCP(dport=(1,100),flags="S")
    responded, unanswered = sr(packet, timeout=10, verbose=0)

    print "List of all open ports in " + DEST

    for a in responded:
        if a[1][1].flags == 18:
            print a[1].sport

if __name__ == '__main__':
    scan_port()