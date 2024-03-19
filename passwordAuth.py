# This will be my password program.
# I will prompt the user to enter a password and then check to see how many combinations there are.

password = input("Enter a password: ")


def passwordCombinations(password):
    passwordCombinations = 0
    if any(char.isdigit() for char in password): #check for numerical characters
        passwordCombinations += 10
    if any(char.isupper() for char in password): #check for upper case characters
        passwordCombinations += 26
    if any(char.islower() for char in password): #check for lower case characters
        passwordCombinations += 26
    if any(                                      #check for special characters
        char
        in [
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            "-",
            "_",
            "+",
            "=",
            "?",
            "<",
            ">",
            ",",
            ".",
            ";",
            ":",
            "[",
            "]",
            "{",
            "}",
            "|",
            "\\",
            "/",
            "`",
            "~",
        ]
        for char in password
    ):
        passwordCombinations += 32

    passwordLength = len(password)

    passwordMaxCombos = passwordCombinations**passwordLength

    return passwordMaxCombos


print(
    "There are",
    passwordCombinations(password),
    "combinations for the password",
    password,
)
