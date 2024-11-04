#1

def check_letter():
    vowels = {'a', 'e', 'i', 'o', 'u'}

  
    letter = input("Please enter a letter (a-z or A-Z): ").strip()

    
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single letter.")
        return

   
    letter_lower = letter.lower()

    
    if letter_lower in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")


check_letter()




#2

def check_voting_eligibility():
    voting_age = 18  
    age_input = input("Please enter your age: ")

    try:
        age = int(age_input) 
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age >= voting_age:
            print("You are eligible to vote!")
        else:
            print("You are not old enough to vote.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for your age.")


check_voting_eligibility()


def calculate_dog_years():
    dog_age = int(input("input dogs age:"))
    
    if age < 0:
        print("Age cannot be negative.")
        return  
    elif age == 0:
        dog_years = 0
    elif age == 1:
        dog_years = 10
    elif age == 2:
        dog_years = 20
    else:
        dog_years = 20 + (age - 2) * 7
    
    
    print(f"The dog's age in dog years is {dog_years}.")


calculate_dog_years()

#4


def weather_advice():
   
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()

    if cold == 'yes' and raining == 'yes':
        print("Wear a waterproof coat.")
    elif cold == 'yes' and raining == 'no':
        print("Wear a warm coat.")
    elif cold == 'no' and raining == 'yes':
        print("Carry an umbrella.")
    elif cold == 'no' and raining == 'no':
        print("Wear light clothing.")
    else:
        print("Please enter 'yes' or 'no' for both questions.")


weather_advice()

#5 

def determine_season():
    
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    day = input("Enter the day of the month: ").strip()

    
    if not day.isdigit() or int(day) < 1 or int(day) > 31:
        print("Please enter a valid day of the month (1-31).")
        return

    day = int(day)

   
    if month == "December":
        if day >= 21:
            season = "Winter"
        else:
            season = "Fall"
    elif month == "January" or month == "February":
        season = "Winter"
    elif month == "March":
        if day < 20:
            season = "Winter"
        else:
            season = "Spring"
    elif month == "April" or month == "May":
        season = "Spring"
    elif month == "June":
        if day < 21:
            season = "Spring"
        else:
            season = "Summer"
    elif month == "July" or month == "August":
        season = "Summer"
    elif month == "September":
        if day < 22:
            season = "Summer"
        else:
            season = "Fall"
    elif month == "October" or month == "November":
        season = "Fall"
    else:
        print("Please enter a valid month (Jan - Dec).")
        return

    
    print(f"{month} {day:02} is in {season}.")


determine_season()

