#password_part_2


import string
import random

#All alphabet, digits and symbols
all = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

#Preset password lengths
p_short = 15
p_medium = 28
p_long = 40

def personalityroute():
    #PROGRAM BEGIN
    pt_ui = input("What are three things that come to your mind when you think about yourself? Please space out your answers! ")
    pwlength_ui = input("Would you like a SHORT, MEDIUM or LONG password? ")
    pwamount_ui = input("How many password options would you like to be generated? ")

    personalitylist = pt_ui.split() #split function creates a list out of SPACED OUT string input
    amount = int(pwamount_ui)

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
