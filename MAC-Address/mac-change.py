#!/usr/bin/env python
import subprocess
import optparse
import re
import platform

def program():
    parse = optparse.OptionParser()
    parse.add_option("-n", "--network", dest="network", help="interface type to change its MAC address")
    parse.add_option("-m", "--macaddr", dest="address", help="custom user choice MAC address")
    (option, argument) = parse.parse_args()
    if not option.network or not option.address:
        parse.error("use -h or --help")
    else:
        return option

def changeMac(network, macadr):
    device = platform.system()
    if device == "Darwin" or device == "Linux":
        try:
            subprocess.call(["sudo", "ifconfig", network, "down"])
            subprocess.call(["sudo", "ifconfig", network, "hw", "ether", macadr])
            subprocess.call(["sudo", "ifconfig", network, "up"])
        except subprocess.CalledProcessError:
            print("[-] error: false root priviledge")
    else:
        print(f"[-] error: {device} system detected")

def macOutput(network):
    try:
        result = subprocess.check_output(["ifconfig", network])
        etherMatch = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
        if etherMatch:
            return etherMatch.group(0)
        else:
            print("[-] error: invalid mac-address")
    except subprocess.SubprocessError:
        print("[-] error: failed interface")

option = program()
changeMac(option.network, option.address)
if macOutput(option.network) == str(option.address):
    print(f"[+] mac-address changed to: {str(macOutput(option.network))}")
else:
    print("[-] error: failed to change mac-address")
