import sys
import socket
from IPy import IP

def checkIP(ipadr):
    try: 
        IP(ipadr)
        return str(ipadr)
    except ValueError:
        try:
            host = socket.gethostbyname(ipadr)
            return host
        except socket.gaierror:
            print(f"\n[!] error: invalid")
            return None

def getBanner(socketValue):
    return socketValue.recv(1024)

def searchIP(ipadr, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        sock.connect((ipadr, port))
        try:
            service = getBanner(sock)
            print(f"[+] status: [{port}] | [UP] | {service.decode()}\n")

            sock.close()
        except socket.timeout:
            print(f"[+] status: [{port}] | [NB]\n")
    except socket.timeout:
        print(f"[-] status: [{port}] | [TO]\n")
    except ConnectionRefusedError:
        print(f"[-] status: [{port}] | [RE]\n")
    except OSError as e:
        print(f"[-] status: [{port}] | [OS]\n")
     
def scanIP(ipadr):
    domain = checkIP(ipadr)
    if domain is None:
        return
    print(f"\n[?] target: {domain}\n")
    for port in range(0,521):
        searchIP(domain, port)

if __name__ == "__main__":
    target = input("\n~ ")
    try:
        if " " in target:
            for perIP in target.split(" "):
                scanIP(perIP)
        else:
            scanIP(target)
    
    except KeyboardInterrupt:
        print("\n[0] executed: ")
        sys.exit()
