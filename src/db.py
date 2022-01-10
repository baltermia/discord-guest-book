import mysql.connector

username = "gb-user"
password = "root"

def get_conn():
    return mysql.connector.connect(user=username, password=password, host="localhost", database="guestbook")