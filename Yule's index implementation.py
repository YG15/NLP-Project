
# coding: utf-8

# In[ ]:

# The following code computes Yule's index which measure Lexical Diversity (LD)
# Author: Yonathan Guttel
# Date: 05.01.2017
# Version: 1


# In[46]:

def yules_ind(entry):
    """
    This function recieves a string (text) and computes its Yule's K and I
    Indices.
    The function is partialy based on Swizec Teller's blog post:
    "https://swizec.com/blog/measuring-vocabulary-richness-with-python/swizec/2528"
    """
    from nltk.stem.porter import PorterStemmer
    from itertools import groupby
    import sys
    
    def words(entry): # clean text from unnecessary characters
        return filter(lambda w: len(w),
                      [w.strip("0123456789!:,.?(){}[]") for w in entry.split()]) 

    def yule_param(entry): # stemm the text and creates a dictionary with counts of each word
        d = {}
        stemmer = PorterStemmer()
        for w in words(entry):
            w = stemmer.stem(w).lower()
            try:
                d[w] += 1
            except KeyError:
                d[w] = 1

        s1 = len(d)
        s2 = 0
        for i in range(1,max(d.values())+1):
            s2_iter=(i**2)*sum(1 for x in d.values() if x==i)
            s2 += s2_iter

        return (s1, s2)
    
    try:
        s1,s2 = yule_param(entry)
    except ValueError:
        print( "Can't calculate indecise, text length is 0")
        sys.exit()
        
        
    yule_K = (10**4)*((s2-s1)/(s1**2)) # original Yule's K indices- The lower the index, the higher LD of the text
    yule_I = 1/((s2-s1)/(s1**2))       # The inverse of Yule's K indices- more intuitive, The bigger the index, 
                                       ### the higher LD of the text
    return (yule_I,yule_K)
        


# In[57]:

# different types of text: #1: Youth book, #2: Pop song, #3: Academic paper, All 45-48 words


entry0='' #test exception
entry1 = 'Mr. and Mrs. Dursley, of number four,        Privet Drive, were proud to say that they were perfectly normal,        thank you very much. They were the last people you’d expect to be        involved in anything strange or mysterious, because they just        didn’t hold with such nonsense.'
entry2 ='It was twenty years ago today        Sgt. Pepper taught the band to play        They\'ve been going in and out of style        But they\'re guaranteed to raise a smile        So may I introduce to you        The act you\'ve known for all these years        Sgt. Pepper\'s Lonely Hearts Club Band'
entry3 ='In recent years the use of species distribution models by ecologists        and conservation managers has increased considerably, along with an        awareness of the need to provide accuracy assessment for predictions        of such models. The kappa statistic is the most widely used measure for        the performance of models'


# In[64]:

#test texts
entries =["entry" + str(i) for i in range(0,4)] #create a list of the entries

#test each element in the list
for entry in entries[::-1]:
    yules = yules_ind(eval(entry))
    print('The text which starts with the words: \"',eval(entry)[0:20],'\", has a Yule\'s I inex of ',round(yules[0],2),         ", and a Yule's K index of ",round(yules[1],2))

