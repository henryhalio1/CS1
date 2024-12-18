#cat
import random                                                                                                                   #allows the code to pick a random item from the list                                                               
import os                                                                                                                       #allows the code to make the first player's choice dissapear
import time                                                                                                                     #allows the code to pause for the set amount of time
rps_diagrams = ["""                                                                                             
    _______
---'   ____)
      (_____)                                                                                          
      (_____)
      (____)
---.__(___)
""","""                                                                                            
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""","""                                                                                         
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]                                                                                                                            #above, are my three ASCII art drawings for rock, paper, and scissors
answers = ["rock", "paper", "scissors"]                                                                                         #the list of possible answers for the rock paper scissors game
numbers = ["1","2","3","4","5","6","7","8","9","10"]                                                                            #list of possible answers for the number game
pc = ["p", "c"]
rn = ["r", "n"]

while True:
        gamechoice = input("Do you want to play Rock Paper Scissors or a Number game; r/n: ").lower()           #asks which game the user wants to play    

        if gamechoice == "r":                                                                                   #if the user chooses rock paper scissors                         
                playerone_score = 0                                                                             #sets player one's score to zero      
                playertwo_score = 0                                                                             #sets player two's score to zero                                                                                
                playerorcomputer = input("Do you want to play rock paper scissors against the computer or another person; p/c:")        #asks if the user wants to play against the computer or another person

                if playerorcomputer not in pc:
                        print("Invalid Response")
                        playerorcomputer = input("Do you want to play rock paper scissors against the computer or another person; p/c:")
                
                while playerone_score < 5 and playertwo_score < 5:                                              #while both players' scores are less than five
                        while True:                                                                             #forever loop
                                player1_choice = input("Player 1, enter rock, paper, scissors, or black hole (only if one player game): ").lower()     #prompts the user to pick rock paper scissors or black hole   
                                time.sleep(0.25)                                                                #pauses the program for 0.25 seconds
                                if player1_choice not in answers:                                               #if the user chooses something that is not in the answers
                                        print("invalid")                                                        #prints invalid if the user chooses something that is not in the answer list
                                else:
                                        break                                                                                #hides player one's choice from player twowhile True:                                                                     #forever loop
                        if playerorcomputer == "p":
                                os.system("cls")
                                while True:
                                        player2_choice = input("Player 2, enter a choice; rock, paper, scissors: ").lower()    #prompts player two to enter a choice
                                        if player2_choice not in answers:                                       #if player two's choice is not in the answer list
                                                print("invalid")                                                #prints invalid
                                        else:
                                                break                                                           #breaks forever loop
                        elif playerorcomputer == "c":
                                player2_choice = random.choice(answers)                                         #computer selects a random weapon
                        print(f'''Player 1 chose                                                                
                                {rps_diagrams[answers.index(player1_choice)]}                                                   
                                                                                                                                
                                        and player 2 chose 
                                {rps_diagrams[answers.index(player2_choice)]}
                                ''')

                        if playerorcomputer == "c":                                                             #if the user chooses computer
                                print("You are player one, the computer is player two. Good luck.")             #tells the user that they are player one and the computer is player two
                        if player1_choice == "black hole" and playerorcomputer == "c":                          #if the user is playing against the computer and chooses black hole
                                print("AUTOMATIC WIN!")                                                         #code prints automatic win!
                        elif player1_choice == player2_choice:                                                  #if player one and player two enter the same choice (rock, paper, or scissors)
                                print("Tie; Try Again")                                                         #prints tie, try again
                        elif player1_choice == "rock" and player2_choice == "scissors":                         #depending on what each players input was, the code will display who won, and add one to their score, before displaying each players score. this is the same until line #91                  
                                print("Player One Wins")
                                playerone_score +=1
                        elif player1_choice == "rock" and player2_choice == "paper":
                                print("Player Two Wins")
                                playertwo_score +=1
                        elif player1_choice == "paper" and player2_choice == "rock":
                                print("Player One Wins")
                                playerone_score +=1
                        elif player1_choice == "paper" and player2_choice == "scissors":
                                print("Player Two Wins")
                                playertwo_score +=1
                        elif player1_choice == "scissors" and player2_choice == "paper":
                                print("Player One Wins")
                                playerone_score +=1
                                time.sleep(0.25)
                        elif player1_choice == "scissors" and player2_choice == "rock":
                                print("Player Two Wins")
                                playertwo_score +=1
                        print("Player 1 score is: ", playerone_score)
                        print("Player 2 score is: ", playertwo_score)


                if playerone_score == 5:                                                                       #if player one reaches a score of five
                        print("Game Over, Player One Wins!")                                                   #prints player one wins
                elif playertwo_score == 5:                                                                     #if player two reaches a score of five
                        print("Game Over, Player Two Wins!")                                                   #prints player two wins
        elif gamechoice == "n":                                                                                #if user chose to play the number game
                computernumber = random.choice(numbers)
                while True:                                                                                    #forever loop                                                #the computer will select a random number (1-10) from the list
                        print("The computer has a number, try to guess it")
                        time.sleep(0.1)
                        guess = input("Enter a number; 1-10: ")                                                #prompts the user to enter a number 1-10
                        if guess == computernumber:                                                            #if the user enters the number the computer selected
                                print("You Win!")                                                              #indicates that the user wins
                                playagain = input("Do you want to play again; y/n: ").lower()                  #asks the user whether or not they want to play again
                                if playagain == "y":                                                           #if the user wants to play again
                                        gamechoice = input("Do you want to play Rock Paper Scissors or a Number game; r/n:").lower()            #asks the user if they want to play RPS or the number game
                                elif playagain == "n":                                                         #if the user does not want to play again
                                        print("Goodbye!")                                                      #prints goodbye
                                        break
                        else:                                                                                  #if the user does not guess the nuber
                                print("Nope! Try again")                                                       #prints nope, try again
                                time.sleep(0.25)                                                               #pauses the code for 0.25 seconds
        if gamechoice not in rn:
                print("Invalid Response")
                gamechoice = input("Do you want to play Rock Paper Scissors or a Number game; r/n: ").lower()

        