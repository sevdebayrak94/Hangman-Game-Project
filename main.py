import random
from hangman_words import word_list
from hangman_art import stages


chosen_word = random.choice(word_list)
print(chosen_word)

################################ Codes ########################

import random
#To Do 1: Randomly choose a word from a list and assign it to a variable called chosen_word. And print it
word_list = ['camel', 'wather', 'baloon', 'aardwark', 'value', 'translation', 'scientist']
chosen_word = random.choice(word_list)
length_chosen_word = len(chosen_word)
lives = 6

position = " "
for i in range(length_chosen_word):
    position += "_ "
print(position)

# To Do : Ask the user to guess the letter
game = False
correct_letters = []
while not game:
    guess = input("Guess a Letter: ").lower()
    display = ""
    for i in chosen_word:
        if i == guess:
            display += i
            correct_letters.append(guess)
        elif i in correct_letters:
            display += i
        else:
            display += "_ "

    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game = True
            print("You Lost!")

    if "_" not in display:
        game = True
        print("You win")

    print(stages[6 - lives])