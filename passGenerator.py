import passGen as pg

# file1 = open(r"password.txt", "a+")

# get_length = pg.pass_length()
# get_upper = pg.pass_upper()
# get_lower = pg.pass_lower()
# get_numbers = pg.pass_numbers()
# get_punct = pg.pass_punctuation()
# generate_pass = pg.get_pass(length=get_length, uppercase=get_upper, lowercase=get_lower, numbers=get_numbers, punctuation=get_punct) #Passing in the collected information from the previous variables to the function.

# file1.write(f"{generate_pass} \n")
# file1.close()
# print(generate_pass)



get_length = pg.pass_length()
get_upper = pg.pass_upper()
get_lower = pg.pass_lower()
get_numbers = pg.pass_numbers()
get_punct = pg.pass_punctuation()

for i in range(25): #generating a range of passwords.

    file2 = open(r"password2.txt", "a+")
    generate_pass = pg.get_pass(length=get_length, uppercase=get_upper, lowercase=get_lower, numbers=get_numbers, punctuation=get_punct)
    file2.write(f"{generate_pass} \n")
    if i == 0:
        file2.close()