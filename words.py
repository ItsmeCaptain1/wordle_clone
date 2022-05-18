import random 

def load_word():

    FILENAME = "words.txt"
    inFile = open(FILENAME,'r')
    line = inFile.read()
    word_list = str.split(line)
    # print(len(word_list))
    return word_list

def target_word():
    word_list = load_word()
    secret_word = random.choice(word_list) 
    return secret_word
