import random                                                                                   #creates ability to pick a random item in a list                                                          
import time                                                                                     #creates ability for code to pause when i write time
answers = ["Yes", "No", "Maybe", "Ask Again Later", "Definitely", "Probably", "Unlikely"]       #random list of answers to questions
times = ["Today", "Never", "Yesterday", "In a Year", "Soon", "Unclear"]                         #random list of answers to questions starting with when


while True:                                                                                     #forever loop
    question = input("Welcome to the Magic 8 Ball. Ask a question. (type 'exit' to quit)")      #prompts user to ask a question and allows them to type exit to quit
    
    if  question.lower ()== 'exit':                                                             #checks if the user answered 'exit'
        print ("Goodbye!")                                                                      #writes goodbye if above is true
        break                                                                                   #breaks the forever loop
    first_word = question.split()[0]                                                            #checks what the first word in the users question is
    if first_word == 'when':                                                                    #checks if the first word of the question is 'when'
        print ("Thinking...")                                                                   #writes "thinking..."
        time.sleep(0.75)                                                                        #pauses the code for 0.75 seconds
        print("Answer: ", random.choice(times))                                                 #prints "answer" and then chooses an answer from the list titled "times"
    else:
        print ("Thinking...")                                                                   #if the first word is not 'when', the code will write "Thinking..."
        time.sleep(0.75)                                                                        #pauses the code for 0.75 seconds
        print("Answer: ", random.choice(answers))                                               #prints "answer" and then chooses an answer from the list titles "answers"

    


