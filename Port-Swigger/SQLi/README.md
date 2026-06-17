# SQL Injection (SQLi)

This directory contains my solutions, notes, and payloads for SQL Injection labs from PortSwigger Web Security Academy.

## Overview

SQL Injection is one of the most impactful web application vulnerabilities. It occurs when untrusted user input is incorporated into SQL queries without proper sanitization, allowing attackers to manipulate database queries.

The labs in this directory cover:

* Basic SQL Injection
* Authentication bypass
* UNION attacks
* Determining the number of columns
* Retrieving data from other tables
* Blind SQL Injection
* Error based SQL Injection
* Time based SQL Injection
* Out of band SQL Injection
* Filter bypass techniques

## Directory Structure

```text
SQLi/
├── Lab 01
├── Lab 02
├── Lab 03
├── ...
└── README.md
```

Each lab directory may include:

* Lab description
* Vulnerability explanation
* Payloads used
* Exploitation steps
* Screenshots
* Key takeaways

## Skills Practiced

* Identifying SQL Injection entry points
* Enumerating database structure
* Crafting UNION SELECT payloads
* Exploiting Blind SQL Injection
* Authentication bypass techniques
* Bypassing filters and WAF restrictions
* Database fingerprinting

## Example Payloads

### Authentication Bypass

```sql
' OR 1=1--
```

### UNION Attack

```sql
' UNION SELECT NULL,NULL--
```

### Extract Database Version

```sql
' UNION SELECT @@version,NULL--
```

### Blind SQLi Boolean Condition

```sql
' AND 1=1--
```

## Learning Resources

* PortSwigger Web Security Academy
* SQL Injection Cheat Sheet
* OWASP SQL Injection Prevention Cheat Sheet

## Disclaimer

This repository is intended for educational purposes only.

All exercises are performed within intentionally vulnerable environments provided by PortSwigger Web Security Academy. Do not attempt these techniques against systems without explicit authorization.

## Status

* Ongoing
* Labs are added as I complete them.
