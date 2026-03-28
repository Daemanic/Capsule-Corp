#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import prettytable

def program():
    parse = argparse.ArgumentParser()
    parse.add_argument("-t", "--target", dest="IP", required=True, help="enter network address")
    return parse.parse_args()

def scan(ip):
    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/request
    receivedList = scapy.srp(packet, verbose=False, timeout=1)[0]
    display = prettytable.PrettyTable(["IP", "MAC Address"])
    for index in receivedList:
        display.add_row([index[1].psrc, index[1].hwsrc])
    print(display)

args = program()
scan(args.ip)
