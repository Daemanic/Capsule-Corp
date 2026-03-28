# Network Scanner [ARP Scanner]

A Python-based network scanner that discovers devices on a local network using ARP requests.

## [?] Features

* Scans a network range (CIDR)
* Displays IP and MAC addresses of active devices
* Uses Scapy for packet crafting
* Clean table output using PrettyTable

## [?] Requirements

* Python3
* Root privileges (required for Scapy)
* Scapy
* PrettyTable

### Install dependencies:

```bash
pip install scapy prettytable
```

## [?] Usage

```bash
sudo python3 script.py -t <target-network>
```

### Example:

```bash
sudo python3 script.py -t 192.168.1.1/24
```

## [?] How It Works

1. Creates ARP request packets
2. Broadcasts them to the network
3. Collects responses from active devices
4. Extracts:

   * IP address
   * MAC address
5. Displays results in a table

## 📊 Sample Output

```
+--------------+-------------------+
| IP           | MAC Address       |
+--------------+-------------------+
| 192.168.1.1  | aa:bb:cc:dd:ee:ff |
| 192.168.1.5  | 11:22:33:44:55:66 |
+--------------+-------------------+
```

## [?] Notes

* Works only on local networks (LAN)
* Requires root privileges
* ARP does not work across routers

## [?] Project Structure

```
Network-Scan/
│── script.py
│── README.md
```

## [?] Learning Concepts

* ARP protocol
* Packet crafting with Scapy
* Layer 2 networking
* CLI tools with `argparse`
