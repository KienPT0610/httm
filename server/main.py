from flask import Flask, render_template, request, redirect, url_for, session
from server.controller.server_controller import ServerController
import os

# Lấy đường dẫn tuyệt đối tới thư mục client
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "client", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "client", "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = "secret_key_123"
controller = ServerController()

@app.route("/")
def index():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    print(f"Attempting login with username: {username} and password: {password}")
    admin = controller.login(username, password)
    if admin:
        session["admin"] = admin
        return redirect(url_for("dashboard"))
    return render_template("login.html", error="Invalid credentials")

@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect(url_for("login"))
    # servers = controller.get_all_servers()
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)