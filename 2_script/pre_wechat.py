# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:27:33 2021

@author: Carol
"""
import re
import pypinyin

def pinyin(phrase):
    """
    Input = str phrase
    Output = str pinyin correspond
    """
    pyin = ''
    for i in pypinyin.pinyin(phrase):
        pyin = pyin + ''.join(i) + " "
    return pyin
text = []
with open('../1_data/1_original/chat.txt', "r") as c:
    file_read = c.readlines()
for i in range(len(file_read)):
    if i%5 == 2:
        text.append(file_read[i])

with open('../1_data/2_corpus/corpus_chat.txt', "w") as c:
    c.writelines(text)

with open('../1_data/2_corpus/corpus_chat.txt', "r", encoding="utf-8") as \
file_opened:
    file_opened = file_opened.read()
pattern = r'？|。|！|\n'
result_list = re.split(pattern, file_opened)
corpus_humain = ''
c = 0
for i in result_list:
    if i != '' and i[0] != '&':
        c += 1
        corpus_humain += str(c)+'\t'+str(i)+'\n'+('#'+pinyin(i))+'\n#\n#\n'   
    elif i != '' and i[0] == '&':
        corpus_humain +=str(i)+'\n'
with open('../1_data/2_corpus/corpus_chat_aseg.txt', "w", encoding="utf-8") as\
file_opened:
    file_opened.write(corpus_humain)

