name = input("What is your name? ")
birth_year = int(input("What is your birth year?" ))

def details():
    age_in_2025 = 2025 - birth_year
    year_whenthey_turn100 = (100 - age_in_2025) + 2025
    above18 = bool(age_in_2025 > 18)

    print(f"Name: {name}")
    print(f"How old they are in 2025: {age_in_2025}")
    print(f"What year they will turn 100: {year_whenthey_turn100}")
    print(f"Whether they are above 18 (True or False): {above18}")

details()
