import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretsNum = ''
    for i in range(NUM_DIGITS):
        secretsNum += str(numbers[i])
    return secretsNum   
     
