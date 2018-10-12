import re
import os
from bs4 import BeautifulSoup


def FixI(text):
    text = re.sub('i', 'и', text)
    return text

def OpenFile(filename):
    file = open(DIR + '/' + filename, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    return lines

def Clean(lines):
    new_lines = []
    for line in lines:
        words = line.split()
        new_line = []
        for word in words:
            flag = False
            for s in word:
                if s.isalpha():
                    flag = True
            if not flag:
                new_line.append(word)
            else:
                end = ''
                s = re.findall('([а-яёА-ЯёA-Za-z/-]+)(.)*', word)
                word = s[0][0]
                if len(s[0]) > 1:
                    end = s[0][1]
                if word.endswith('ъ'):
                    word = word[:len(word) - 1]
                if word in {'оне', 'одне', 'однех', 'однем', 'однеми'}:
                    new_form = {'оне':'они', 'одне':'одни', 'однех':'одних', 'однем':'одним', 'однеми':'одними'}
                    word = new_form[word]
                if ('-' in word) and not(word.startswith('-')):
                    ind = word.index('-')
                    if word[ind - 1] == 'ъ':
                        word = word[:ind - 1] + word[ind:]
                word += end
                new_line.append(word)
        new_line = ' '.join(new_line)
        new_lines.append(new_line)
    return new_lines

def WriteSong(lines, filename):
    file = open(DIR2 + '/' + filename, 'w', encoding='utf-8')
    for line in lines:
        if line:
            file.write(line + '\n')
    file.close()

def FixJat(lines):
    for i in range(len(lines)):
        lines[i] = re.sub('ѣ', 'е', lines[i])
    return lines

DIR = 'songs'
DIR2 = 'songs_new_now'
files = os.listdir(DIR)
for filename in files:
    print(filename)
    song_lines = OpenFile(filename)
    song_lines = FixJat(song_lines)
    song_lines = Clean(song_lines)
    WriteSong(song_lines, filename)