# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:14:11 2020

@author: Carol
"""

#import os
import re
import pypinyin
import sys

'''
def import_data(rep="../1_data/1_original"):
    """
    Input = str rep des data
    Output = list files_read[[lignes de ficher1],[lignes de ficher2]...]
    """   
    files_read = []
    for file in os.listdir(rep):
        if file[0] == ".": continue
        with open(os.path.join(rep,file), "r", encoding="utf-8") as file_opened:
            file_read = file_opened.readlines()
            files_read.append(file_read)
    return files_read
'''

def cree_corpus(rep="../1_data/1_original",file="nouvelles"):
    """
    Input = str rep des data
    Output = fichier ../1_data/2_corpus/corpus.txt
    """   
    with open(rep+'/'+file+'.txt', "r", encoding="utf-8") as file_opened:
        file_read = file_opened.readlines()
    corpus = []
    for i in file_read:
        if i != "\n":
            corpus.append(i.strip())
    with open("../1_data/2_corpus/"+'corpus_'+str(file)+'.txt', "w", encoding="utf-8") as \
    file_opened:
        for i in corpus:
            file_opened.write(i)
            file_opened.write("\n")
    return True

def corpus_aseg(rep="../1_data/2_corpus", file="nouvelles"):
    """
    Input = str rep des data
    Output = fichier ../1_data/2_corpus/corpus_humain.txt
    """
    with open(rep+'/'+'corpus_'+str(file)+'.txt', "r", encoding="utf-8") as \
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
    with open(rep+'/corpus_'+str(file)+'_aseg.txt', "w", encoding="utf-8") as\
    file_opened:
        file_opened.write(corpus_humain)
    return True

def pinyin(phrase):
    """
    Input = str phrase
    Output = str pinyin correspond
    """
    pyin = ''
    for i in pypinyin.pinyin(phrase):
        pyin = pyin + ''.join(i) + " "
    return pyin

if __name__ =="__main__" :
    cree_corpus(rep="../1_data/1_original", file = sys.argv[1])
    corpus_aseg(rep="../1_data/2_corpus", file= sys.argv[1])
    