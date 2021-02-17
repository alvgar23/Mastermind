# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 01:30:17 2020

@author: alvar
"""

"""
import some necessary functions
"""
from random import choice
from time import sleep
from IPython import get_ipython

"""
Define some global variables
"""
colors = ["red", "white", "grey", "green", "brown", "yellow",
          "black", "orange", "blue", "purple", "pink"]

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
        
    1. The COM chooses randomly 4 colors.
    2. The player must try to match the colors in order.
    3. If the player matches 1 color and its position, gets 1 DEAD.
    4. If the player matches 1 color but not its position, gets 1 HURT
    5. The player try to modify his colors to match them all.
    6. The player will have 15 attempts to match before the game over.
    """
    print(menu)
    
    answer = input("Do you want to see an example game? (y/n): ")
    
    if answer.lower() == "y":
        print("EXAMPLE:")
        sleep(2)
        print("COM chooses white, red, black and blue")
        sleep(2)
        print("Player chooses red, white, grey and green")
        sleep(2)
        print("0 DEAD, 2 HURT, 14 ATTEMPTS")
        sleep(2)
        print("Player chooses grey, green, brown and yellow")
        sleep(2)
        print("0 DEAD, 0 HURT, 13 ATTEMPTS")
        sleep(2)
        print("Player chooses white, red, black and orange")
        sleep(2)
        print("3 DEAD, 0 HURT, 12 ATTEMPTS")
        sleep(2)
        print("Player chooses white, red, black and blue")
        sleep(2)
        print("Those are the colors. PLAYER WINS!")
        sleep(2)
        
    get_ipython().magic("clear")    #clear console
    print("==> LET'S START THE GAME! <==")



def color_generator():
    
    """
    Randomly selects 4 different colors in one concrete order
    """
    
    com_color = []
    
    n1 = choice(colors)
    com_color.append(n1)
    
    n2 = choice(colors)
    com_color.append(n2)
    while n1 == n2:
        com_color.remove(n2)
        n2 = choice(colors)
        com_color.append(n2)
    
    n3 = choice(colors)
    com_color.append(n3)
    while n3 == n1 or n3 == n2:
        com_color.remove(n3)
        n3 = choice(colors)
        com_color.append(n3)
    
    n4 = choice(colors)
    com_color.append(n4)
    while n4 == n1 or n4 == n2 or n4 == n3:
        com_color.remove(n4)
        n4 = choice(colors)
        com_color.append(n4)
    
    return com_color



def user_color():
    
    """
    Allows the user to introduce 4 colors and try to guess the COM's
    """
    player_color = []
    
    print("\nPlease, choose 4 of these colors\n", colors)
    n1 = input("First color: ")
    while n1.lower() not in colors:
        print("Only one these colors. Do not repeat any.\n", colors)
        n1 = input("First color: ")
    
    n2 = input("Second color: ")
    while n1.lower() == n2.lower() or n2.lower() not in colors:
        print("Only one these colors. Do not repeat any.\n", colors)
        n2 = input("Second color: ")
    
    n3 = input("Third color: ")
    while (n3.lower() == n1.lower() or n3.lower() == n2.lower()
           or n3.lower() not in colors):
        print("Only one these colors. Do not repeat any.\n", colors)
        n3 = input("Third color: ")
    
    n4 = input("Fourth color: ")
    while (n4.lower() == n1.lower() or n4.lower() == n2.lower() 
           or n4.lower() == n3.lower() or n4.lower() not in colors):
        print("Only one these colors. Do not repeat any.\n", colors)
        n4 = input("Fourth color: ")
    
    player_color.append(n1.lower())
    player_color.append(n2.lower())
    player_color.append(n3.lower())
    player_color.append(n4.lower())
    
    return player_color



def compare(com_color, player_color):
    
    """
    Compares the COM's and the player's colors.
    Computes how many dead and how many hurt there are.
    """
    dead = 0
    hurt = 0
    for i in range(len(player_color)):
        if player_color[i] == com_color[i]:
            dead += 1
        elif player_color[i] in com_color:
            hurt += 1
    print("\n==> PLAYER HAS", dead, "DEAD AND", hurt, "HURT <==")
    print("------------------------------------------------------")
    return dead, hurt #returns a tuple (dead,hurt)



def game(dead, hurt):
    
    """
    Plays the game, taking into account the attempts
    """
    
    menu()
    com_color = color_generator()
    attempts = 15
    attempts_bg = attempts #we use this aux to don't change the original value
    
    while attempts > 0:
        
        player_color = user_color()
        
        get_ipython().magic("clear")    #clear console
        print("------------------------------------------------------")
        print("\n==> Player's color are: ", player_color, "<==")
        (dead, hurt) = compare(com_color, player_color)
        
        background(attempts, dead, hurt, player_color, attempts_bg)
        
        if (dead, hurt) == (4,0):
            print("\nPLAYER WINS!")
            print("The colors were", com_color)
            break
        else:
            attempts -= 1
            print("==> PLAYER HAS", attempts, "MORE ATTEMPTS <==")
            print("------------------------------------------------------")
    
    if attempts == 0:
        print("\nGAME OVER! COM WINS.")
        print("The COM's colors were", com_color)
        
    
    return attempts, attempts_bg



def background(attempts, dead, hurt, player_color, attempts_bg):
    
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
    attempt.append(player_color)
    attempt.append(dead)
    attempt.append(hurt)
    background_list.append(attempt) #we save all the rounds here
    
    print()
    for i in range(len(background_list)):
        print(background_list[i][0], "-",background_list[i][1], 
              background_list[i][2], "DEAD", background_list[i][3], "HURT" )
    print()
    return background_list



game(dead, hurt)
