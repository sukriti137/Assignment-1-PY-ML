import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

if __name__ == "__main__":
    try:
        birth_year = int(input("Enter your birth year: "))
        if birth_year > 0 and birth_year <= datetime.datetime.now().year:
            age = calculate_age(birth_year)
            print(f"You are {age} years old.")
        else:
            print("Please enter a valid birth year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")
