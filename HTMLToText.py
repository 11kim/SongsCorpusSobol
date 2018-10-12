import re
import os
from bs4 import BeautifulSoup


def OpenFile(file_name):
    file = open(DIR + '/' + file_name, 'r', encoding='utf-8')
    text = file.read()
    file.close()
    return text


def FixJat(text):
    text = re.sub('<font class=old>&#x463;</font>', 'ѣ', text)
    return text


def CleanFile(text):
    text = re.sub('&nbsp;', '', text)
    return text


def Normilize(file_name):
    file_name = file_name[:len(file_name) - 3]
    while file_name[-1] in {'.', '...'}:
        file_name = file_name[:len(file_name) - 1]
    file_name += '.txt'
    return file_name


def MakeSongFile(file_name, song_text):
    file_name = Normilize(file_name)
    file = open(DIR2 + '/' + file_name, 'w', encoding='utf-8')
    file.write(song_text)
    file.close()


DIR = '1initial_files'
DIR2 = 'songs'
files = os.listdir(DIR)
for file_name in files:
    file_text = FixJat(OpenFile(file_name))
    file_text = CleanFile(file_text)
    soup = BeautifulSoup(file_text, 'html5lib')
    stihs = soup.select('.text .stih1')
    tags = ['stih0', 'stih', 'stih3', 'stih3-6', 'stih5', 'stix0', 'stix', 'stix1', 'stix2', 'stix2-6', 'stix3', 'stix3b', 'stix3-6']
    for tag in tags:
        if stihs:
            break
        stihs = soup.select('.text .%s' % tag)
    song_text = ''
    for stih in stihs:
        song_text += stih.get_text() + '\n'
    if song_text == '':
        print(file_name)
    MakeSongFile(file_name, song_text)



