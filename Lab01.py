user_year = int(input('Enter year: ')) #Takes user's inp year and stores it

if user_year % 100 == 0 and user_year % 400 == 0: #Checks if year is a century year
    print(f'{user_year} is a leap year')
elif user_year % 100 != 0 and user_year % 4 == 0: #If year NOT a century year
    print(f'{user_year} is a leap year')
else:
    print(f'{user_year} is not a leap year')