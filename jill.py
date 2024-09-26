import module
import argparse

def cracked(filename, filename2):
    file = open(filename, 'r') # opens file that contains users and hashed passwords
    users = module.users(file.readlines())

    file = open(filename, 'r') # opens file that contains users and hashed passwords
    passwords = module.passwords(file.readlines())

    file = open(filename2, 'r') # opens file that contains the wordlist
    words = module.words(file.readlines())

    file = open(filename2, 'r') # opens file that contains the wordlist
    hashed_words = module.hashed_words(file.readlines())

    counter2 = 0 
    counter = 0
    while counter < len(hashed_words):
        if hashed_words[counter] == (passwords[counter2]):
            print(f"{users[counter2]}:{words[counter]}")
            counter2 += 1
            counter = 1
        
        counter = counter + 1

def main():
    parser = argparse.ArgumentParser(description='Crack password from two files.')
    parser.add_argument('filename', help='The file to get users')
    parser.add_argument('filename2', help='The file to get passwords')
    args = parser.parse_args()
    
    password = cracked(args.filename, args.filename2)

if __name__ == '__main__':
    main()