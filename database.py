import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='tiger',
                database='bookstore'
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close() 