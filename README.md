# discord-guest-book
Discord bot for our M426 module project.

Main repository: [lyne/m426](https://github.com/lyne/m426/)

# Installation
## 1. Download Python
You can download python from here: [python.org/downloads](https://www.python.org/downloads/)

## 2. Install Modules
Using pip we install the required python modules:
```
pip install -U discord.py
```
```
pip install -U python-dotenv
```

## 3. Discord Bot Token
In the `src` directory create a new file named `.env`. In that file add the following line:
```
DISCORD_TOKEN=<token>
```
Replace `<token>` with your discord-bots token.

---

To create a Bot and recieve the Token head to [discord.com/developers](https://discord.com/developers/)
