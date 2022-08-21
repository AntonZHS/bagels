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


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Вы угадали!'

    clues = []
    for i in range(len(guess)):
        if guess == secretNum:
            clues.append('Горячо')
        elif guess[i] in secretNum:
            clues.append('Тепло')
    if len(clues) == 0:
        return 'Холодно'

    clues.sort()
    return ''.join(clues)
