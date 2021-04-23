#!/usr/bin/env python3

import csv
import random
import time

def get_list_of_words(path):
    words = []
    with open(path, 'r') as word_file:
        reader = csv.reader(word_file)
        for w in reader:
            words.append(w)

    return words

def get_random_word(words):
    n = random.randint(0, len(words))
    return words[n]


if __name__ == '__main__':
    words = get_list_of_words('./sanalista.txt')
    for i in range(10):
        print(get_random_word(words))
        time.sleep(0.5)