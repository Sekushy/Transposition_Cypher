import string

def encryptMessage(message, key):
    keyNumber = generateKeyNumber(key)
    extraLetters = len(message) % len(key)
    dummy_characters = len(key) - extraLetters

    if extraLetters != 0:
        for i in range(dummy_characters):
            message += "q"

    numberOfRows = int(len(message) / len(key))
    matrix = [[0] * len(key) for i in range(numberOfRows)]

    # z is just an index
    z = 0
    for i in range(numberOfRows):
        for j in range(len(key)):
            matrix[i][j] = message[z]
            z += 1

    for i in range(numberOfRows):
        for j in range(len(key)):
            print(matrix[i][j], end= ' ')
        print()

    numberLocation = getLocationOfNumbersInKey(keyNumber, key)
    print(numberLocation)

    encryptedMessage = ''
    k = 0
    for i in range(numberOfRows):
        if k == len(key):
            break
        else:
            temp = int(numberLocation[k])
        for j in range(numberOfRows):
            encryptedMessage += matrix[j][temp]
        k += 1
    print('Encrypted message: {}'.format(encryptedMessage))

def getLocationOfNumbersInKey(keyNumber, key):
    numberLocation = ''
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if keyNumber[j] == i:
                numberLocation += str(j)
    return numberLocation


def generateKeyNumber(key):
    keyword = list(range(len(key)))
    tempPositionerForCharInKey = 0

    for i in range(len(string.ascii_letters)):
        for j in range(len(key)):
            if key[j] in string.ascii_letters[i]:
                tempPositionerForCharInKey += 1
                keyword[j] = tempPositionerForCharInKey
    return keyword

if __name__ == '__main__':
    message = 'Message to be encrypt'
    key = 'MASBO'

    encryptMessage(message, key)




