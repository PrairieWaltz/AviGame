from random import randint
from time import sleep
import colorama
from colorama import Fore, Style
from multiprocessing import Process
print(Fore.BLUE + Style.BRIGHT)

game_open = """
------------------------------------------------------------------------
------------------------------------------------------------------------
--------------------------/ \---\-----/---|-----------------------------
-------------------------/___\---\---/----|-----------------------------
------------------------/     \---\-/-----|-----------------------------
------------------------------------------------------------------------
--------------------Has a Game for YOU to Play!!------------------------
------------------------------------------------------------------------
"""
game_over = """
------------------------------------------------------------------------
--------------------GAME OVER YA WEIRDO...GO HOME!!---------------------
------------------------------------------------------------------------
"""

print(game_open)
print(Fore.CYAN)

question_list = 0
score = 0

while question_list < 10:

    play = input('Are you interested? Y/N: ').lower()
    if play == "y":
        print('Get ready for your first question!')
    else:
        print(f'Thanks anyway...Your final score was {score}/10')
        break
    sleep(1)

    print('')
    q1 = int(input('What year was I born? '))
    if q1 == 2013:
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)

    print('')
    q2 = input('What\'s my favorite color? ').lower()
    if q2 == 'cyan':
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)

    print('')
    q3 = int(input('How many toes does a Panda have? '))
    if q3 == 6:
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)

    print('')
    q4 = input('What is the longest word in English? ').lower()
    if q4 == 'pneumonoultramicroscopicsilicovolcanoconiosis':
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)

    print('')
    q5 = input('Does Avi hate Football? T/F: ').lower()
    if q5 == 't':
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)

    print('')
    q6 = input('Does cat urine glow in black-light? T/F ').lower()
    if q6 == 't':
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)

    print('')
    q7 = input('Do more people drown in Fresh or Salt water? ').lower()
    if q7 == 'fresh':
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)

    print('')
    q8 = int(input('What percentage of your body\'s oxygen does the brain use? '))
    if q8 == '20':
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)

    print('')
    q9 = int(input('What year did DiVinci finish his last major artwork?  '))
    if q9 == 1515:
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)

    print('')
    q10 = int(input('What percentage of your body weight is blood!!?? '))
    if q10 == 8:
        score += 1
        print(f'Correct! Your score is now {score}/10')
    else:
        print('Sorry thats wrong!')
    sleep(1)
    print(game_over)
    break


print(f"Your final score was {score}/10")
