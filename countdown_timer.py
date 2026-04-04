def timer():
    while True:
        countdown_number = int(input("Enter countdown number: "))
        if countdown_number <= 0:
            print("Invalid! Enter a positive number.")
        else:
            while countdown_number != 0:
                print(countdown_number)
                countdown_number = countdown_number - 1

            print("Blast off! 🚀")
            break

timer()

while True:
    countdown_again = input("Count down again? (yes/no): ")
    if countdown_again.strip().lower() == "yes":
        timer()
    else:
        print("Goodbye!")
        break
