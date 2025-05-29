import random
import string
import time
import os
import csv

def get_password_length():
    '''
    asks the user how many characters they want their new password to be
    Args:
        None
    Returns:
        None: the program checks if they entered an integer greater than 3
    '''
    while True:
        try:
            length = int(input("How many digits do you want your password to be? "))
            
            if length < 4:
                print("Password length must be greater than 3.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter an integer.")

def password_generator():
    '''
    generates a secure password with the number of digits the user requested
    Args:
        length (previous input)
    Returns:
        print: prints the password using random letters, numbers, and special characters
    '''
    length = get_password_length()
    characters = list(string.ascii_letters + string.digits + string.punctuation + "*")
    password = ''

    for i in range(length):
        password += random.choice(characters)
    print(f"Generated password: {password}")
    return password

def add_entry(websites, usernames, passwords):
    '''
    Allows the user to add websites/credentials to the code
    Args:
        websites (list): the blank list of websites that will be added to as the user enters credentials
        usernames (list): the blank list of usernames that will be added to as the user enters credentials
        passwords (list): the blank list of passwords that will be added to as the user enters credentials
    Returns:
        print: "Credentials added successfully!"
    '''
    website = input("Enter a website: ")
    username = input("Enter your username: ")
    password = input("Enter your password (Press 'g' to generate): ")

    if password.lower() == "g":
        password = password_generator()
    websites.append(website)
    usernames.append(username)
    passwords.append(password)
    print("Credentials added successfully!")

def access_credential(website, username, password):
    '''
    allows the user to view all of their stored credentials
    Args:
        website (input): uses the user's previously entered websites to display a list of all of the stored credentials
        username (input): uses the user's previously entered usernames to display a list of all of the stored credentials
        password (input): uses the user's previously entered passwords to display a list of all of the stored credentialsN
    Returns:
        list: the program prints all of the user's stored credentials in a list vertically
    '''
    print(f"Website: {website} | Username: {username} | Password: {password}")

def access_credentials(websites, usernames, passwords):
    '''
    DESCRIPTION
    Args:
        NAME (TYPE): DESCRIPTION
        NAME (TYPE): DESCRIPTION
        NAME (TYPE): DESCRIPTION
    Returns:
        TYPE: NAME/DESCRIPTION
    '''
    print("Your credentials: ")
    for index in range(len(websites)):
        access_credential(websites[index], usernames[index], passwords[index])
    print()

def get_index(websites, usernames, passwords):
    '''
    DESCRIPTION
    Args:
        NAME (TYPE): DESCRIPTION
        NAME (TYPE): DESCRIPTION
        NAME (TYPE): DESCRIPTION
    Returns:
        TYPE: NAME/DESCRIPTION
    '''
    while True:
        website = input("Which website's credentials would you like to access? (Enter 'r' to return to choices): ")

        if website in websites:
            index = websites.index(website)
            access_credential(websites[index], usernames[index], passwords[index])
            return index
        elif website.lower() == 'r':
            return -1
        else:
            print("Website not found.")

def change_credentials(websites, usernames, passwords):
    '''
    DESCRIPTION
    Args:
        NAME (TYPE): DESCRIPTION
        NAME (TYPE): DESCRIPTION
        NAME (TYPE): DESCRIPTION
    Returns:
        TYPE: NAME/DESCRIPTION
    '''
    index = get_index(websites, usernames, passwords)
    usernames[index] = input("Choose a new username: ")
    passwords[index] = input("Choose a new password: ")
    print("Credentials changed successfully!")

def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.

    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    '''
    #DOCUMENT ALL LINES IN THIS FUNCTION!
    if not arrays:
        raise ValueError("At least one array must be provided.")
    
    num_rows = len(arrays[0])
    for arr in arrays:
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        for i in range(num_rows):
            row = [arr[i] for arr in arrays]
            csvwriter.writerow(row)

def main():
    for i in range(3):
        password = input("Enter the Password Keeper code or exit: ")

        if password == '1234':
            break
        elif password == "exit":
            print("Exiting Program...")
            time.sleep(1)
            exit()
        else:
            print(f"Incorrect Password. You have {2-i} tries remaining")
    os.system('cls')

    websites = []
    usernames = []
    passwords = []

    while True:
        print('''Welcome to Password keeper, the menu is below: 
1. Add a website
2. Display all saved credentials
3. View credentials for a website
4. Modify stored credentials
5. Generate a secure password
6. Export entries to a csv
        ''')
        choice = input("Make your choice (Enter 'q' to quit): ").lower()
        
        if choice.lower() == "q":
            print("Exiting Program...")
            time.sleep(0.75)
            break
        elif choice == '1':
            add_entry(websites, usernames, passwords)
        elif choice == '2':
            access_credentials(websites, usernames, passwords)
        elif choice == '3':
            index = get_index(websites, usernames, passwords)

            if index != -1:
                access_credential(websites[index], usernames[index], passwords[index])
        elif choice == '4':
            index = get_index(websites, usernames, passwords)
            if index != -1:
                change_credentials(websites, usernames, passwords)
        elif choice == '5':
            print(f'Your generated password is {password_generator()}')
        elif choice == '6':
            filename = input('Enter filename: ')
            export_to_csv(filename+".csv", ["Website", "Useername", "Password"], websites, usernames, passwords)
            print(f'Successfully exported to {filename}.csv')
        else:
            print("Invalid Response")
main()