# ARP Spoofing & Packet Sniffing Tool [Educational]

A Python-based toolkit that demonstrates **ARP spoofing (MITM)** and **HTTP packet sniffing** on a local network. This project is designed to help understand how attackers can intercept and analyze network traffic in a controlled lab environment.

---

## [?] Features

### ARP Spoofing (`arp.py`)

* Performs ARP poisoning between a target and a gateway
* Positions attacker as **Man-in-the-Middle (MITM)**
* Continuously sends spoofed ARP replies
* Restores ARP tables on exit (Ctrl+C)

### Packet Sniffing (`sniff.py`)

* Captures HTTP traffic on the network
* Extracts visited URLs
* Detects possible login data (e.g., usernames, passwords)
* Uses Scapy for packet inspection

---

## [?] Requirements

* Python 3
* Root privileges (required for Scapy)
* Scapy library

### Dependencies:

```bash
pip install scapy
```

---

## [?] Usage

### 1. Start ARP Spoofing

```bash
sudo python3 arp.py -t <target-ip> -r <gateway-ip>
```

**Example:**

```bash
sudo python3 arp.py -t 192.168.1.16 -r 192.168.1.1
```

---

### 2. Start Packet Sniffing

Run this in a **separate terminal**:

```bash
sudo python3 sniff.py -n <interface>
```

**Example:**

```bash
sudo python3 sniff.py -n en0
```

---

## [?] How It Works

1. **ARP Spoofing**

   * Sends fake ARP replies to both target and router
   * Tricks them into routing traffic through the attacker

2. **MITM Position**

   ```
   Target <----> Attacker <----> Router
   ```

3. **Packet Sniffing**

   * Captures intercepted traffic
   * Extracts:

     * URLs
     * Potential login credentials (HTTP only)

---

## [?] Important Notes

* Works only on **local networks (LAN)**
* Devices must be on the **same subnet**
* Requires **sudo/root privileges**
* Works mainly on **HTTP (not HTTPS)**
  *(HTTPS traffic is encrypted and cannot be read)*
* May temporarily disrupt network connectivity

---

## [?] Project Structure

```
ARP-Spoof/
│── arp.py
│── sniff.py
│── README.md
```

---

## [?] Learning Concepts

* ARP Protocol (Address Resolution Protocol)
* Layer 2 networking
* Man-in-the-Middle (MITM) attacks
* Packet sniffing and analysis
* Network security fundamentals

---

## [?] Legal Disclaimer

This project is intended for:

* Educational purposes
* Ethical hacking labs
* Authorized network testing only

---
