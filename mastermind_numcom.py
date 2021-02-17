# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:24:11 2020

@author: alvar
"""

"""
Mastermind. User gives a 4 digit number and COM try to guess it.
It usually guess the number before 200 attempts.
(User usually do it in less than 10, so still not comparable)
"""

"""
import some necessary functions
"""
from random import randint, choice, shuffle
from time import sleep



"""
Define some global variables
"""
dead = 0
hurt = 0

background = [] #we will need it later in background()
background_list = [] # we will need it in background()


def user_number():
    
    """
    Allows the user to introduce a number that COM will try to guess
    """
    
    while True:
        
        try:
    
            print("\nPlease, introduce 4 digits: ")
            n1 = input("First digit: ")
            while int(n1) < 0 or int(n1) > 9:
                print("Only one digit between 0 and 9 that cannot be repeated.")
                n1 = input("First digit: ")
        
        except ValueError: #if it's not a digit
                print("You must introduce a number.")
                
        else:
            break #ends loop
    
    while True:
        
        try:
    
            n2 = input("Second digit: ")
            while n1 == n2 or int(n2) < 0 or int(n2) > 9:
                print("Only one digit between 0 and 9 that cannot be repeated.")
                n2 = input("Second digit: ")
                
        except ValueError: #if it's not a digit
                print("You must introduce a number.")
        
        else:
            break #ends loop
    
    while True:
        
        try:
    
            n3 = input("Third digit: ")
            while n3 == n1 or n3 == n2 or int(n3) < 0 or int(n3) > 9:
                print("Only one digit between 0 and 9 that cannot be repeated.")
                n3 = input("Third digit: ")
                
        except ValueError: #if it's not a digit
                print("You must introduce a number.")
        
        else:
            break #ends loop
            
    while True:
        
        try:   
    
            n4 = input("Fourth digit: ")
            while n4 == n1 or n4 == n2 or n4 == n3 or int(n4) < 0 or int(n4) > 9:
                print("Only one digit between 0 and 9 that cannot be repeated.")
                n4 = input("Fourth digit: ")
                
        except ValueError: #if it's not a digit
                print("You must introduce a number.")
        
        else:
            break #ends loop
    
    player_number = n1 + n2 + n3 + n4
    return player_number



def number_generator():
    
    """
    Randomly generates a 4 different digits number (type string) and try to 
    guess the user's number
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



def compare(com_number, player_number):
    
    """
    Compares the COM's and the player's numbers.
    Computes how many dead and how many hurt there are.
    """
    dead = 0
    hurt = 0
    for i in range(len(com_number)):
        if com_number[i] == player_number[i]:
            dead += 1
        elif com_number[i] in player_number:
            hurt += 1
    print("\n==> COM HAS", dead, "DEAD AND", hurt, "HURT <==")
    print("------------------------------------------------------")
    return dead, hurt #returns a tuple (dead,hurt)



def decision(dead, hurt, com_number):
    """
    COM has to take different decisions depending on how many dead and hurt it
    has.
    """
    
    if dead == 0 and hurt == 0:
        #do it normally
        com_number = number_generator()
    
    elif dead == 0 and hurt == 1:
        #keep one and shuffle
        n1 = choice(com_number)
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
        
        list_com_number = list(com_number)
        shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
    
    elif dead == 0 and hurt == 2:
        #keep 2 and shuffle
        n1 = choice(com_number)
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)
        
        n3 = str(randint(0,9))
        while n3 == n1 or n3 == n2:
            n3 = str(randint(0,9))
        
        n4 = str(randint(0,9))
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = str(randint(0,9))
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i    
    
    elif dead == 0 and hurt == 3:
        #keep 3 and shuffle
        n1 = choice(com_number)
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)
        
        n3 = choice(com_number)
        while n3 == n1 or n3 == n2:
            n3 = choice(com_number)
        
        n4 = str(randint(0,9))
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = str(randint(0,9))
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i    
    
    elif dead == 0 and hurt == 4:
        #keep 4 and shuffle
        n1 = choice(com_number)
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)
        
        n3 = choice(com_number)
        while n3 == n1 or n3 == n2:
            n3 = choice(com_number)
        
        n4 = choice(com_number)
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = choice(com_number)
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i 
    
    elif dead == 1 and hurt == 0:
        #keep one in the same position
        n1 = choice(com_number)
        ind = com_number.index(n1)
        
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
        
        list_com_number = list(com_number)
        #shuffle until dead is in the same position
        while list_com_number[ind] != n1: 
            shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
    
    elif dead == 1 and hurt == 1:
        #keep one in the same position
        n1 = choice(com_number)
        print(n1)
        ind = com_number.index(n1)
        
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)  # keep another and shuffle
        
        n3 = str(randint(0,9))
        while n3 == n1 or n3 == n2:
            n3 = str(randint(0,9))
        
        n4 = str(randint(0,9))
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = str(randint(0,9))
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        #shuffle until dead is in the same position
        while list_com_number[ind] != n1: 
            shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
    
    elif dead == 1 and hurt == 2:
        #keep one in the same position
        n1 = choice(com_number)
        ind = com_number.index(n1)
        
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)  # keep another 2 and shuffle
        
        n3 = choice(com_number)
        while n3 == n1 or n3 == n2:
            n3 = choice(com_number)
        
        n4 = str(randint(0,9))
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = str(randint(0,9))
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        #shuffle until dead is in the same position
        while list_com_number[ind] != n1: 
            shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
    
    elif dead == 1 and hurt == 3:
        #keep one in the same position
        n1 = choice(com_number)
        ind = com_number.index(n1)
        
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)  # keep the other and shuffle
        
        n3 = choice(com_number)
        while n3 == n1 or n3 == n2:
            n3 = choice(com_number)
        
        n4 = choice(com_number)
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = choice(com_number)
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        #shuffle until dead is in the same position
        while list_com_number[ind] != n1: 
            shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
    
    elif dead == 2 and hurt == 0:
        #keep two in the same position
        n1 = choice(com_number)
        ind = com_number.index(n1)
        
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)
        ind2 = com_number.index(n2)
        
        n3 = str(randint(0,9))
        while n3 == n1 or n3 == n2:
            n3 = str(randint(0,9))
        
        n4 = str(randint(0,9))
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = str(randint(0,9))
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        #shuffle until dead is in the same position
        while list_com_number[ind] != n1 or list_com_number[ind2] != n2: 
            shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
    
    elif dead == 2 and hurt == 1:
        #keep two in the same position
        n1 = choice(com_number)
        ind = com_number.index(n1)
        
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)
        ind2 = com_number.index(n2)
        
        n3 = choice(com_number)
        while n3 == n1 or n3 == n2:
            n3 = choice(com_number)
        
        n4 = str(randint(0,9))
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = str(randint(0,9))
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        #shuffle until dead is in the same position
        while list_com_number[ind] != n1 or list_com_number[ind2] != n2: 
            shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
            
    elif dead == 2 and hurt == 2:
        #keep two in the same position
        n1 = choice(com_number)
        ind = com_number.index(n1)
        
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)
        ind2 = com_number.index(n2)
        
        n3 = choice(com_number)
        while n3 == n1 or n3 == n2:
            n3 = choice(com_number)
        
        n4 = choice(com_number)
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = choice(com_number)
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        #shuffle until dead is in the same position
        while list_com_number[ind] != n1 or list_com_number[ind2] != n2: 
            shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
    
    elif dead == 3 and hurt == 0:
        #keep three in the same position
        n1 = choice(com_number)
        ind = com_number.index(n1)
        
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)
        ind2 = com_number.index(n2)
        
        n3 = choice(com_number)
        while n3 == n1 or n3 == n2:
            n3 = choice(com_number)
        ind3 = com_number.index(n3)
        
        n4 = str(randint(0,9))
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = str(randint(0,9))
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        #shuffle until dead is in the same position
        while (list_com_number[ind] != n1 or list_com_number[ind2] != n2
               or list_com_number[ind3] != n3): 
            shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
    
    elif dead == 3 and hurt == 1:
        #keep three in the same position
        n1 = choice(com_number)
        ind = com_number.index(n1)
        
        n2 = choice(com_number)
        while n1 == n2:
            n2 = choice(com_number)
        ind2 = com_number.index(n2)
        
        n3 = choice(com_number)
        while n3 == n1 or n3 == n2:
            n3 = choice(com_number)
        ind3 = com_number.index(n3)
        
        n4 = choice(com_number)
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = choice(com_number)
        com_number = n1 + n2 + n3 + n4
        
        list_com_number = list(com_number)
        #shuffle until dead is in the same position
        while (list_com_number[ind] != n1 or list_com_number[ind2] != n2
               or list_com_number[ind3] != n3): 
            shuffle(list_com_number)
        com_number = ""
        
        for i in list_com_number:
            com_number = com_number + i
    
    return com_number



def game(dead, hurt):
    
    """
    Plays the game, taking into account the attempts
    """
    
    # menu()
    player_number = user_number()
    attempts = 200
    attempts_bg = attempts #we use this aux to don't change the original value
    com_number = number_generator() # First round, 0 dead, 0 hurt
    
    while attempts > 0:
        com_number = decision(dead, hurt, com_number)
        print("------------------------------------------------------")
        print("\n==> COM's number is: ", com_number, "<==")
        (dead, hurt) = compare(com_number, player_number)
        
        background(attempts, dead, hurt, com_number, attempts_bg)
        
        if (dead, hurt) == (4,0):
            print("\nCOM WINS!")
            print("The number was", com_number)
            break
        else:
            attempts -= 1
            print("==> COM HAS", attempts, "MORE ATTEMPTS <==")
            print("------------------------------------------------------")
            sleep(0)
            
    if attempts == 0:
        print("\nGAME OVER! PLAYER WINS.")
        print("The player's number was", player_number)

    return attempts, attempts_bg



def background(attempts, dead, hurt, com_number, attempts_bg):
    
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
    attempt.append(com_number)
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