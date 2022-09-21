# Password Generator by Andy H 20220606


def main():

    import random

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = ":;<>,.?-=+!@#$%^&*"

    upper, lower, nums, syms = True, True, True, True 

    all=""
    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums: 
        all += digits
    if syms:
        all += symbols

    in1= str(input("This is a Password Generator.\nWould you like a long or short password? "))
    length=""

    if (in1 == 'long'):
        length = 20
    elif (in1 == 'short'):
        length = 10

    in2 =str(input("How many possible passwords would you like generated? "))
    amount= int(in2)

    print("These are your",amount,"generated passwords:")
    for x in range(amount):
        password = "".join(random.sample(all, length))  #sample means you cant resuse symbols
        print(password)


main()

again = str(input("Would you like to use the password generator again? Yes/No " ))
if again.lower() == "yes":
    main()
else:
    exit()

#Super proud that I used the in range properly for this password code. 