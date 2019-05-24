import string

def generateKeyNumber(key):

    keyword = list(range(len(key)))
    initializer = 0

    for i in range(len(string.ascii_letters)):
        for j in range(len(key)):
            if key[j] in string.ascii_letters[i]:
                initializer += 1
                keyword[j] = initializer
    print(keyword)

if __name__ == '__main__':
    message = 'Message to be encrypted'
    key = 'MASBO'
    generateKeyNumber(key)




