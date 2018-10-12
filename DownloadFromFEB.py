import requests
import re
from bs4 import BeautifulSoup


def make_title(text):
    s = re.findall('(<TITLE>|<title>)(.*)(</TITLE>|</title>)', text)
    s = s[0][1]
    title = re.findall('«(.*)»', s)
    if title:
        title = title[0]
        return title
    else:
        print(s)
        return '1'


def downloader(name):
    print(name)
    result = requests.get(name)
    filetext = result.text
    return filetext


def make_file_names(filelist, vol_num):
    pages = re.findall('<p class=str>(.+)', filelist)
    if not pages:
        pages = re.findall('<p class=sod2>(.+)', filelist)
    filenums = {}
    for i in pages:
        if i.isdigit():
            if i in filenums:
                filenums[i] += 1
            else:
                filenums[i] = 1
    filenames = []
    for i in filenums:
        nums = []
        if filenums[i] == 1:
            song_num = '00' + str(i)
            song_num = song_num[len(song_num) - 3:]
            song_num += '-'
            nums.append(song_num)
        else:
            for j in range(1, filenums[i] + 1):
                song_num = '00' + str(i)
                song_num = song_num[len(song_num) - 3:]
                song_num += str(j)
                nums.append(song_num)
        for i in nums:
            name = 'http://feb-web.ru/feb/byliny/texts/so' + str(vol_num) + '/so' + str(vol_num) + '3' + str(i) + '.htm?cmd=p'
            filenames.append(name)
    return filenames


def make_song_file(filetext):
    title = make_title(filetext)
    titles.append(title)
    file = open('1initial_files/' + title + '.txt', 'w', encoding='utf-8')
    soup = BeautifulSoup(filetext, 'html5lib')
    #filetext = soup.prettify() for format files!
    file.write(filetext)
    file.close()


titles = []
filenames = []
for vol_num in range(1, 7 + 1):
    listname = 'http://feb-web.ru/feb/byliny/texts/so' + str(vol_num) + '/so' + str(vol_num) + '2001-.htm?cmd=p'
    filelist = downloader(listname)
    filenames += make_file_names(filelist, vol_num)

print(filenames)

for filename in filenames:
    filetext = downloader(filename)
    songfile = make_song_file(filetext)












