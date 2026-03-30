# ARP Spoofing Tool [Educational]

A Python-based ARP spoofing script that demonstrates how ARP poisoning works on a local network. This tool can be used to understand Man-in-the-Middle (MITM) attack concepts in a controlled lab environment.

---

## [?] Features

* Performs ARP spoofing between a target and a gateway
* Continuously sends spoofed ARP replies
* Restores ARP tables on exit (Ctrl+C)
* Uses Scapy for packet crafting
* Simple CLI interface using `argparse`

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

```bash
sudo python3 script.py -t <target-ip> -r <gateway-ip>
```

### Example:

```bash
sudo python3 script.py -t 192.168.1.16 -r 192.168.1.1
```

---

## [?] How It Works

1. Retrieves MAC addresses of:

   * Target device
   * Router (gateway)

2. Sends spoofed ARP responses:

   * Tells target: "I am the router"
   * Tells router: "I am the target"

3. This creates a **Man-in-the-Middle position**

4. Continuously maintains spoofing by sending packets in a loop

5. On exit (`Ctrl+C`):

   * Restores original ARP mappings

---

## [?] ARP Spoofing Flow

```
Target <----> Attacker <----> Router
```

* Traffic is redirected through the attacker machine

---

## [?] Important Notes

* Works only on **local networks (LAN)**
* Requires devices to be on the **same subnet**
* Must be run with **sudo/root privileges**
* May temporarily disrupt network connectivity

---

## [?] Legal Disclaimer

This tool is intended for:

* Educational purposes
* Ethical hacking labs
* Authorized network testing only

**Do NOT use this on networks without permission.**

---

## [?} Project Structure

```
ARP-Spoof/
│── script.py
│── README.md
```

---

## [?] Learning Concepts

* ARP Protocol (Address Resolution Protocol)
* Layer 2 networking
* Packet crafting with Scapy
* Man-in-the-Middle (MITM) attacks
* Network traffic manipulation

---
