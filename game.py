from random import randint


# Game function
## Build for 12 maximum guess by default
## Need to be able to take input

def mm():
    # Code generator
    code_range = ['A','B','C','D','E','F']
    code = []

    for i in range(4):
        code.append(code_range[randint(0,5)])

    # Max guess
    ## Guess count set to 12 max, with difficulty scale from 0-3 reducing guess count by 2 per unit increment.
    difficulty_set = False
    while not difficulty_set:
        d = input("Select difficulty (0-3 with 0 as easiest): ")
        try:
            if float(d) in [0,1,2,3]:
                difficulty_set = True
                max_guess = 12 - int(d)*2
                print (f"Difficulty {int(d)} chosen.")
                print (f"You will have {max_guess} attempts to crack the code.")
            else: 
                print ('Incorrect value given.')
        except:
            print('Incorrect value given.')

    # Input loops for game
    guess_tracker = []
    for i in range(max_guess):
        
        check_len = False
        check_elem = False
        
        ## Print attempt number
        print(f"Attempt #{i+1}")

        while not check_len or not check_elem:
            ## Take input of 4 letters within code range, case insensitive
            guess = list(input("Make a guess [type 'guess' to see your guesses so far]: "))
            check_len = len(guess) == 4
            check_elem = all(str.upper(i) in code_range for i in guess)
            
            ## Reject and ask for input again if above is not met.
            if str.lower(''.join(guess)) == "guess":
                print("Your guesses and results so far\n")
                for i in range(len(guess_tracker)):
                    r = guess_check(guess_tracker[i],code)[0]
                    print(f"{i+1}: {''.join(guess_tracker[i])}---{''.join(r)}")
            elif not check_len and not check_elem:
                    print("Wrong length and element(s). Guess must be 4 letters long, with all letters between A-F.")
            elif not check_len:
                print("Wrong length. Guess must be 4 letters long, with all letters between A-F.")
            elif not check_elem:
                print("Wrong element(s). Guess must be 4 letters long, with all letters between A-F.")
        
        ## Add current guess to guess_tracker
        guess_tracker.append(guess)

        comparison, checker = guess_check(guess,code)
        print(f"Result: {''.join(comparison)}")

        if checker == [2,2,2,2]:
            break
        else:
            pass
    
    # Output win/loss prompt
    if checker == [2,2,2,2]:
        print("Congratulations. You found the correct answer!")
    else:
        print(f"You lose! The correct answer was {''.join(code)}.")

    # Ask if player wants to play again.
    again = input("Play again? ['y' to play again.]: ")

    if str.lower(again) == 'y':
        mm()
    else:
        print("Thanks for playing!")

def guess_check(g,c):
    ## Compare guess to code answer.
    ch = [0,0,0,0]
    for i,a in enumerate(g):
        if str.upper(a) == c[i]:
            ch[i] += 2
        elif str.upper(a) in c: ##NEED TO FIX THIS PART. IT IS ATTACHING SINGLE OCCURRENCE TO MULTIPLE RESULT.
            ch[i] += 1

    ## Print comparison result, prettied. Probably should build a function for this?
    comp = []
    pegs = ["◌","○","●"] #apparently some full width symbols are not welcome on the terminal?
    comp = [pegs[i] for i in sorted(ch,reverse=True)]

    return [comp, ch]

mm()