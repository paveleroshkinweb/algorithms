import random

def get_rand(number=10, randomRange=50):
    array = []
    for i in range(1, number):
        randomNumber = random.randint(1, randomRange)
        array.append(randomNumber)
    return array

