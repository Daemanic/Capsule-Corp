#!/usr/bin/env python3
import subprocess
import argparse
import re
import platform

def program():
    parse = argparse.ArgumentParser()
    parse.add_argument("-n", "--network", dest="network", required=True, help="interface type for its MAC address")
    parse.add_argument("-m", "--macaddr", dest="address", required=True, help="custom user choice MAC address")
    return parse.parse_args()

def changeMac(network, macadr):
    try:
        if platform.system() == "Linux":
            subprocess.check_call(["sudo", "ifconfig", network, "down"])
            subprocess.check_call(["sudo", "ifconfig", network, "hw", "ether", macadr])
            subprocess.check_call(["sudo", "ifconfig", network, "up"])
        else:
            print(f"[-] error: {platform.system()} system detected")
    except subprocess.CalledProcessError:
        print("[-] error: false root priviledge")

def macOutput(network):
    try:
        result = subprocess.check_output(["ifconfig", network])
        etherMatch = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
        if etherMatch:
            return etherMatch.group(0).lower()
        else:
            print("[-] error: invalid mac-address")
    except subprocess.SubprocessError:
        print("[-] error: failed interface")

args = program()
changeMac(args.network, args.address)
if macOutput(args.network) == str(args.address).lower():
    print(f"[+] mac-address changed to: {str(macOutput(args.network))}")
else:
    print("[-] error: failed to change mac-address")
