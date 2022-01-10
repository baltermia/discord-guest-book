# discord-guest-book
Discord bot for our M426 module project.

Main repository: [lyne/m426](https://github.com/lyne/m426/)

[Bot invitation link](https://discord.com/api/oauth2/authorize?client_id=928313113965649971&permissions=2147486784&scope=bot)

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

# Database
The databases source code is in the main git-repo: [lyne/m426/Database](https://github.com/lyne/m426/Database/)
## 1. Install XAMPP
A MySql Database is used. So for the database to work, you first need to download XAMPP: [apachefriends.org/download.html](https://www.apachefriends.org/download.html)
Download the executeable and install XAMPP on your machine following the steps of the installatin file.

## 2. Create `guestbook` Database
First start `MySQL` and `Apache` from XAMPP. Then Click on the `Admin` Button on `MySQL`. This open the PhpMyAdmin-Portal in your browser.

Now, using the GUI, create a database named `guestbook`.

## 3. Import Database from dump
You can get the dump file from here: [lyne/m426/Database/guests.sql](https://github.com/lyne/m426/Database/guests.sql)

Then, again using the PhpMyAdmin-Portal, import the database into the newly created `guestbook` database.

## 4. Create/Alter user
In the bots source code a default user is used using following credentials:
- `username:` gb-user
- `password:` root

You can either add this user to your database using PhpMyAdmin (again) or use your own user (if you already have a user that has access to all your mysql databases).

To use your own user just paste the credentials into the *TODO*.
