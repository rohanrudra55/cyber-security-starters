#!/usr/local/bin/python3
# to optimise we can import selective funcionalities
from scapy.all import *

# some random common ports
ports = [25,80,53,443,445,8080,8443]

def SynScan(host):
    """
    sr(...) = send the packet
    Ip = IP address of the host we are specifing
    sport =  to check the traffic comming and going from this port
    flag = sending 'S" sin scan packets 
    It till handle to build and send packets
    ans = open ports
    unans = close ports
    """
    ans,unans = sr(IP(dst=host)/TCP(sport=5555,dport=ports,flags="S"),timeout=2,verbose=0)
    print("Open ports at %s:" % host)
    for(s,r,) in ans:
        """
        s[TCP] = send TCP Packet
        r[TCP] = received TCP Packet
        """
        if s[TCP].dport == r[TCP].sport:
            print(s[TCP].dport)

def DNSScan(host):
    """
    rd = request
    DNSQR = DNS querry
    53 = specifies DNS server
    """
    ans, unans = sr(IP(dst=host)/UDP(sport=5555, dport=53)/DNS(rd=1,qd=DNSQR(qname="randritas.wixsite.com/rsm2m")), timeout=2, verbose=0)
    if ans:
        print("DNS Server at %s" % host)


host = "192.168.0.1"

SynScan(host)
DNSScan(host)
