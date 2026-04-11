# CAPTCHA-Based Login Automation (Educational)

A Python script that demonstrates automated interaction with a login system protected by CAPTCHA using OCR (Optical Character Recognition).

This project is intended for **learning purposes**, showcasing how CAPTCHA systems work and how automation tools interact with web authentication flows.

---

## [?] Features

* Fetches CAPTCHA images from a web server
* Uses OCR (`pytesseract`) to extract CAPTCHA text
* Automates login attempts using username and password wordlists
* Handles CAPTCHA failures and retries dynamically
* Uses persistent sessions (`requests.Session`) to maintain cookies

---

## [?] Requirements

* Python 3
* Tesseract OCR engine
* Python libraries:

  * `requests`
  * `pytesseract`
  * `Pillow`

### Dependencies:

```bash id="4c4n5h"
pip install requests pytesseract pillow
```

### Install Tesseract:

#### macOS:

```bash id="l7i8x0"
brew install tesseract
```

#### Linux:

```bash id="y3d8gp"
sudo apt install tesseract-ocr
```

---

## [?] Usage

```bash id="5q9m7v"
python3 script.py -u <url> -f <username_wordlist> -p <password_wordlist>
```

### Example:

```bash id="k1r9sl"
python3 script.py -u http://example.com -f users.txt -p passwords.txt
```

---

## [?] How It Works

1. Establishes a session with the target website
2. Retrieves CAPTCHA image from `/captcha`
3. Converts image to text using OCR
4. Sends login request with:

   * Username
   * Password
   * CAPTCHA solution
5. Handles responses:

   * Retries if CAPTCHA fails
   * Moves to next credentials if incorrect
   * Stops when login is successful

---

## [?] Workflow

```id="d8p9zs"
Fetch CAPTCHA → Solve with OCR → Attempt Login → Analyze Response → Repeat
```

---

## [?] Important Notes

* OCR accuracy may vary depending on CAPTCHA complexity
* Works best on **simple numeric CAPTCHAs**
* Requires stable network connection
* May not work on advanced CAPTCHA systems (e.g., reCAPTCHA)

---

## [?] Legal Disclaimer

This project is intended for:

* Educational purposes
* Security research in controlled environments
* Authorized testing only

Do NOT use this tool on systems without explicit permission.

---

## [?] Project Structure

```id="h7k2pl"
Project/
│── script.py
│── README.md
│── users.txt
│── passwords.txt
```

---

## [?] Learning Concepts

* HTTP requests and sessions
* CAPTCHA mechanisms
* OCR (Optical Character Recognition)
* Automation with Python
* Basic authentication workflows

---
