# Pythagorean Theorem Calculator Calculator

# Imports
import math

# Title
print('------------------------------------------------------------------------------')
print(' Pythagorean Theorem Calculator')
print('------------------------------------------------------------------------------')
print('')
print('')
print('                                   |\\')
print('                                   | \\')
print('                                  A|  \\C')
print('                                   |   \\')
print('                                   -----')
print('                                     B')
print('')
print('------------------------------------------------------------------------------')
print(' What would you like to do?:')
print('------------------------------------------------------------------------------')
print(' [1] Calculate side A')
print(' [2] Calculate side B')
print(' [3] Calculate side C')
print('------------------------------------------------------------------------------')
print('')

# Choose What you would like to do
while True:
    sides_choosing_answer = input('Please choose 1 or 2 or 3: ')

    # Calculate side A
    if sides_choosing_answer == '1':
        
        # Makes sure that the numbers provided are valid
        while True:
            try:
                print('')
                Side_C_Length = float(input('What is the length of Side C in cm?: '))
                Side_B_Length = float(input('What is the length of Side B in cm?: '))
                
                if Side_C_Length <= Side_B_Length:
                    print('Side C must be longer than Side B for a valid right angle triangle.')
                    continue

                final_answer = math.sqrt(pow(Side_C_Length, 2) - pow(Side_B_Length, 2))
                side_found = 'A'
                break

            except ValueError:
                print('That is not a valid number Set! Try again.')

    # Calculate side B
    elif sides_choosing_answer == '2':
        
        # Makes sure that the numbers provided are valid
        while True:
            try:
                print('')
                Side_C_Length = float(input('What is the length of Side C in cm?: '))
                Side_A_Length = float(input('What is the length of Side A in cm?: '))

                if Side_C_Length <= Side_A_Length:
                    print('Side C must be longer than Side A for a valid right triangle.')
                    continue

                final_answer = math.sqrt(Side_C_Length**2 - Side_A_Length**2)
                side_found = 'B'
                break

            except ValueError:
                print('That is not a valid number! Try again.')

    # Calculate side C
    elif sides_choosing_answer == '3':
        
        # Makes sure that the numbers provided are valid
        while True:
            try:
                print('')
                Side_A_Length = float(input('What is the length of Side A in cm?: '))
                Side_B_Length = float(input('What is the length of Side B in cm?: '))

                final_answer = math.sqrt(Side_A_Length**2 + Side_B_Length**2)
                side_found = 'C'
                break

            except ValueError:
                print('That is not a valid number! Try again.')

    # If 1 or 2 or 3 was not entered
    else: 
        print('Please enter either 1 or 2 or 3.')
        continue
    
    break

print('')
print('------------------------------------------------------------------------------')
print(f'The length of side {side_found} is {round(final_answer, 3)} cm rounded to 3 D.P.')
print('------------------------------------------------------------------------------')
print('')
input('Press the Enter Key to Exit...')