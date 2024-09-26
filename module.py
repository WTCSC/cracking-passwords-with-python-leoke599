import hashlib

def passwords(text):
    password_list = [] # an empty list so that i can append the stuff from the loop
    for password in text:
        password = password.strip() # deletes whitespace from txt file
        sep = password.split(':') # seperates the users and passwords
        passwords = sep[1] # gets just the hashed password
        password_list.append(passwords) # puts the hashed password in the empty list
    return password_list # returns the list with the hashed passwords

def users(text):
    users_list = [] # empty list for appending
    for user in text:
        user = user.strip() # deletes whitespace from txt file
        sep = user.split(':') # seperates the users and passwords
        users = sep[0] # gets just the users
        users_list.append(users) # puts the users in the empty list
    return users_list # returns the list with users

def words(text):
    clean_words = [] # empty list for appending
    for word in text:
        clean_word = word.strip() # deletes whitespace from txt file
        clean_words.append(clean_word) # puts the words without whitespaces in the empty list
    return clean_words # returns the list of clean words with no whitespaces

def hashed_words(text):
    word_hash = [] # empty list for appending
    for word in text:
        clean_word = word.strip() # deletes whitespace from txst file
        sha256_hash = hashlib.sha256() # creates hash objects
        sha256_hash.update(clean_word.encode('utf-8')) # update hash objects with password bytes for each word
        hashed = sha256_hash.hexdigest() # makes hexidemical representation of hashes
        word_hash.append(hashed) # puts all the hashes into the empty list
    return word_hash # returns all the hashed words
