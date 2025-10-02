import mysql.connector

class DAO:
    def __init__(self, host="localhost", user="root", password="12345", database="httm"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.con = None

    def connect(self):
        """Mở kết nối đến cơ sở dữ liệu MySQL."""
        self.con = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.con

    def close(self):
        """Đóng kết nối đến cơ sở dữ liệu MySQL."""
        if self.con:
            self.con.close()
            self.con = None

    