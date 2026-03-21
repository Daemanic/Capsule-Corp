#!/usr/bin/env python
import subprocess
import optparse
import platform

def program(value, change):
    device = platform.system()
    if device == "Darwin" or device == "Linux":
        try:
            subprocess.call(["sudo", "ifconfig", value, "down"], shell=True)
            subprocess.call(["ifconfig", value, "hw", "ether", change], shell=True)
            subprocess.call(["ifconfig", value, "up"], shell=True)
            print(f"[+] changing MAC address to [{change}]")
        except subprocess.CalledProcessError as error:
            print(f"[!] error: {error}")
    else:
        print(f"[-] error: {device.lower()}_detected")

parse = optparse.OptionParser()
parse.add_option("-n", "--network", dest="network", help="interface type to change its MAC address")
parse.add_option("-m", "--macadr", dest="address", help="custom user choice MAC address")
(option, argument) = parse.parse_args()

if not option.network:
    parse.error("false network\n[-] use -h or --help")
elif not option.address:
    parse.error("false macadr\n[-] use -h or --help")
else:
    program(option.network, option.address)
