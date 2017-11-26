################################################
# Name: text_splitter
# Author: Yonathna Guttel
# Purpose: Recieves a text for which it generate two random indecies, cand crop the text to include only the string between the indecies
# Arguments: a plain txt (string object)
# Returning: a partial plain txt (string object)
# date: 26.11.2017
#version: 1
##############################################
import random as rnd

def text_splitter(text):

    #get the text length
    text_len = len(text.split())

    #test that the text is long enough
    if text_len<5000:
        return ("Text too short")

    #pick a text split which is longer than 5000 words
    dif=0
    while dif <5000 :
        indeces = [rnd.randint(0,text_len),rnd.randint(0, text_len)]
        ind_start = min(indeces)
        ind_end = max(indeces)
        dif =ind_end-ind_start

    split_list = text.split()[ind_start:ind_end]
    split_text = ' '.join(str(e) for e in split_list)

    #post split text length
    print ("Split text length is: ", len(split_text.split()))

    return (split_text)

