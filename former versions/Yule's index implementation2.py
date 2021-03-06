
# coding: utf-8

# In[1]:

def yules_ind(entry):
    """
    This function recieves a string (text) and computes its Yule's K and I
    Indices.
    the function is partialy based on Swizec Teller's blog post:
    "https://swizec.com/blog/measuring-vocabulary-richness-with-python/swizec/2528"
    """
    from nltk.stem.porter import PorterStemmer
    from itertools import groupby
    from collections import defaultdict
    import logging
    from termcolor import colored
    import sys
    
    def words(entry): # clean text from unnecessary characters
        return filter(lambda w: len(w),
                      [w.strip("0123456789!:,.?(){}[]") for w in entry.split()]) 

    def yule_param(entry): # stemm the text and creates a dictionary with counts of each word
        if len(entry.split())>2: #do it only if the text has more than 2 words
            stemmer = PorterStemmer()
            entry_dic = defaultdict(int)
            for w in words(entry):
                w = stemmer.stem(w).lower()
                entry_dic[w] +=1
            
            s1 = len(entry_dic)
            s2 = 0
            
            for i in range(1,max(entry_dic.values())+1):
                s2_iter=(i**2)*sum(1 for x in entry_dic.values() if x==i)
                s2 += s2_iter
            yule_K = (10**4)*((s2-s1)/(s1**2)) # original Yule's K indices- The lower the index, the higher LD of the text
            yule_I = 1/((s2-s1)/(s1**2))       # The inverse of Yule's K indices- more intuitive, The bigger the index, 
                                               ### the higher LD of the text
            return (round(yule_K,2),round(yule_I,2))  
        
        # If the text is 2 words and shorter, it publish a warning message and puts Nones in the indices
        else:
            print (colored("Warning: Text needs to to br longer than 2 words in order to have Lexical Diversity index",'red'))
            yule_K = None
            yule_I = None
            return (yule_K,yule_I)
    
    yule_K, yule_I = yule_param(entry)
    
    return (yule_I,yule_K) 


# In[2]:

if __name__ == "__main__":
    # different types of text: #1: Youth book, #2: Pop song, #3: Academic paper, All 45-48 words


    entry0='' #test exception
    entry1 = 'Mr. and Mrs. Dursley, of number four,            Privet Drive, were proud to say that they were perfectly normal,            thank you very much. They were the last people you’d expect to be            involved in anything strange or mysterious, because they just            didn’t hold with such nonsense.'
    entry2 ='It was twenty years ago today            Sgt. Pepper taught the band to play            They\'ve been going in and out of style            But they\'re guaranteed to raise a smile            So may I introduce to you            The act you\'ve known for all these years            Sgt. Pepper\'s Lonely Hearts Club Band'
    entry3 ='In recent years the use of species distribution models by ecologists            and conservation managers has increased considerably, along with an            awareness of the need to provide accuracy assessment for predictions            of such models. The kappa statistic is the most widely used measure for            the performance of models'


# In[3]:

#test texts
entries =["entry" + str(i) for i in range(0,4)] #create a list of the entries

#test each element in the list
for entry in entries[::-1]:
    yules = yules_ind(eval(entry))
    print('The text which starts with the words: \"',eval(entry)[0:20],'\", has a Yule\'s K inex of ',yules[0],         ", and a Yule's I index of ",yules[1])

