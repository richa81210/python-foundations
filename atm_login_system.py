i = 3
while i > 0:
    pin = input("Enter PIN: ")
    if pin == "1234":
        print("Access granted. Welcome!")
        break
    else:
        i -= 1
        if i > 0:
            attempt_str = "attempt" if i == 1 else "attempts"
            print(f"Wrong PIN. {i} {attempt_str} remaining.")

if i == 0:
    print("Card blocked. Too many wrong attempts.")