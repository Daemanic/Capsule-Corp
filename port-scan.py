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
            print(f"\n[!] syntax-error: [?D]\n")
            return None

def searchIP(ipadr, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        sock.connect((ipadr, port))
        if port == 80:
            request = "GET / HTTP/1.0\r\nHost: {}\r\n\r\n".format(ipadr)
            sock.send(request.encode())
        try:
            service = sock.recv(1024)
            status = service.decode().split('\n')[0]
            print(f"[+] status: [{port}] | [UP] {status}\n")
        except socket.timeout:
            print(f"[+] status: [{port}] | [NB]\n")
        sock.close()
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
    port = input("[?] port: ")
    print(f"[?] target: {domain}\n")
    for endPort in port.split():
        try:
            if 0 < int(endPort) < 65536:
                searchIP(domain, int(endPort))
            else:
                print(f"\n[!] end-port: [?P]\n")
        except ValueError:
            print(f"\n[!] syntax-error: [?D]\n")

if __name__ == "__main__":
    try:
        target = input("\n[?] domain: ")
    except KeyboardInterrupt:
        print(f"\n[0]")
        sys.exit()
    try:
        for perIP in target.split():
            scanIP(perIP)
    except KeyboardInterrupt:
        print(f"\n[0]")
        sys.exit()
