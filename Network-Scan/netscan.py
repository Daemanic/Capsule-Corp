#!/usr/bin/env python3
import argparse
import scapy.all as scapy

def program():
    parse = argparse.ArgumentParser()
    parse.add_argument("-i", "--ipadr", required=True, help="enter local network gateway")
    return parse.parse_args()

def scan(ip):
    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/request
    receivedList, unused = scapy.srp(packet, verbose=False, timeout=1)
    print(receivedList.summary())

args = program()
scan(args.ip)
