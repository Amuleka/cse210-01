import random

# Create list of words
words = ['Mexico', 'USA', 'Brazil', 'Argentina', 'France', 'Italy', 'Germany', 'Sweden']

# Randomly choose one of the listed words
word = random.choice(words)

# Create spaces to hide the word
spaces = ['_']* len(word)

# Create a function
# 1- Find all of the letter positions from the users guess
# 2- If the letter exists will replace the underscore with the correct letter
def get_letter_position(guess, word, spaces):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            removed_character = '*'
            word = word[:index] + removed_character + word[index+1:]
            spaces[index]= guess
        else: index = -1
    return (word, spaces)

# Create a function to check if the user guesses all of the letters (1=Yes, -1=No)

def win_check():
    for i in range(0,len(spaces)):
        if spaces[i] == '_':
            return -1
        
    return 1

# Chosse some number of turns for the user to guess the word
num_turns = len(word)
for i in range(0, num_turns):
    guess = input('Guess a character: [a-z] ')

    if guess in word:
        word, spaces = get_letter_position(guess, word, spaces)
        print(spaces)
    else:
        print('Sorry, that letter is not in the word! ')

    if win_check() == 1:
        print(' Congratulations, You won!')
        break
    print('You have ' + str(num_turns - i) + 'turns left.')

