# MAC Address Changer

A simple Python CLI tool to change the MAC address of a network interface on Linux systems.

## [?] Features

* Change MAC address using command-line arguments
* Uses `argparse` for clean CLI handling
* Verifies MAC address change after execution
* Lightweight and beginner-friendly

## [?] Requirements

* Python3
* Linux OS
* Root privileges `sudo`
* `ifconfig` installed

## [?] Usage

```bash
sudo python3 script.py -n <interface> -m <new-mac>
```

### Example:

```bash
sudo python3 script.py -n eth0 -m 00:11:22:33:44:55
```

## [?] How It Works

1. Parses user input (`-n`, `-m`)
2. Brings network interface down
3. Changes MAC address
4. Brings interface back up
5. Verifies the change using regex

## [?] Notes

* Works only on Linux systems
* Requires root privileges
* `ifconfig` is deprecated on some systems (consider `ip` command)

## [?] Project Structure

```
MAC-Address/
│── mac.py
│── README.md
```

## [?] Learning Concepts

* `argparse` (CLI tools)
* `subprocess` (system commands)
* Regular expressions
* Networking basics (MAC addresses)
