from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# ==============================
# OWASP A2: Hardcoded Secret
# ==============================
app.secret_key = "secret123"   # ❌ Hardcoded secret key

# ==============================
# Database Setup
# ==============================
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', '1234')")
conn.commit()

# ==============================
# OWASP A3: SQL Injection
# ==============================
@app.route("/search")
def search():
    user = request.args.get("user")

    # ❌ Vulnerable SQL query
    query = "SELECT * FROM users WHERE username = '" + user + "'"
    cursor.execute(query)

    return str(cursor.fetchall())

# ==============================
# OWASP A7: Cross-Site Scripting (XSS)
# ==============================
@app.route("/xss")
def xss():
    name = request.args.get("name")
    # ❌ No output encoding
    return f"<h1>Hello {name}</h1>"

# ==============================
# OWASP A1: Broken Authentication
# ==============================
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # ❌ Weak authentication
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Login Failed"

# ==============================
# OWASP A5: Command Injection
# ==============================
@app.route("/cmd")
def cmd():
    command = request.args.get("cmd")
    # ❌ Command injection
    return os.popen(command).read()

# ==============================
# OWASP A6: Security Misconfiguration
# ==============================
@app.route("/debug")
def debug():
    # ❌ Sensitive information disclosure
    return str(app.config)

# ==============================
# Run App
# ==============================
if __name__ == "__main__":
    app.run(debug=True)
