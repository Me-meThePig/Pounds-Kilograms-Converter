# prompt user for their weight
weight = float(input('Enter your weight: '))
unit = input('Is your weight measured in kilograms (kg) or pounds (pd): ').lower()

# convert weight
try:
    if unit == ('kg' or 'kilogram' or 'kilograms'):
        print(f'{weight} kilograms is equal to {round(weight * 2.204623, 3)} pounds.')
    elif unit == ('pd' or 'pound' or 'pounds'):
        print(f'{weight} pounds is equal to {round(weight * 0.453592, 3)} kilogams.')
    else:
        print('Please enter a valid unit.')
except:
    print("An error has occurred. Please try again.")