import dns
import dns.resolver
import socket

def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]]+result[1]

def DNSRequest(domain):
    """
    'A' = is a type of record
    Check if any other domain is associated with that IP Address
    """
    try:
        result =dns.resolver.resolve(domain,'A')
        if result:
            print(domain)
            for answer in result:
                print(answer)
                print("Domain Names: %s" % ReverseDNS(answer.to_text()))
    except(dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return

def SubdomainSearch(domain,dictionary,nums):
    """
    add domain and subdomains to make a complete domain.
    some also have a numeric digit associated with domain name, we 
    will also test that here
    """
    for word in dictionary:
        subdomain = word+"."+domain
        DNSRequest(subdomain)
        if nums:
            for i in range(0,10):
                s = word+str(i)+"."+domain
                DNSRequest(s)

domain = "google.com"
d = "subdomains.txt"
with open(d,"r") as f:
    dictionary = f.read().splitlines()
SubdomainSearch(domain,dictionary,True)
