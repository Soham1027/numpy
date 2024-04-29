import random
guess = ''
while guess not in ('0', '1'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = (input())
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == int(guess):
    print(toss)
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    
    if toss == int(guess):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')