#!/usr/bin/env python3
import scapy.all as scapy
import optparse

def program():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--ipadr", dest="ip", help="enter local network gateway")
    (option, argument) = parse.parse_args()
    if not option.ip:
        parse.error("use -h or --help")
    return option

def scan(ip):
    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/request
    receivedList, unused = scapy.srp(packet, verbose=False, timeout=1)
    print(receivedList.summary())

option = program()
scan(option.ip)
