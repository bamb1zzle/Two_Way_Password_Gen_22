Two Way Password Generator Breakdown:

___________________________________________________

Project timeline:

    Date Started: 18th September
    Date Completed: 20th September
    Estimated completion time = 12 hours.

__________________________________________________

Modules/Concepts worked with: 

    random module:
        random.choice(x): returns random element from a sequence
        random.sample(x,y): returns random sample of a sequence. x = sequence, y = length of output

    string module:
        - ASCII string: string.ascii_lowercase + string.ascii_uppercase
        - DIGIT string: string.digits
        - SYMBOLS string: string.punctuation
        - Ljust string method: aligns string according to width specified with blank space if 'fillchr' argument is not passed.
                                string.ljust(x, '!') 
                                a = astro
                                print(a.ljust(10,'!'))
                                output = astro!!!!!

    if, for, while loops:
        - Repeating loop until desired output.
            while True:
            input(x)
                if input(x) == 1:
                #execute program + break from loop
                program()
                break

    formatting:
        - "".join
            joins objects in list or array
        -'{}{}'.format(x,y)
            curly brackets creates placeholders for your variables

___________________________________________________

Reflection/What I've learned:

    Initial thoughts-
This started off as just a small initial project because I wanted to do something simple to get my mind jogging. I enjoyed the process of making my base model but wanted to improve it. I aimed to do this by:

    - Adding multiple options for passwords and multiple lengths in these options using range: short, medium, long
    - Using an attribute that relates to the user to make the password more easily memorable.

    Mid Project-

    - PART 1 - STANDARD GENERATOR: The problem for this was trying to get a different password length for EACH of the passwords generated within the users preferred range. I was able to achieve this though by using the .choice(x) of the random module.

    - PART 2 - PERSONALITY GENERATOR: This was my biggest hurdle of the whole process. To achieve my original scope of what I wanted for my project I had to work with so many variables at once and it was discouraging to see an error after everytime I tried to find a solution. Day 2 was full of errors and not one success. But the biggest thing I've gained from this experience was to BREAK DOWN your goal into small tiny goals. Once I broke down each variable and worked with them one by one instead of all at once it became a lot easier to understand what was working and what wasn't instead of being consistently overwhelmed by the errors. I didn't achieve my original goal for the password generator as I wasn't sure how I was going to make multiple password combinations work but I'm proud that I was able to shift the goalpost, achieve a good fraction of what I originally wanted and didn't give up. 

    End of Project-
It's incredibly easy to be overwhelmed by what you don't know and be hard on yourself for consistently running into errors but there's no point being harsh in yourself. Enjoying the process and building a habit towards learning and progress is my everyday goal and I believe I'm putting in the work towards that.
