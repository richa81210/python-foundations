

while True:
    password = input("Create a password: ")
    
    if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password):
        print("Strong password! Account created.")
        break
    elif len(password) < 8:
        print("Too short! Must be at least 8 characters.")
    elif not any(c.isdigit() for c in password):
        print("Password must contain at least one number.")
    elif not any(c.isupper() for c in password):
        print("Password must contain at least one uppercase letter.")

