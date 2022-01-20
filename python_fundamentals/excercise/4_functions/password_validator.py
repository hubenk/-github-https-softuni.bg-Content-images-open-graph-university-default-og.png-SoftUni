def length(password_check1):
    if len(password_check1) < 6 or len(password_check1) > 10:
        print("Password must be between 6 and 10 characters")


def symbols(password_check2, a, b):
    if len(password_check2) != a + b:
        print("Password must consist only of letters and digits")


def digits(password_check3):
    if password_check3 < 2:   #password_check3.isalnum() проверява дали стригна е само от букви и цифри
        print("Password must have at least 2 digits")


def valid_pass(password, a, b):
    if 5 < len(password) < 11 and len(password) == a + b and b >= 2:
        print("Password is valid")


password = input()

num_count = 0
chr_count = 0
for symbol in password:
    if symbol.isdigit():
        chr_count += 1
    if symbol.isalpha():
        num_count += 1

# result = lenght, symbols, digits
# if all(result):   =   #if all(result) == True:

length(password)
symbols(password, num_count, chr_count)
digits(chr_count)
valid_pass(password, num_count, chr_count)
