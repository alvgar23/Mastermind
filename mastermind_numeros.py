# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:29:48 2020

@author: alvar
"""

"""
import some necessary functions
"""
from random import randint
from time import sleep
from IPython import get_ipython



"""
Define some global variables
"""
dead = 0
hurt = 0

background = [] #we will need it later in background()
background_list = [] # we will need it in background()



def menu():
    
    """
    Shows how to play and gives the choice of seeing an example
    """
    
    menu = """
    MASTERMIND
    
    How to play:
        
    1. The COM chooses a random 4-digit number.
    2. The player must try to match the number.
    3. If the player matches 1 digit and its position, gets 1 DEAD.
    4. If the player matches 1 digit but not its position, gets 1 HURT
    5. The player try to modify his digits to match the number.
    6. The player will have 10 attempts to match before the game over.
    """
    print(menu)
    
    answer = input("Do you want to see an example game? (y/n): ")
    
    if answer.lower() == "y":
        print("EXAMPLE:")
        sleep(2)
        print("COM chooses 2179")
        sleep(2)
        print("Player chooses 1234")
        sleep(2)
        print("0 DEAD, 2 HURT, 14 ATTEMPTS")
        sleep(2)
        print("Player chooses 3456")
        sleep(2)
        print("0 DEAD, 0 HURT, 13 ATTEMPTS")
        sleep(2)
        print("Player chooses 2178")
        sleep(2)
        print("3 DEAD, 0 HURT, 12 ATTEMPTS")
        sleep(2)
        print("Player chooses 2179")
        sleep(2)
        print("That's the number. PLAYER WINS!")
        sleep(2)

    get_ipython().magic("clear")    #clear console
    print("==> LET'S START THE GAME! <==")    
    


def number_generator():
    
    """
    Randomly generates a 4 different digits number (type string)
    """
    
    n1 = str(randint(0,9))
    n2 = str(randint(0,9))
    while n1 == n2:
        n2 = str(randint(0,9))
    
    n3 = str(randint(0,9))
    while n3 == n1 or n3 == n2:
        n3 = str(randint(0,9))
    
    n4 = str(randint(0,9))
    while n4 == n1 or n4 == n2 or n4 == n3:
        n4 = str(randint(0,9))
    
    com_number = n1 + n2 + n3 + n4
    return com_number



def user_number():
    
    """
    Allows the user to introduce a number and try to guess the COM's
    """
    
    print("\nPlease, introduce 4 digits: ")
    
    while True:
    
        try:
        
            n1 = input("First digit: ")
            while int(n1) < 0 or int(n1) > 9:
                print("Only one digit between 0 and 9 that cannot be repeated.")
                n1 = input("First digit: ")
                
        except ValueError: #if it's not a digit
                print("You must introduce a number.")
                
        else:
            break  #ends loop
    
    while True:
    
        try:
        
            n2 = input("Second digit: ")
            while n1 == n2 or int(n2) < 0 or int(n2) > 9:
                print("Only one digit between 0 and 9 that cannot be repeated.")
                n2 = input("Second digit: ")
                
        except ValueError: #if it's not a digit
            print("You must introduce a number.")
        
        else:
            break  #☺ends loop
    
    while True:
    
        try:
    
            n3 = input("Third digit: ")
            while n3 == n1 or n3 == n2 or int(n3) < 0 or int(n3) > 9:
                print("Only one digit between 0 and 9 that cannot be repeated.")
                n3 = input("Third digit: ")
                
        except ValueError: #if it's not a digit
            print("You must introduce a number.")
        
        else:
            break  #☺ends loop
    
    while True:
    
        try:
    
            n4 = input("Fourth digit: ")
            while n4 == n1 or n4 == n2 or n4 == n3 or int(n4) < 0 or int(n4) > 9:
                print("Only one digit between 0 and 9 that cannot be repeated.")
                n4 = input("Fourth digit: ")
    
        except ValueError: #if it's not a digit
            print("You must introduce a number.")
        
        else:
            break  #☺ends loop
    
    player_number = n1 + n2 + n3 + n4
    return player_number



def compare(com_number, player_number):
    
    """
    Compares the COM's and the player's numbers.
    Computes how many dead and how many hurt there are.
    """
    dead = 0
    hurt = 0
    for i in range(len(player_number)):
        if player_number[i] == com_number[i]:
            dead += 1
        elif player_number[i] in com_number:
            hurt += 1
    print("\n==> PLAYER HAS", dead, "DEAD AND", hurt, "HURT <==")
    print("------------------------------------------------------")
    return dead, hurt #returns a tuple (dead,hurt)



def game(dead, hurt):
    
    """
    Plays the game, taking into account the attempts
    """
    
    menu()
    com_number = number_generator()
    attempts = 20
    attempts_bg = attempts #we use this aux to don't change the original value
    
    while attempts > 0:
        
        player_number = user_number()
        print("------------------------------------------------------")
        print("\n==> Player's number is: ", player_number, "<==")
        (dead, hurt) = compare(com_number, player_number)
        
        background(attempts, dead, hurt, player_number, attempts_bg)
        
        if (dead, hurt) == (4,0):
            print("\nPLAYER WINS!")
            print("The number was", com_number)
            break
        else:
            attempts -= 1
            print("==> PLAYER HAS", attempts, "MORE ATTEMPTS <==")
            print("------------------------------------------------------")
    
    if attempts == 0:
        print("\nGAME OVER! COM WINS.")
        print("The COM's number was", com_number)

    return attempts, attempts_bg



def background(attempts, dead, hurt, player_number, attempts_bg):
    
    """
    Returns all the data of each attempt, recalling the number, dead and hurt.
    """
    
    attempt = [] # we will save every round here
    attempt_change = [] 
    
    #we change attempt 15 for attempt_bg 1, attempt 14 for attempt_bg 2...
    for i in range(attempts_bg, 0, -1):
         attempt_change.append(i)
    
    for i in range(len(attempt_change)):
        if attempts == attempt_change[i]:
            attempts_bg = attempt_change[-1-i]
    
    attempt.append(attempts_bg)  #we save each round here
    attempt.append(player_number)
    attempt.append(dead)
    attempt.append(hurt)
    background_list.append(attempt) #we save all the rounds here
    
    print()
    for i in range(len(background_list)):
        print(background_list[i][0], "-",background_list[i][1], "-",
              background_list[i][2], "DEAD", background_list[i][3], "HURT" )
    print()
    return background_list



game(dead, hurt)