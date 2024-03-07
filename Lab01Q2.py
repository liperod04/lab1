user_input = str(input('Enter integer: ')) # Takes in user input integer

digit_count = len(user_input) # Takes length/number of digits from user input

if digit_count == 1: # Checks if "digit" should be set to singular or plural
    print(f'{user_input} has {digit_count} digit')
else:
    print(f'{user_input} has {digit_count} digits')