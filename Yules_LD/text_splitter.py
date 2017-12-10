################################################
# Name: text_splitter
# Author: Yonathna Guttel
# Purpose: Recieves a text for which it generate a random index as start and a end index which is defined by a given range.
#          The function crop the text to include only the string between the indecies
# Arguments: a plain txt (string object)
#            a rande for the text splet
# Returning: a partial plain txt (string object)
# date: 10.12.2017
#version: 2
##############################################
import random as rnd

def text_splitter(text, sp_range=1000):

    #get the text length
    text_len = len(text.split())

    #test that the text is long enough
    if text_len<5000 :
        return ("Text too short")

    #test if the range is too long (in regard to text):
    if (text_len - sp_range) < 0:
        return ("Range too long")

    #pick a text split which is longer than 5000 words
    ind_start = rnd.randint(0,text_len-sp_range)
    ind_end = ind_start+sp_range


    split_list = text.split()[ind_start:ind_end]
    split_text = ' '.join(str(e) for e in split_list)

    #post split text length
    print ("Split text length is: ", len(split_text.split()))

    return (split_text)

