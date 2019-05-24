import string

def encryptMessage(message, key):
    keyNumber = generateKeyNumber(key)
    extraLetters = len(message) % len(key)
    dummy_characters = len(key) - extraLetters

    if extraLetters != 0:
        for i in range(dummy_characters):
            message += "q"

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




