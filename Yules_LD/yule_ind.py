################################################
# Name: yules_ind
# Author: Yonathna Guttel
# Purpose: computes Yule's index which measure Lexical Diversity (LD)
# Arguments: a text string
# Returning: Its Yule indecies
# date: 26.11.2017
# Version: 3
##############################################

def yules_ind(entry):
    """
    This function recieves a string (text) and computes its Yule's K and I
    Indices.
    the function is partialy based on Swizec Teller's blog post:
    "https://swizec.com/blog/measuring-vocabulary-richness-with-python/swizec/2528"
    """
    from nltk.stem.porter import PorterStemmer
    from collections import defaultdict
    from termcolor import colored

    def words(entry):  # clean text from unnecessary characters
        return filter(lambda w: len(w),
                      [w.strip("0123456789!:,.?(){}[]") for w in entry.split()])

    def yule_param(entry):  # stemm the text and creates a dictionary with counts of each word


        if len(entry.split()) > 2:  # do it only if the text has more than 2 words
            stemmer = PorterStemmer()
            entry_dic = defaultdict(int)
            for w in words(entry):
                w = stemmer.stem(w).lower()
                entry_dic[w] += 1

            # generate the index sub values
            s1 = len(entry_dic)
            s2 = 0

            # calculate s2
            for i in range(1, max(entry_dic.values()) + 1):
                s2_iter = (i ** 2) * sum(1 for x in entry_dic.values() if x == i)
                s2 += s2_iter

            # If s2=s2 (only unique words in text) Yule's index cannot be calculated due to zero devision, show worning
            ##mesage and plave Nones in indices
            if s1 == s2:
                print(colored("Warning: The number of words in the text and the number of uniques words is equal, "
                              "division by 0 occured", 'magenta'))
                yule_K = None
                yule_I = None
                return (yule_K, yule_I)

            # If everything is OK, calculate as normal
            else:
                yule_K = (10 ** 4) * (
                (s2 - s1) / (s1 ** 2))  # original Yule's K indices- The lower the index, the higher LD of the text
                yule_I = 1 / (
                (s2 - s1) / (s1 ** 2))  # The inverse of Yule's K indices- more intuitive, The bigger the index,
                ### the higher LD of the text
            return (round(yule_K, 2), round(yule_I, 2))

            # If the text is 2 words and shorter, it publish a warning message and puts Nones in the indices
        else:
            print(colored("Warning: Text needs to to be longer than 2 words in order to have Lexical Diversity index",
                          'red'))
            yule_K = None
            yule_I = None
            return (yule_K, yule_I)

    yule_K, yule_I = yule_param(entry)

    return (yule_I, yule_K)


if __name__ == "__main__":
    import Gutenberg_text_scrapper as gts
    import text_splitter as ts

    corpus_num = [460,2003] #can be a single number too, but it has to be in a list
    iters= 15 #number of trial for each text


    for txt in corpus_num:
        text = gts.get_scrap(txt)
        for iter in range(iters):
            split_text=ts.text_splitter(text)
            yules = yules_ind(split_text)
            print('The text which starts with the words: \"', split_text[0:20], '\", has a Yule\'s K inex of ', yules[0],
                  ", and a Yule's I index of ", yules[1])
