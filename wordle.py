from words import target_word
from words import load_word

def is_word_guessed(SECRET_WORD, GUESSED_WORD):
    return SECRET_WORD == GUESSED_WORD

def is_valid_word( word ):
    if len(word) != 5 :
        print("Please Input a Valid Word !!!")
        return False
    word_list = load_word()
    if word in word_list:
        return True 
    else: 
        print("Please Input a Valid Word !!!")
        return False

def display_result_of_guessed_word(SECRET_WORD, GUESSED_WORD):
    res = ['_','_','_','_','_']
    # index => 0 2 4 6 8
    allPos = [0,1,2,3,4]
    for i in range(5):
        if SECRET_WORD[i] == GUESSED_WORD[i] :
            res[i] = '@'
            allPos.remove(i)
    for i in range(5):
        for j in allPos:
            if SECRET_WORD[j] == GUESSED_WORD[i]:
                res[i] = '#'
                allPos.remove(j)
                break

    for i in range(5):
        print(res[i],end=' ')
    print("\n\n")



def wordle_clone(SECRET_WORD):
    CHANCE = 0
    max_trial = 6
    res = True 
    while(CHANCE < max_trial ):
        CHANCE += 1
        while True:
            GUESSED_WORD = input("PLEASE GUESS A WORD : ")
            print()
            GUESSED_WORD = GUESSED_WORD.lower()
            if GUESSED_WORD == "quit":
                return False
            if is_valid_word(GUESSED_WORD):
                break 
       
        if is_word_guessed(SECRET_WORD, GUESSED_WORD):
            print(" * * Congratulations, you guessed the right word !!! * * ", end='\n\n')
            res = False 
            break
        else: 
            display_result_of_guessed_word(SECRET_WORD,GUESSED_WORD)
    
    if res : 
        print("You Lose The Game.")
    print()
    ip = input("Want to Start Game Again ? (yes/no) ")
    ip = ip.lower()
    if ip == "yes":
        return True
    else : 
        return False 


def  startGame():
    print("""
        WELCOME TO WORDLE_CLONE.
        You have total 6 Chances to find a 5 lenght secret word. 
        You can guess a word with exactly 5 lenght no less no more then that.

        AFTER guessing there will be one of the 3 conditions applied on every letter, following are:
        A @ character means a letter was guessed correctly
        in the correct position.
        A # character means a letter was guessed correctly,
        but in the incorrect position,
        A _ character means a letter was guessed incorrectly.

        IF YOU CANNOT ABLE TO GUESS WORD IN 5 CHANCES YOU WILL LOSE. 
        ELSE YOU CONSIDERED AS A WINNER OF WORDLE_CLONE.

        To quit, type "quit".
    """)

    while True:
        print()
        print("Let's Begin the Game !!!", end="\n\n")
        SECRET_WORD = target_word()
        print(" target word = " + SECRET_WORD )
        play = wordle_clone(SECRET_WORD)
        if not play: 
            print()
            print("Thanks for playing, Hope you come back soon.", end="\n\n")
            break

startGame()

