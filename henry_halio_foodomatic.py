#FLOWER BOX
# Henry Halio, 4/7/2025
# This Python code provides an interactive experience with three mini-games: a food menu generator, 
# a Clue style game, and a madlibs-style story generator. Users can choose which experience they would like to do and are prompted for various inputs, 
# such as the number of food items or the elements needed for a madlib story. The program incorporates random choices to select items from predisposed 
# lists and ensures input validation to improve user experience. The code implements for loops which choose items from a list using indexes, white 
# repeating itself for an amount of time selected by the user. Finally, users have the option to play again or exit the program.
#CHALLENGES:
#Different Domain (Clue-style game)
#Generate and add in the costs for flairs as well
#Calculate the total cost for all items.
#Ensure that the user is entering a valid number when asking for menu items.
#Remove the possibility of duplicate items.
#Apply parallel arrays and/or for loops to something different (Madlibs)
#SOURCES: Data Quest, Stack Overflow, Youtube

import random #allows code to pick a random item from a list

foods = ["Cauliflower", "Tilapia Fillet", "Pork Loin", "Salmon", "Potatoes", "Three Color Squash", "Eggplant", "Steak", "Baguette"] #list of foods
prices = [20, 25, 28, 30, 18, 20, 22, 30, 20]   #list of prices
flairs = ["with balsamico", "with garlic and olive oil", "with minted yogurt", "with chutney", "salad", "with salsa", "over stickey rice", "au jus", "with basmati rice"]    #list of sides/flair
people = ["Ms. Peackock", "Professor Plum", "Colonel Mustard", "Ms. Scarlett", "Mr. Boddy", "Mr. Green", "Mrs. White"] #list of people
rooms = ["The Library", "The Hall", "The Lounge", "The Dining Room", "The Kitchen", "The Ballroom", "The Conservatory", "The Billiards Room", "The Study"] #list of rooms
weapons = ["Rope", "Wrench", "Candlestick", "Lead Pipe", "Revolver", "Dagger", "Knife"] #list of weapons

while True: #forever loop
    listchoice = input("Would you like to see the food options, play madlibs, or play clue? f/m/c: ") #asks the user what part of my code they want to play

    if listchoice == "c": #if the user chpose to play clue
        while True:
            try: #ensures that the user enters a number (along with the lines below)
                cluenumber = int(input("How many accusations would you like to file? ")) #asks how many accusations the user wants to file
                
                if cluenumber > 7:
                    print("Too many, maximum accusations is 7")
                    continue
                break   #breaks the forever loop
            except ValueError: #if the user does not enter a number
                print("Not valid. Enter a number") #repromps the user to enter a number

        for i in range(cluenumber): #the next few lines show the program picking a random person, the weapon that goes along with them, and a random room
            person = random.choice(people)
            index = people.index(person)

            print(person, "with a", weapons[index], "in the", random.choice(rooms))
            
    elif listchoice == "f": #if the user want to view the program
        while True: #forever loop
            try:
                number = int(input("How many menu items would you like? ")) #asks the user how many menu items they want
                if number < 1:
                    print("Invalid. Enter a number between 1 and 9: ")
                break #breaks the forever loop
            except ValueError: 
                print("Not valid. Enter a number") #if the user does not enter a number it tells them and reasks the question
        total = 0 #sets the total to 0 so it can start counting from there

        for i in range(number): #the next few lines show the program picking a random food, the price that goes along with it, a random flair, and the total price of their order
            food = random.choice(foods)
            flair = random.choice(flairs)

            price = prices[foods.index(food)]
            print(f'{food} {flair}, ${price} + $1')
            total += price + 1 #the total (0) is added to the price and is displayed below
        print("Your total is: $", total)

    elif listchoice == "m":
        adjective1 = input ("Enter an adjective: ")
        noun1 = input ("Enter a noun: ")
        noun2 = input ("Enter another noun: ")
        adjective2 = input ("Enter another adjective: ")
        celebrity = input ("Enter a celebrity: ")
        food = input ("Enter any food item: ")
        pluralnoun = input ("Enter a plural noun: ")
        pasttenseverb = input ("Enter a past tense verb: ")
        adjective3 = input ("Enter an adjective: ")
        noun3 = input ("Enter a noun: ")
        adjective4 = input ("Enter an adjective: ")
        print(f"It was a {adjective1} day when I saw a {noun1} just relaxing on my {noun2}. It looked way too {adjective2} to be normal. Then {celebrity} showed up with some {food} like it was no big deal. Outta nowhere, a bunch of {pluralnoun} {pasttenseverb} across the backyard. Everything felt super {adjective3}, and then the {noun3} started glowing all {adjective4} and weird.")

    else:
        print("Invalid Response. Enter 'f' for food options, 'm' for madlibs, or 'c' for clue") #if the user does not choose f m or c the program asks the question again
    
    while True: #forever loop
        playagain = input("Do you want to play again? y/n: ") #asks the user if they want to play again
        
        if playagain == "y": #if the user wants to play again it asks them which game they want to play
            break #breaks forever loop
        elif playagain == "n": #if they don't want to play again
            exit() #ends the code
        else:
            print("Invalid Response. Enter y or n.") #if the user does not enter y or n it asks the question again