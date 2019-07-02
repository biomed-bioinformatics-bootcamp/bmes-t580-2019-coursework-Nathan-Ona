# imports the random module that allows for the generation of random values
import random
# Creates divider for program
print('---------------------------')
print('   GUESS THE PRIMER!       ')
print('---------------------------')
print()
# Generates random DNA sequence
DNA_goal = random.choice('ACGT')
DNA_goal += random.choice('ACGT')
DNA_goal += random.choice('ACGT')
DNA_goal += random.choice('ACGT')
DNA_goal += random.choice('ACGT')
X = 2
# asks user for their name and welcomes the use
user_name = input('What is your name?')
print('Hello ' + user_name)
# temporary value to enter the while loop for the game to start
user_guess = 'QWERT'
# checks if the guess value is less than the chosen random number
while user_guess != DNA_goal:
    # asks use for their guess at the random 5 base pair primer
    user_guess = input('please enter a 5 base pair primer ')
    # checks if the user guess is equal to the random base primer, otherwise outputs that the user guess
    # was correct
    misses = 0
    for i in range(len(user_guess)):
        if user_guess[i] != DNA_goal[i]:
            misses += 1
    if misses > 0:
        print('Sorry, your guessed %i bases wrong. Play Again?' % misses)
    else:
        print('Good job' + user_name + ', your guessed the Primer!')