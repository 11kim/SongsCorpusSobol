import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import re
import os
import json
from pprint import pprint as pp
import sys


def uni(text):
    for i in range(len(text)):
        text[i] = text[i].lower()
        word = text[i]
        while (len(word) > 0) and not(word[-1].isalpha()):
            word = word[:len(word) - 1]
        while (len(word) > 0) and not(word[0].isalpha()):
            word = word[1:]
        text[i] = word
    return text

def open_file(filename):
    file = open(DIR + '/' + filename, 'r', encoding='utf-8')
    text = file.readlines()
    text = [uni(line.split()) for line in text]
    return text


def write_song(song_text, filename):
    filename = filename[:len(filename) - 3] + 'json'
    file = open(DIR2 + '/' + filename, 'w', encoding='utf-8')
    json.dump(song_text, file, sort_keys = True, indent=2, ensure_ascii=False)
    file.close()


def info(word):
    chars = morph.parse(word)
    feat = str(chars[0].tag).split(',')
    return {word:{'OpencorporaTag':feat, 'normal_form':chars[0].normal_form}}



DIR = 'songs_new'
DIR2 = 'songs_py'
files = os.listdir(DIR)
for filename in files:
    song_text = open_file(filename)
    song_py = []
    i = 1
    for line in song_text:
        s = []
        for word in line:
            s.append(info(word))
        song_py.append(s)
        i += 1
    #print(song_py)
    write_song(song_py, filename)