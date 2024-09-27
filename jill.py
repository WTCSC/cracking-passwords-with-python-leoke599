import module
import argparse

def cracked(filename, filename2): # first filename is where the users and hashed passwords are. filename2 is the wordlist
    file = open(filename, 'r') # opens file that contains users and hashed passwords
    users = module.users(file.readlines()) # finds user using my module. using readlines is neccessary because it has to be a list in order to execute the function

    file = open(filename, 'r') # opens file that contains users and hashed passwords
    passwords = module.passwords(file.readlines())  # finds hashed passwords using my module. using readlines is neccessary because it has to be a list in order to execute the function

    file = open(filename2, 'r') # opens file that contains the wordlist
    words = module.words(file.readlines())  # finds words in the wordlist using my module. using readlines is neccessary because it has to be a list in order to execute the function

    file = open(filename2, 'r') # opens file that contains the wordlist
    hashed_words = module.hashed_words(file.readlines())  # hashes words in wordlist using my module. using readlines is neccessary because it has to be a list in order to execute the function

    counter2 = 0 # counter used to check each user
    counter = 0 # counter used to iterate through each word
    while counter < len(hashed_words): # while loop to iterate over each word making sure not to go over the amount of words in the wordlist or it would cause an error
        if hashed_words[counter] == (passwords[counter2]): # checks if the hashed word = the hased password
            print(f"{users[counter2]}:{words[counter]}") # prints the user and corresponding password if found
            counter2 += 1 # this is used to move onto the next user if a user's password is already found
            counter = 0 # this is used to read the wordlist from the start again
        
        counter = counter + 1 # this is used to iterate over to another word if there is no match

def main():
    parser = argparse.ArgumentParser(description='Crack password from two files.') # creates argument parser object
    parser.add_argument('filename', help='The file to get users') # adds argument to the script for users and hashed passwords
    parser.add_argument('filename2', help='The file to get passwords') # adds argument to the script for the wordlist file
    args = parser.parse_args() # allows to parse arguments from the command line
    
    cracked(args.filename, args.filename2) # used to replace filename and filename2 with actual files

if __name__ == '__main__': # ensure that the main() is only called when the script is run directly
    main() 