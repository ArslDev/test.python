import sqlite3
import os

# ==============================
# 1) Hard-coded Credentials
# ==============================
DB_PASSWORD = "admin123"   # ❌ Hard-coded password

# ==============================
# Database Setup
# ==============================
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', '1234')")
conn.commit()

print("=== Vulnerable Python Program ===")

# ==============================
# 2) SQL Injection
# ==============================
username = input("Enter username to search: ")

# ❌ Vulnerable SQL Query
query = "SELECT * FROM users WHERE username = '" + username + "'"
cursor.execute(query)
print("User Data:", cursor.fetchall())

# ==============================
# 3) Weak Authentication
# ==============================
login_user = input("Login Username: ")
login_pass = input("Login Password: ")

# ❌ Weak login logic
if login_user == "admin" and login_pass == "1234":
    print("Login Successful!")
else:
    print("Login Failed!")

# ==============================
# 4) Command Injection
# ==============================
file_name = input("Enter file name to view: ")

# ❌ Command Injection vulnerability
os.system("type " + file_name)  # Windows
# os.system("cat " + file_name) # Linux / Mac

# ==============================
# 5) Path Traversal / Insecure File Write
# ==============================
new_file = input("Enter file name to create: ")

# ❌ No file validation
with open(new_file, "w") as f:
    f.write("This is a vulnerable file write example.")

print("File created successfully!")
