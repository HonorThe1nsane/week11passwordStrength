# This will be my password program.
# I will prompt the user to enter a password and then check to see how many combinations there are.

password = input("Enter a password: ")


def passwordCombinations(password):
    passwordLength = len(password)
    passwordCombinations = 0
    passwordCombinations = 2**passwordLength
    return passwordCombinations


print(
    "There are",
    passwordCombinations(password),
    "combinations for the password",
    password,
)
