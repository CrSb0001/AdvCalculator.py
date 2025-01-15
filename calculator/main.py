START_UP_INPUTS=set('12345')

def calc_setup():
    while True:
        choice=input(f'\nInput:')
        val=set(f'{choice}')
        if val.issubset(START_UP_INPUTS)==True:
            return True
        else:
            print('That isn\'t an allowed value. Try again please.')
            continue

print('Hi there! What type of math would you like to do with this calculator?')
print('')
print('+-+--------------+')
print('|1|Basic Math    |')
print('+-+--------------+')
print('|2|Basic Algebra |')
print('+-+--------------+')
print('|3|Trigonometry  |')
print('+-+--------------+')
print('|4|Linear Algebra|')
print('+-+--------------+')
print('|5|Calculus      |')
print('+-+--------------+')
calc_setup()
