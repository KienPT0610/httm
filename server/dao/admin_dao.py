from server.dao import DAO
from server.entity.Admin import Admin

class AdminDAO(DAO):
    def checkLogin(self, username, password) -> Admin | None:
        """Kiểm tra thông tin đăng nhập của admin."""
        con = self.connect()
        cursor = con.cursor()
        query = "SELECT * FROM tbladmin WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        row = cursor.fetchone()
        self.close()
        if row:
            return Admin(*row)
        return None
    