# NmapScan
Tool to use Nmap, in Flask with different types of scans. 👁

<p align="center">
<img src="assets/Demo_04.png" title="NmapScan" alt="NmapScan" width="600"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white" alt="Python version">
  <img src="https://img.shields.io/badge/NMAP-SCANNER-red?logo=nmap&logoColor=white">
  <img src="https://img.shields.io/badge/PYTHON-FLASK-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/PENTESTING-AUTOMATION-red?logo=kali-linux&logoColor=white">
  <img src="https://img.shields.io/badge/ACTIVE-RECON-orange?logo=security&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-green?logo=open-source-initiative&logoColor=white" alt="License">
</p>

> **The project is open to partners.**

# SUPPORTED DISTRIBUTIONS
|Distribution | Verified version | 	Supported | 	Status |
|--------------|--------------------|------|-------|
|Kali Linux| 2026.2| ✅| Working   |
|Parrot Security OS| 6.3| ✅ | Working   |
|Windows| 11 | ✅ | Working   |
|BackBox| 9 | ✅ | Working   |
|Arch Linux| 2024.12.01 | ✅ | Working   |

# Root privileges:
To run some types of advanced scans with Nmap (such as -sS, -O, -A), sudo is required. Make sure that the user running the application has the necessary permissions or configure sudo to not prompt for a password when running Nmap (this should be done with caution).

# System Settings:
Sudo permissions without password (optional): If you want to prevent Flask from requesting the sudo password when running certain scans, you can configure sudo to allow the user to run nmap without a password:
```
sudo visudo
```
Then, add a line like the following to the end of the file (replace username with the system user name):
```
username ALL=(ALL) NOPASSWD: /usr/bin/nmap
```

# Solutions:
Run the program as sudo: Since the Flask application is running the Nmap command and it needs root permissions, a straightforward solution is to run Flask with sudo:

## Example:
```
sudo python3 nmap_scan.py
```

However, this is not the most secure solution, especially in a production environment. If you decide to use this method, make sure it is only enabled in controlled environments.

Assign specific permissions to Nmap using setcap: If you want to avoid running the entire Flask script with sudo, you can grant specific permissions to Nmap to run without needing root permissions for certain scans:
```
sudo setcap cap_net_raw,cap_net_admin,cap_net_bind_service+eip $(which nmap)
```
# USAGE
```
git clone https://github.com/HackUnderway/NmapScan.git
```
```
cd NmapScan
```
```
python3 nmap_scan.py
```
# REQUIREMENTS
```
pip install -r requirements.txt
```

<p align="center">
<img src="assets/Demo_01.png" title="NmapScan" alt="NmapScan" width="600"/>
<img src="assets/Demo_02.png" title="NmapScan" alt="NmapScan" width="600"/>
<img src="assets/Demo_03.png" title="NmapScan" alt="NmapScan" width="600"/>
<img src="assets/Demo_04.png" title="NmapScan" alt="NmapScan" width="600"/>
<img src="assets/Report_PDF.png" title="NmapScan" alt="NmapScan" width="600"/>
</p>

# SUPPORT
Questions, bugs or suggestions to : info@hackunderway.com

# LICENSE
- [x] NmapScan is licensed. 
- [x] See [LICENSE](https://github.com/HackUnderway/NmapScan#MIT-1-ov-file) for more information.

We need partners and sponsors, if you're interested in support or help contact.

# 👨‍💻 Author

* [Victor Bancayan](https://www.offsec.com/bug-bounty-program/) - (**CEO at [Hack Underway](https://hackunderway.com/)**) 

---

<h2 align="center">🕵️‍♂️ OSINT Platform</h2>
<p align="center">
  <a href="https://hackunderway.io/" target="_blank">
    <img src="https://img.shields.io/badge/Try%20Enterprise%20Mode-hackunderway.io-0088CC?style=for-the-badge&logo=internet&logoColor=white" alt="OSINT Platform">
  </a>
</p>
<p align="center">
  <b>Automate OSINT processes</b><br>
  New <b>Enterprise Mode</b> – Maltego-inspired interface with visual graphs and professional workflows.<br>
  <a href="https://hackunderway.io/new-update-to-our-osint-platform-hack-underway/" target="_blank">📢 See what's new</a>
</p>

## 🔗 Links
[![Patreon](https://img.shields.io/badge/patreon-000000?style=for-the-badge&logo=Patreon&logoColor=white)](https://www.patreon.com/c/HackUnderway)
[![Web site](https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox&logoColor=white)](https://hackunderway.com)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/HackUnderway)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@JeyZetaOficial)
[![Twitter/X](https://img.shields.io/badge/Twitter/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/JeyZetaOficial)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/hackunderway)
[![TryHackMe](https://img.shields.io/badge/TryHackMe-212C42?style=for-the-badge&logo=tryhackme&logoColor=white)](https://tryhackme.com/p/JeyZeta)

## ☕️ Support the project

If you like this tool, consider buying me a coffee:

[![Buy Me a Coffee](https://img.shields.io/badge/-Buy%20me%20a%20coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/hackunderway)

## 🌞 Subscriptions

###### Subscribe to: [Jey Zeta](https://www.facebook.com/JeyZetaOficial/subscribe/)

[![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)](https://www.kali.org/)

from <img src="https://i.imgur.com/ngJCbSI.png" title="Perú"> made in <img src="https://i.imgur.com/NNfy2o6.png" title="Python"> + <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white" height="13"> with <img src="https://i.imgur.com/S86RzPA.png" title="Love"> by: <font color="red">Victor Bancayan</font>

© 2026
