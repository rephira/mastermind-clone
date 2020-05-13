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

    # FOR TESTING PURPOSES! DELETE THIS WHEN FINISHED!
    print(code)

    # Max guess
    ## Guess count set to 12 max. May want to add variable length in the future.
    max_guess = 12

    # Input loops for game
    for i in range(max_guess):
        
        check_len = False
        check_elem = False
        
        ## Print attempt number
        print(f"Attempt #{i+1}")

        while not check_len and not check_elem:
            ## Take input of 4 letters within code range, case insensitive
            guess = list(input("Make a guess."))
            check_len = len(guess) == 4
            check_elem = all(str.upper(i) in code_range for i in guess)
            
            ## Reject and ask for input again if above is not met.
            if not check_len and not check_elem:
                print("Wrong length and element(s). Guess must be 4 letters long, with all letters between A-F.")
            elif not check_len:
                print("Wrong length. Guess must be 4 letters long, with all letters between A-F.")
            elif not check_elem:
                print("Wrong element(s). Guess must be 4 letters long, with all letters between A-F.")
        
        ## Compare guess to code answer.
        checker = [0,0,0,0]
        for i,a in enumerate(guess):
            if str.upper(a) == code[i]:
                checker[i] += 2
            elif str.upper(a) in code:
                checker[i] += 1

        ## Print comparison result
        ### Raw print of checker for now. Need to replace with prettier output later.
        print(checker)
mm()