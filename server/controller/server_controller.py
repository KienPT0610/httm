from server.dao.admin_dao import AdminDAO

class ServerController:
    def __init__(self):
        self.adminDao = AdminDAO()
    
    def login(self, username, password):
        return self.adminDao.checkLogin(username, password)