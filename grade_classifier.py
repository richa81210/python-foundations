def get_season(month):
    match month:
        case 12 | 1 | 2:
            return "Winter"
        case 3 | 4 | 5:
            return "Spring"
        case 6 | 7 | 8:
            return "Summer"
        case 9 | 10 | 11:
            return "Autumn"
        case _:
            return "Invalid"
        
def main():
    month = int(input("Enter the month number (1-12): "))
    season = get_season(month)
    print(f"The season is: {season}")

if __name__ == "__main__":
    main()