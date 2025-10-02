from server.controller.server_controller import ServerController

controller = ServerController()
if __name__ == "__main__":
    admin = controller.login("adminA", "123456")
    if admin:
        print("Login successful:", admin)
    else:
        print("Login failed")