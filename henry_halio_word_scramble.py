import random                                                                                                                                       #allows the code to choose a random item from a list
name = input("What is your name? ")                                                                                                                 #asks the user for their name
print("Good luck, ", name)
games = 0                                                                                                                                           #sets the number of games to 0
wins = 0                                                                                                                                            #sets the number of wins to 0
words = ["Ravens", "Giants", "Chiefs", "Bills"]                                                                                                     #creates the list of words

while True:                                                                                                                                         #forever loop
    word = random.choice(words)                                                                                                                     #defines the variable 'word' as a random choice from the list
    display = list(word)                                                                                                                            #names display as the name of the list of words
    random.shuffle(display)                                                                                                                         #scrambles one of the words from the list and displays it
    display = "".join(display)                                                                                  
    turns = 5                                                                                                                                       #sets the number of turns to 5

    while turns > 0:                                                                                                                                #while the user still has at least 1 turn left
        guess = input(f"Unscramble {display}. Enter real word here: ")                                                                              #displays the scrambled word from the list and tells the user to guess the real word

        if guess == word:                                                                                                                           #if the user's guess matches the real word
            print ("Correct!")                                                                                                                      #displays 'correct!'
            wins += 1                                                                                                                               #adds one to the user's score
            break                                                                                                                                   #breaks the forever loop
        
        turns -= 1                                                                                                                                  #subtracts one from the number of turns the user has left

        while True:                                                                                                                                 #forever loop
            scramble = input(f"You did not guess the word you have {turns} attempts left. Would you like to rescramble the words? y/n: ")           #tells the user that they did not guess the word, how many turns they have left, and if they would like to rescramble the word
            
            if scramble == "n":                                                                                                                     #if they do not want to rescramble it, it displays the same thing again
                break                                                                                                                               #ends the forever loop
            elif scramble == "y":                                                                                                                   #if the user wants to rescramble the word
                display = list(word)                                                                                                                #displays the new scrambled word
                random.shuffle(display)
                display = "".join(display)
                break                                                                                                                               #ends the forever loop
            else:
                print("Invalid Response")                                                                                                           #if the user inputted anything other than yes or no, it displays "invalid response"
    print (f"The word was {word}")                                                                                                                  #if the user runs out of turns it tells them the word
    games += 1                                                                                                                                      #adds one to the number of games played

    while True:                                                                                                                                     #forever loop
        play_again = input(f"{name}, you scored {wins} wins out of {games} games. Would you like to play again? y/n: ")                             #gives the user the option to play again after telling them their score out of how many games played
        if play_again == "n":                                                                                                                       #if they do not want to play again
            print("Goodbye")                                                                                                                        #displays 'goodbye!'
            exit()                                                                                                                                  #ends the code  
        elif play_again == "y":                                                                                                                     #if the user wants to play again
            break                                                                                                                                   #ends the forever loop and brings them back to the start
        else:                                       
            print("Invalid Response. Enter yes or no")                                                                                              #if the user inputs anything other than yes or no, it tells them that they have to answer yes or no