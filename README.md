# NmapScan
Tool to use Nmap, in Flask with different types of scans. 👁

[![Join our Fanpage](https://img.shields.io/badge/Join%20Our%20Fanpage-Hack%20Underway-1.svg)](https://www.facebook.com/HackUnderway/)

![NmapScan](https://github.com/HackUnderway/NmapScan/blob/main/Nmap_Scan.png)
![NmapScan](https://github.com/HackUnderway/NmapScan/blob/main/Dark.png)
![NmapScan](https://github.com/HackUnderway/NmapScan/blob/main/Light.png)
![NmapScan](https://github.com/HackUnderway/NmapScan/blob/main/Options_Nmap.png)

> **The project is open to partners.**

# SUPPORTED DISTRIBUTIONS
|Distribution | Version Check | supported | status |
----------|-------|------|-------|
|Kali Linux| 2024.3| yes| working   |
|Parrot Security OS| 6.0| yes | working   |
|Windows| 11 | yes | working   |
|BackBox| 8.1 | yes | working   |
|Arch Linux| 2024.06.01 | yes | working   |

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
sudo python3 app.py
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
# SUPPORT
Questions, bugs or suggestions to : info@hackunderway.com

# LICENSE
- [x] NmapScan is licensed. 
- [x] See [LICENSE](https://github.com/HackUnderway/NmapScan#MIT-1-ov-file) for more information.

We need partners and sponsors, if you're interested in support or help contact.

# SECURITY RESEARCHER

* Victor Bancayan - [@VictorBancayan](https://twitter.com/VictorBancayan) - (**CEO at [Hack Underway](https://www.instagram.com/hackunderway/)**) 

## 🔗 LINKS
[![PATREON](https://img.shields.io/badge/patreon-000000?style=for-the-badge&logo=Patreon&logoColor=white)](https://www.patreon.com/c/HackUnderway)
```
Fanpage: https://www.facebook.com/HackUnderway
X: https://twitter.com/JeyZetaOficial
Web site: https://hackunderway.com
Youtube: https://www.youtube.com/@JeyZetaOficial
```
[![Kali Linux Badge](https://img.shields.io/badge/Kali%20Linux-1793D1?logo=kalilinux&logoColor=fff&style=plastic)](https://www.facebook.com/HackUnderway/)

from <img src="https://i.imgur.com/ngJCbSI.png" title="Perú"> made in <img src="https://i.imgur.com/NNfy2o6.png" title="Python"> with <img src="http://cdn0.bodas.com.mx/img/smileys/smiley_heart.png" title="Love"> by: <font color="red">Victor Bancayan</font>, if you want Donate <a href="https://www.buymeacoffee.com/HackUnderway"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=HackUnderway&button_colour=40DCA5&font_colour=ffffff&font_family=Comic&outline_colour=000000&coffee_colour=FFDD00" /></a>

© 2024
