#!/usr/bin/env python3

import csv
import random
import time
import timeit

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

def print_info():
    print('Testissä valitaan ensin testin kesto sekunteina.')
    print('Viimeisen sanan saa kirjoittaa loppuun.')
    print('WPM lasketaan todellisen ajan mukaan (joka on yleensä pitempi kuin kesto koska viimeinen sana).')

def start():
    print('Valitse kesto (sec)')
    test_time = 5 # int(input('>>> '))
    t_end = time.time() + test_time
    start_time = time.time()
    wrote = []
    while t_end > time.time():
        words = get_list_of_words('./sanalista.txt')
        print(get_random_word(words))
        user_input = input('>>> ')
        end_time = time.time()
        wrote.append(user_input)
    
    print(wrote)
    print('Kokonaisaika: {:.2f} s'.format(end_time - start_time))

def show_statistic():
    pass

def cli():
    print(' (1) Info')
    print(' (2) Aloita')
    print(' (3) Statistiikkaa')
    print(' (4) Lopeta')
    choise = input('>>> ')
    return choise


if __name__ == '__main__':
    start()
    # while True:
    #     try:
    #         choise = cli()
    #         if choise == '1':
    #             print_info()
    #         elif choise == '2':
    #             start()
    #         elif choise == '3':
    #             show_statistic()
    #         elif choise == '4':
    #             if input('Haluatko varmasti lopettaa (k/e): ') == 'k':
    #                 break
    #     except (KeyboardInterrupt, EOFError):
    #         print()
    #         break
