#!/usr/bin/env python3
import argparse
import scapy.all as scapy
import prettytable

def program():
    parse = argparse.ArgumentParser()
    parse.add_argument("-i", "--ipadr", dest="ip", required=True, help="enter local network ip-address")
    return parse.parse_args()

def scan(ip):
    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/request
    receivedList = scapy.srp(packet, verbose=False, timeout=1)[0]
    table = prettytable.PrettyTable(["IP", "MAC Address"])
    for index in receivedList:
        table.add_row([index[1].psrc, index[1].src])
    print(table)

args = program()
scan(args.ip)
