# 🕹️ TELNET.LIVE
 Python powered website using flask to display html and handle routing hosted in a RPI 4

More will come to this project as is it a home for my work

If you want to alter or add to this script please feel free to do so

![PICTURE](https://raw.githubusercontent.com/Quinny-J/telnet.live/main/snap.png)

# ⚡ Getting Started

Install Python **[Link](https://www.python.org/downloads/)**

Follow these steps

```bash
# Goto Dir
$ cd telnet.live

# Install Requirements
$ pip install requirements.txt

# Run It !
$ python -m flask run

```

## 📕 Reference 
- Flask - https://flask.palletsprojects.com/en/3.0.x/

## 📝 Todo (maybe)
- Guide for RPI/VPS installation (Self/Paid Hosting)
- Add a protected route like a login page or members area
- Integrate other python projects to make a hub for my work
- SteamAPI steamyFlask integration 

## 📜 steamyFlask API
- `/api/v1/sf/level/?steam_id=STEAMIDHERE` <br>
↳ Returns the level of the steamid supplied
- `/api/v1/sf/level/needed_xp/?steam_id=STEAMIDHERE` <br>
↳ Returns the amount of xp needed to rank up the the next rank based of the steamid supplied
- `/api/v1/sf/level/total_xp/?steam_id=STEAMIDHERE` <br>
↳ Returns the total xp earned from the steamid supplied


