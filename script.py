import bcrypt
passwords = {'student123': 'john@lsus.edu', 'student123': 'alice@lsus.edu', 'clubadmin123': 'sarah@lsus.edu', 'admin123': 'mike@lsus.edu'}
for pw, email in passwords.items():
    h = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
    print(f"UPDATE Users SET PasswordHash='{h}' WHERE Email='{email}';")