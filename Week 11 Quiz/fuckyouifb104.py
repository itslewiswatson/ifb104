vowels = ['a', 'e', 'i', 'o', 'u'];

counter = 4

def check_buttons():
    if counter > 0:
        print('PREV ACTIVE')
    elif counter < len(vowels) - 1:
        print('PREV DISABLED')
    if counter < len(vowels) - 1:
        print('NEXT ACTIVE')
    else:
        print('NEXT DISABLED')

check_buttons()