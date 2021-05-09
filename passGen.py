import random
import string


def get_pass(length=12, uppercase=True, lowercase=True, numbers=True, punctuation=True):
    char_set = ''
    if uppercase:
        char_set += string.ascii_uppercase
    if lowercase:
        char_set += string.ascii_lowercase
    if numbers:
        char_set += string.digits
    if punctuation:
        char_set += string.punctuation
        
    return ''.join(random.choice(char_set) for i in range(length))


def pass_length():
    while True:
        try:
            length = input("How man characters long would you like the password to be?: ").lower()
            if length.isdigit() == False:
                raise Exception("Please enter a number")
                
            if length.isdigit():
                    length = int(length)
                    return length
            else:
                length = False
                return length

        except Exception as err:
            print(err)
            continue

def pass_lower():
    while True:
        try:
            lower = input("Would you like to use lowercase letter? Y/N: ").lower()
            if lower == 'y':
                lower = True
                return lower
            elif lower == 'n':
                lower = False
                return lower
            else:
                raise Exception("Please enter 'y' or 'n'..")
        except Exception as err2:
            print(err2)
            continue

def pass_upper():
    while True:
        try:
            upper = input("Would you like to use UPPERCASE letter? Y/N: ").lower()
            if upper == 'y':
                upper = True
                return upper
            elif upper == 'n':
                upper = False
                return upper
            else:
                raise Exception("Please enter 'y' or 'n'..")
        except Exception as err3:
            print(err3)
            continue


def pass_numbers():
    while True:
        try:
            numbers = input("Would you like to use numbers? Y/N: ").lower()
            if numbers == 'y':
                numbers = True
                return numbers
            elif numbers == 'n':
                numbers = False
                return numbers
            else:
                raise Exception("Please enter 'y' or 'n'..")
        except Exception as err4:
            print(err4)
            continue


def pass_punctuation():
    while True:
        try:
            punct = input("Would you like to use punctuation? Y/N: ").lower()
            if punct == 'y':
                punct = True
                return punct
            elif punct == 'n':
                punct = False
                return punct
            else:
                raise Exception("Please enter 'y' or 'n'..")
        except Exception as err5:
            print(err5)
            continue


def main():
    get_length = pass_length()
    get_upper = pass_upper()
    get_lower = pass_lower()
    get_numbers = pass_numbers()
    get_punct = pass_punctuation()
    get_password = get_pass(length=get_length, uppercase=get_upper, lowercase=get_lower, numbers=get_numbers, punctuation=get_punct)
    print(get_password)

if __name__ == "__main__":
    main()