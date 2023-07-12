# Math Quiz

# July 10th, 2023

# CTI-110 P5HW - Math Quiz

# Marcelina Lopez

#

import random

def AdditionProblem():
    a = random.randint(0,99)
    b = random.randint(0,99)
    print(f' {a}')
    print(f'+{b}')
    print('Enter answer.')
    answer = int(input())
    while answer!=(a+b):
        if answer<(a+b):print('Sorry, guess is too low.')
        else: print('Sorry, guess is too high.')
        answer = int(input('try again:'))
    print('Congratulations!!!! Your answer is correct.\n')

def SubtractionProblem():
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    if a<b:a,b=b,a
    print(f' {a}')
    print(f'-{b}')
    print('Enter answer.')
    answer = int(input())
    while answer != (a - b):
        if answer < (a - b):
            print('Sorry, guess is too low.')
        else:
            print('Sorry, guess is too high.')
        answer = int(input('try again:'))
    print('Congratulations!!!! Your answer is correct.\n')

def main():
    print('Welcome to Math Quiz\n')
    while True:
        print('MAIN MENU')
        print('--------------------')
        print('1. Adding Random Numbers')
        print('2. Subtracting Random Numbers')
        print('3. Exit\n')
        choice = input('Please choose one of the menu options: ')
        if choice == '1':
            AdditionProblem()
        elif choice == '2':
            SubtractionProblem()
        elif choice == '3':
            print('Thank you for playing...\nBye!!')
            break

main()

