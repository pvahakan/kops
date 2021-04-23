#!/usr/bin/env python3

import csv
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

if __name__ == '__main__':
    write_to_file('sanalista.txt')