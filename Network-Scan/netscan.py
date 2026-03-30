#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import prettytable

def program():
    parse = argparse.ArgumentParser()
    parse.add_argument("-t", "--target", dest="ip", required=True, help="enter network address")
    return parse.parse_args()

def scan(ip):
    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/request
    try:
        receivedList = scapy.srp(packet, verbose=False, timeout=2)[0]
    except Exception as error:
        print(f"\n[-] error: {errro}")
        return

    if not receivedList:
        print("\n[-] error: no devices found")
        return
    display = prettytable.PrettyTable(["IP", "MAC Address"])
    for index in receivedList:
        display.add_row([index[1].psrc, index[1].hwsrc])
    print(display)

args = program()
scan(args.ip)
