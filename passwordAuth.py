# This will be my password program.
# I will prompt the user to enter a password and then check to see how many combinations there are.
import math

while True: # This will loop until a password is entered
    password = input("Enter a password: ")


    def passwordCombinations(password):
        special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?", "/", " "]
        passwordCombinations = 0
        if any(char.isdigit() for char in password): #check for numerical characters
            passwordCombinations += 10
        if any(char.isupper() for char in password): #check for upper case characters
            passwordCombinations += 26
        if any(char.islower() for char in password): #check for lower case characters
            passwordCombinations += 26
        if any(char in special_characters for char in password): #check for special characters
            passwordCombinations += 33

        passwordLength = len(password)

        passwordMaxCombos = passwordCombinations**passwordLength

        return passwordMaxCombos



    def findBits(passwordMaxCombos):
        bits = 0
        while passwordMaxCombos > 1:
            passwordMaxCombos = passwordMaxCombos // 2
            bits += 1
        return bits



    print(
        "There are",
        passwordCombinations(password),
        "combinations for the password",
        password,
    )
    print()

    print("That is equivalent to", findBits(passwordCombinations(password)), "bits")
    print()
    print("Would you like to try again? (y/n)")
    tryAgain = input()
    if tryAgain == "n":
        break
    else:
        continue
