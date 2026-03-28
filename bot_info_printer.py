bot_name = input("What is the bot name? ")
number_of_tasks_automated = int(input("How many tasks have you automated? "))
average_time = float(input("How much time is saved per task in minutes? "))
bot_active = input("Is bot currently active? ")


hours = float(average_time/60)

def summary():
    print("=============================")
    print("       BOT SUMMARY REPORT")
    print("=============================")
    print(f"Bot Name     : {bot_name}")
    print(f"Tasks Done   : {number_of_tasks_automated}")
    print(f"Time Saved   : {average_time:.2f} minutes ({hours:.2f}) hours")
    print(f"Status       : {bot_active}")

    print("=============================")

summary()