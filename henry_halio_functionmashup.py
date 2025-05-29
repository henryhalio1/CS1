import random
def chorus ():
    '''
    Prints the chorus of a song
    Args:
        none
    Returns:
        print(chorus)
    '''
    print("Sing us a song, you're the piano man")
    print("Sing us a song tonight")
    print("Well, we're all in the mood for a melody")
    print("And you've got us feelin' alright")
    print("")
def song():
    '''
    Prints a verse of the song
    Args:
        None
    '''
    print("It's 9 o'clock on a Saturday, and the regular crowd shuffles in,")
    print("there's an old man, sitting next to me, making love to his tonic and gin.")
    print("")
    chorus()
    print("Now John at the bar is a friend of mine, He gets me my drinks for free")
    print("And he's quick with a joke or to light up your smoke, But there's some place that he'd rather be")
    print("He says, 'Bill, I believe this is killing me', As the smile ran away from his face")
    print("Well, I'm sure that I could be a movie star, If I could get out of this place")
    print("")
    chorus()
def add(a, b):
    '''
    def add(a, b):
        adds two numbers together
    Args:
        a, b (variables): numbers
    Returns:
        output type: sum of two numbers
    '''
    print(f"The sum is {a+b}")
def print_list(array):
    '''
    def printlist(array
        takes every item in a list and prints them in order vertically
    Args:
        array(list)
    Returns:
        output type: items in a list displayed vertically
    '''
    for item in array:
        print(item) #prints each item in the list vertically
def inlist(array, variable):
    '''
    def inlist(array, variable)
        checks if a variable is in a list
    Args:
        array, variable(list and items in the list)
    Returns:
        output type: True or False
    '''
    return variable in array  #if the variable is in the list, it returns true or false
def is_integer(value):
    '''
    def is_integer(value)
        checks if an input is an integer
    Args:
        value(number)
    Returns:
        output type: True or False
    '''
    try:
        int(value) #checks to see whether or not the number is an integer
        return True
    except ValueError: #if it is not, it prints false
        return False
def get_random():
    '''
    def get_random()
        takes two numbers and prints a random number
    Args:
        number1, number2 (user inputs)
    Returns:
        output type: random number
    '''
    number1, number2 = get_integers()
    print(random.randint(number1, number2)) #prints a random number regardless of the numbers entered
def count_vowels(string):
    '''
    def count_values(string)
        counts the number of vowels in a given phrase
    Args:
        string: phrase
    Returns:
        output type: number of vowels in the phrase
    '''
    vowels = 0 #starts the number of vowels at 0
    for letter in string:
        if letter in ['a', 'e', 'i', 'o', 'u']: #defines the list of vowels
            vowels += 1 #for each vowel, the program adds 1 to the number of vowels
    return f"The number of vowels in 'Hello World' is: {vowels}"
def reverse_string(s):
    '''
    def reverse_string()
        Takes a string and returns it reversed
    Args:
        s (the string I programmed)
    Returns:
        the string is printed but it is reversed
    '''
    return s[::-1] #allows a string to be reversed
def reverse_string(s):
    return s[::-1]
def is_palindrome(s): #checks if a word is a palindrome
    '''
    def is_palindrome()
        Takes a string and checks whether it is a palindrome
    Args:
        none
    Returns:
        the computer checks whether the input is a palindrome and tells the user
    '''
    return s == reverse_string(s) #uses the reverse string function to check whether the input is a palindrome
def get_integers():
    '''
    def get_integers()
        Takes two integers from the user and adds them
    Args:
        number1, number2(inputs entered by the user)
    Returns:
        output type: sum of the numbers that the user entered
    '''
    while True:
        number1 = input("Enter an integer: ")
        number2 = input("Enter another integer: ")

        if is_integer(number1) and is_integer(number2):
            return int(number1), int(number2)
        else:
            print("Invalid input. Please enter integers.")
def main():
    '''
    def main():
        houses all of the functions under it and then runs them
    Args:
        all previous functions
    Returns:
        output type: all functions are run
    '''
    while True: #forever loop
        print("Choose a function, your function choices are: 1. Singsong, 2. Add, 3. Printlist, 4. Inlist, 5. Getrandom, 6. CountVowels, 7. Reverse String, 8. Palindrome Checker, 9. Get Initials, 10. Letter Changer, and 11. Name Generator")
        functionchoice = input("Select an option (1-11), enter 12 to exit: ")
        if functionchoice == "1":
            song()
        elif functionchoice == "2":
            add(2, 3)
        elif functionchoice == "3":
            print_list([1, 2, 3])
        elif functionchoice == "4":
            print(inlist([1, 2, 3], 'a'))
        elif functionchoice == "5":
            get_random()
        elif functionchoice == "6":
            print(count_vowels('Hello World'))
        elif functionchoice == "7":
            userstring = input("Enter a word or phrase, and the computer will print it backwards: ")
            print("Reversed string:", reverse_string(userstring))
        elif functionchoice == "8":
            print("An example of a palindrome is 'radar'. A palindrome reads the same forwards and backwards.")
            user_input = input("Enter a word to check if it is a palindrome: ")
            if is_palindrome(user_input):
                print(f'"{user_input}" is a palindrome!')
            else:
                print(f'"{user_input}" is not a palindrome.')
        elif functionchoice == "9":
            def get_initials(name):
                words = name.split()
                initials = ''.join(word[0].upper() for word in words)
                return initials
            full_name = input("Enter a full name: ")
            initials = get_initials(full_name)
            print(f"The initials of '{full_name}' are: {initials}")
        elif functionchoice == "10":
            def replace_character(s, old_word, new_word):
                result = ''
                for word in s:
                    if word == old_word:
                        result += new_word
                    else:
                        result += word
                return result
            original_string = input("Enter a string: ").lower()
            old_word = input("Enter the character you want to replace: ").lower()
            new_word = input("Enter the new character: ").lower()
            updated_string = replace_character(original_string, old_word, new_word)
            print(f"The updated string is: {updated_string}")
        elif functionchoice == "11": 
            def generate_name():
                first_names = ["Alex", "Jamie", "Taylor", "David", "Henry", "Patrick", "William", "Matthew"]
                last_names = ["Smith", "Johnson", "Williams", "White", "Clark", "Jefferson", "Kelly", "Jones"]
                return random.choice(first_names) + " " + random.choice(last_names)
            print(generate_name())
        elif functionchoice == "12":
           break
        else:
            print("Invalid Choice, Please try again")
main()