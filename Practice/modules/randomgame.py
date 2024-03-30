import random
from random import randint
#generate a number 1-10
#input from user


def run_guess_game(guess,answer):
    if 0 < int(guess) < 11:
        if int(guess) == answer:
            print('You are genious!')
            return True
        else:
            print('try again')
    else:
        print('hey stupid, I said 1-10.')
        return False
if __name__ == '__main__':

    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input('guess a number 1-10: '))
            if (run_guess_game(guess,answer)):
                break
        except ValueError:
            print('please enter a number')
            continue

