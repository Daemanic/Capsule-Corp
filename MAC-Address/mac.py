#!/usr/bin/env python3
import subprocess
import argparse
import re
import platform
import sys
import os


def check_root():
    if os.geteuid() != 0:
        print("\n[-] Error: This script requires root privileges.")
        print("[*] Please run with: sudo python3", " ".join(sys.argv))
        sys.exit(1)

def validate_mac(mac_address):
    pattern = r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
    if re.match(pattern, mac_address):
        return True
    print(f"[-] Error: Invalid MAC address format: {mac_address}")
    print("[*] Expected format: XX:XX:XX:XX:XX:XX")
    return False

def get_current_mac(network):
    try:
        system = platform.system()
        
        if system == "Linux":
            result = subprocess.check_output(
                ["ip", "link", "show", network],
                stderr=subprocess.STDOUT,
                text=True)
            ether_match = re.search(r'link/ether ([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}', result)
            if ether_match:
                return ether_match.group(0).split()[1].lower()
            
            ether_match = re.search(r'HWaddr ([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}', result)
            if ether_match:
                return ether_match.group(0).split()[1].lower()
                
        elif system == "Darwin":
            result = subprocess.check_output(["ifconfig", network], stderr=subprocess.STDOUT, text=True)
            ether_match = re.search(r'ether ([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}', result)
            if ether_match:
                return ether_match.group(1).lower()
        else:
            print(f"[-] Error: Unsupported system: {system}")
            return None 
        print("[-] Error: Could not find MAC address")
        return None
        
    except subprocess.CalledProcessError as error:
        print(f"[-] Error: Failed to get interface info: {error}")
        return None
    except FileNotFoundError:
        print("[-] Error: Required command not found")
        return None


def change_mac(network, mac_address):
    try:
        system = platform.system()
        if system == "Linux":
            try:
                subprocess.check_call(["sudo", "ip", "link", "set", network, "down"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.check_call(["sudo", "ip", "link", "set", network, "address", mac_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.check_call(["sudo", "ip", "link", "set", network, "up"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                subprocess.check_call(["sudo", "ifconfig", network, "down"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.check_call(["sudo", "ifconfig", network, "hw", "ether", mac_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.check_call(["sudo", "ifconfig", network, "up"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
        elif system == "Darwin":
            subprocess.check_call(["sudo", "ifconfig", network, "down"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.check_call(["sudo", "ifconfig", network, "ether", mac_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.check_call(["sudo", "ifconfig", network, "up"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print(f"[-] Error: Unsupported system: {system}")
            return False
        return True
    except subprocess.CalledProcessError:
        print("[-] error: failed to change MAC address (check interface)")
        return False
    except FileNotFoundError:
        print("[-] error: required command not found")
        return False


def check_interface_exists(network):
    try:
        system = platform.system()
        if system == "Linux":
            subprocess.check_call(["ip", "link", "show", network], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif system == "Darwin":
            subprocess.check_call(["ifconfig", network], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        print(f"[-] error: interface '{network}' does not exist")
        return False

def program():
    parse = argparse.ArgumentParser(description="MAC Address Changer - Spoof your MAC address")
    parse.add_argument("-n", "--network", dest="network", required=True, help="network interface name (e.g: eth0, wlan0, en0)")
    parse.add_argument("-m", "--mac", dest="mac_address", required=True,help="new MAC address (format: xx:xx:xx:xx:xx:xx)")
    return parse.parse_args()

if __name__ == "__main__":
    check_root()
    args = program()
    mac_address = args.mac_address.lower()
    if not validate_mac(mac_address):
        sys.exit(1)
    
    if not check_interface_exists(args.network):
        sys.exit(1)
    
    old_mac = get_current_mac(args.network)
    if old_mac:
        print(f"[*] Current MAC: {old_mac}")
    
    print(f"[*] Changing MAC to: {mac_address}")
    if change_mac(args.network, mac_address):
        new_mac = get_current_mac(args.network)
        if new_mac == mac_address:
            print(f"[+] Success! MAC address changed to: {new_mac}")
        else:
            print(f"[-] Warning: MAC mismatch (expected: {mac_address}, got: {new_mac})")
    else:
        print("[-] Failed to change MAC address")
        sys.exit(1)
