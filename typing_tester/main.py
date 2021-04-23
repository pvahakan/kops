#!/usr/bin/env python3

import csv
import random
import time
import xml.etree.ElementTree as ET

path = '../kotus-sanalista_v1/kotus-sanalista_v1.xml'

def parse_xml(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    words = []

    for item in root:
        for child in item:
            if child.tag == 's':
                words.append(child.text)

    return words

def write_to_file(f):
    with open(f, 'w') as writer:
        for word in parse_xml(path):
            if not word.startswith('à'):
                writer.write(word.strip('-') + '\n')

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