#Two Type Password Generator by Andy H 

#1. Password Generator for people that want either a long or short password.
#2. Should use a combination of letters list + symbols list + numbers list.
#3. Should have alternative option to do one based on your personality traits.
#4. The user should be able to get a range of options within set parameters.

import string
import random

#All alphabet, digits and symbols

all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

#PATHWAY ONE - STANDARD PASSWORD GENERATOR

def standard():
    s_short = [x for x in range(6, 10)]
    s_long = [x for x in range(14, 20)]
    #PROGRAM BEGIN
    in0 = input("Would you like a long or short password? ")
    in1 = input("Enter the amount of passwords you would like to generate: ")
    amount = int(in1)
    print("These are your",amount,"generated passwords:")

    if in0 == "short":
        for x in range(amount):
            length = (random.choice(s_short))
            password = "".join(random.sample(all, length))
            print (password)

    elif in0 == "long":
        for x in range(amount):
            length = (random.choice(s_long))
            password = "".join(random.sample(all, length))
            print (password)

    else:
        print ("Invalid request. Please, try again.")
        #Run program again from last stop. Add in while loop

#PATHWAY TWO - PERSONALITY PASSWORD GENERATOR

def personality():
    
    #Password Composition
    def short_pass():
        attribute = random.choice(personalitylist)
        length = p_short - len(attribute)
        rseq = "".join(random.sample(all, length))
        comb1= '{}{}'.format(attribute, rseq)
        comb2 = '{}{}'.format(rseq,attribute)
        pw_combos = [comb1, comb2]
        print(random.choice(pw_combos))

    def med_pass():
        attribute = random.sample(personalitylist,2)
        attribute_pick = '{}{}'.format(attribute[0].capitalize(), attribute[1].upper())
        length = p_medium - len(attribute_pick)
        rseq = "".join(random.sample(all,length))
        comb1 = '{}{}'.format(attribute_pick, rseq)
        comb2 = '{}{}'.format(rseq,attribute_pick)
        pw_combos = [comb1, comb2]
        print(random.choice(pw_combos))

    def long_pass():
        attribute = random.sample(personalitylist, 3)
        attribute_pick = '{}{}{}'.format(attribute[0].capitalize(), attribute[1].lower(), attribute[2].upper())
        length = p_long - len(attribute_pick)
        rseq = "".join(random.sample(all,length))
        password = '{}{}'.format(attribute_pick, rseq)
        print(password)

    #Password Lengths
    p_short = 15
    p_medium = 28
    p_long = 40

    #PROGRAM BEGIN
    pt_ui = input("What are three things that come to your mind when you think about yourself? Please space out your answers! ")
    pwlength_ui = input("Would you like a SHORT, MEDIUM or LONG password? ")
    pwamount_ui = input("How many password options would you like to be generated? ")

    personalitylist = pt_ui.split() #split function creates a list out of SPACED OUT string input
    amount = int(pwamount_ui)
    print("These are your",amount,"generated passwords:")

    if pwlength_ui.lower() == "short":
        for x in range (amount):
            short_pass()
    elif pwlength_ui.lower() == "medium":
        for x in range (amount):
            med_pass()
    elif pwlength_ui.lower() == "long":
        for x in range(amount):
            long_pass()
    else:
        print ("Invalid password length request. Please, try again. Remember to pick from the length options available!")

#User Input = Question Loop

def question(): 
    print("This is a Two Way Password Generator\nHow would you like to generate passwords?")

    while True: #USE WHILE LOOP TO REPEAT QUESTION UNTIL THE RIGHT INPUT IS USED.
        question = int(input("1. Randomly automated.\n2. Based on my personality traits.\n"))
        if question == 1:
            standard()
            break
        elif question == 2:
            personality()
            break
        else:
            print("Invalid input. Please, try again.")


#PROGRAM BEGIN

question()

again = (input("Thank you for using our generator! Would you like to generate more passwords? YES or NO?\n"))
if again.lower() == "yes":
    question()
else: 
    print("Thank you. See you again!")
    exit()