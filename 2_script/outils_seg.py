# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:23:27 2021

@author: Carol
"""
import sys
import re
import jieba
import thulac
import pkuseg
#from pyhanlp import *

def import_data(rep="../1_data/2_corpus/",file="corpus_chat"):
    """
    Input = str rep des data
    Output = list[str] contenu du fichier, rep
    """
    with open(rep+file+'.txt', 'r', encoding='utf-8') as file_opened:
        contenu = file_opened.readlines()
    pattern = r'？|。|！|\n'
    result_list = re.split(pattern, str(contenu))
    return result_list, rep

def seg_jieba(result_list,rep="../1_data/2_corpus/",file="corpus_chat"):
    """
    Input = list[str] contenu du fichier, rep
    Output = fichier seg ../1_data/2_corpus/file_jieba.txt
    """
    print(file)
    for i in result_list:
        with open (rep+file+'_jieba.txt', 'a') as file_opened:
            file_opened.write("/ ".join(jieba.cut(str(i), cut_all=False)))  # 精确模式
            file_opened.write('\n')
    return True

def seg_thulac(rep="../1_data/2_corpus/",file="corpus_chat"):
    """
    Input = str  rep
    Output = fichier seg ../1_data/2_corpus/file_thulac.txt
    """
    thu_seg = thulac.thulac(seg_only=True)
    thu_seg.cut_f(rep+file+'.txt', rep+file+'_thulac.txt')
    return True

def seg_pku(result_list,rep="../1_data/2_corpus/",file="corpus_chat"):
    """
    Input = str contenu du fichier, rep
    Output = fichier seg ../1_data/2_corpus/file_pku.txt
    """
    pkuseg.test(rep+file+'.txt', rep+file+'_pku.txt')
    '''seg = pkuseg.pkuseg()
    for i in result_list:     
        seg_list = seg.cut(str(i))
        with open (rep+file+'_pku.txt', 'a') as file_opened:
           file_opened.write(str(seg_list))
           file_opened.write('\n')'''
    return True

'''
def seg_hanlp(result_list,rep="../1_data/2_corpus/",file="corpus_chat"):
    """
    Input = str contenu du fichier, rep
    Output = fichier seg ../1_data/2_corpus/file_hanlp.txt
    """
    for i in result_list:
        HanLP.segment(i)
        with open (rep+file+'_hanlp.txt', 'a') as file_opened:
           file_opened.write(seg_list)
    return True
'''

        

if __name__ =="__main__" :
    seg_jieba(import_data(rep="../1_data/2_corpus/",file=sys.argv[1]),file=sys.argv[1])
    seg_thulac(rep="../1_data/2_corpus/",file=sys.argv[1])
    seg_pku(import_data(rep="../1_data/2_corpus/",file=sys.argv[1]),file=sys.argv[1])
   # seg_hanlp(import_data(rep="../1_data/2_corpus/",file=sys.argv[1]))