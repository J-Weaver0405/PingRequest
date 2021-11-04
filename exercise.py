import random
import string


# uchars = uppercase
# lchars =  lowercase 
# dchars = digits
# schars = punctuation or special 

def get_random_string(uchars = 2, lchars = 6, dchars = 1, schars = 1):
    # Generates a 10 characters long random string
    # with 3 upper case, 3 lowe case, 2 digits and 2 special characters

    str_uchars, str_lchars, str_dchars, str_schars = '', '', '', ''

    for i in range(uchars):
        str_uchars += random.SystemRandom().choice(string.ascii_uppercase)

    for i in range(lchars):
        str_uchars += random.SystemRandom().choice(string.ascii_lowercase)

    for i in range(dchars):
        str_uchars += random.SystemRandom().choice(string.digits)

    for i in range(schars):
        str_uchars += random.SystemRandom().choice(string.punctuation)

    random_str = str_uchars + str_lchars + str_dchars + str_schars
    random_str = ''.join(random.sample(random_str, len(random_str)))
    return random_str


print('Your Random String-1:', get_random_string())



def format_number(num):
    if type(num) != int:
        return 'you must enter a number'
    elif num < 0:
        return 'needs to be greater 0'
    elif len(str(num)) < 3:
        return num
    num = str(num)
    count = 0
    for i in range(len(num)-1,0,-1):
        count += 1
        if count % 3 == 0:
            num = num[:i] + ',' + num[i:]
    
    return num


