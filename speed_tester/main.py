#!/usr/bin/env python3

import time
import random
import os

letters = ['h', 'j', 'k', 'l']
running = True

def random_letter():
    i = random.randint(0, 3)
    return letters[i]

def update_time(x):
    if x > 0.35:
        return x - 0.05 * x
    else:
        return 0.35

def cli_print():
    os.system('clear')
    i = letters.index(random_letter())
    for l in letters:
        if l == letters[i]:
            print(l.upper(), end='\t')
        else:
            print(l, end='\t')
    print()

if __name__ == "__main__":
    t = 1.3
    while running:
        cli_print()
        if t < 0.4:
            break
        time.sleep(t)
        t = update_time(t)
