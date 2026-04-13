#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import prettytable
import sys
import os

def check_root():
    if os.geteuid() != 0:
        print("\n[-] error: root privileges required")
        print("[?] run with: sudo python3", " ".join(sys.argv))
        sys.exit(1)

def program():
    parse = argparse.ArgumentParser(description="Network Scanner - discover devices on a network")
    parse.add_argument("-t", "--target", dest="ip", required=True, help="target network address (e.g., 192.168.1.1/24)")
    parse.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")
    return parse.parse_args()

def scan(ip, verbose=False):
    try:
        request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = broadcast / request
        if verbose:
            print("[+] sending ARP requests to", ip)
        receivedList = scapy.srp(packet, verbose=verbose, timeout=5)[0]

    except PermissionError:
        print("\n[-] error: permission denied (run with sudo)")
        return []
    except Exception as e:
        print(f"\n[-] error: {e}")
        return []

    if not receivedList:
        print("\n[-] failure: no devices found on the network")
        return []
    results = []
    for element in receivedList:
        results.append({"ip": element[1].psrc, "mac": element[1].hwsrc})
    return results

def display_results(results):
    if not results:
        return
    table = prettytable.PrettyTable(["IP Address", "MAC Address"])
    table.align["IP Address"] = "l"
    table.align["MAC Address"] = "l"
    for device in results:
        table.add_row([device["ip"], device["mac"]])
    print("\n" + str(table))
    print(f"[+] found {len(results)} device(s)\n")


if __name__ == "__main__":
    check_root()
    args = program()
    results = scan(args.ip, verbose=args.verbose)
    display_results(results)
