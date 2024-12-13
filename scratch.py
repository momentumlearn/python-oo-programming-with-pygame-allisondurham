






import random
from random import randrange


def generate_color():
    r = random.randrange(255)
    g = random.randrange(225)
    b = random.randrange(225)
    return (r, g, b)

def color_list():
    color_bank = []
    for i in range(5):
        color_bank.append(generate_color())
    print(color_bank)
    return color_bank

def color_choice():
    print(random.choice(color_list()))
    return random.choice(color_list())

color_list()
color_choice()