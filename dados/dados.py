""" Cosas simples """
import random

dado1 = [1, 2, 3, 4, 5, 6]
dado2 = [1, 2, 3, 4, 5, 6]

def echar_dados():
    x = random.choice(dado1)
    y = random.choice(dado2) 
    return(x, y)

