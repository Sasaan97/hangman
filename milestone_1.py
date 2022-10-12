import random

word_list = ['watermelon', 'mango', 'pineapple', 'grape', 'blueberry']

word = random.choice(word_list)

guess = input('enter a single letter ')

if len(guess) == 1:
    if guess.isalpha():
        print('good guess!')
    else:
        print('Oops! That is not a valid input')
else:
    print('Oops! That is not a valid input')