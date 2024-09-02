import random

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']

words = '''ant axolotl aardvark
        baboon badger bat bear beaver
        camel cat clam cobra cougar coyote crow
        deer dog donkey duck
        eagle elephant eel emu
        ferret fox frog falcon
        goat goose gecko giraffe
        hawk hippopotamus horse
        lion lizard llama
        mole monkey moose mouse mule
        newt narwhal nightingale
        otter owl ox ocelot opossum
        panda parrot pigeon python
        quail quahog
        rabbit ram rat raven rhino
        salmon seal shark sheep skunk sloth snake spider stork swan
        tiger toad trout turkey turtle
        urchin
        vulture viper
        weasel whale wolf wombat
        xerus
        yak yellowjacket yellowtail
        zebra zokor'''.split()

def random_word(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            if i < len(blanks):
                blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def get_guess(already_guessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        else:
            return guess

def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = random_word(words)
game_over = False

while True:
    found_all_letters = False 
    print('The secret word is in the dictionary. You have 6 guesses.')
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters and not game_over:
            print('Yes! The secret word is "' + secret_word + '"! You won!')
            game_over = True
    else:
        missed_letters = missed_letters + guess

        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter ' + str(len(missed_letters)) + ' missed guesses and ' + str(
                len(correct_letters)) + ' correct guesses, the word was "' + secret_word + '"')
            game_over = True

    if found_all_letters and not game_over:
        print('Yes! The secret word is "' + secret_word + '"! You won!')
        game_over = True

    if game_over:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_over = False
            secret_word = random_word(words)
        else:
            break
