import csv
import re
from collections import Counter

with open("bike-items.txt") as source:
    r = csv.reader(source, delimiter=',', quotechar='"')
    text = re.compile(r'\b[a-zA-Z]+\b')
    docs = [ (' '.join(re.findall(text, x[0])).lower(), ' '.join(re.findall(text, x[1])).lower())  \
            for i,x in enumerate(r) if i > 1 ]
    
#print(docs[0][0],docs[0][1])

items_t = [ d[0] for d in docs ] # item titles
items_d = [ d[1] for d in docs ] # item descriptions
items_i = range(0, len(items_t)) # item id

corpus = items_t[0:5]

def encode(term):
    temp = 0

    for i in range(0, len(term)):
        temp += ord(term[i])

    return temp

def get_tf(corpus):
    #tf = Counter()
    
    temp = dict()
    for key in corpus:
        temp[key] = encode(key)
    
    return temp

tf = get_tf(corpus)

print(tf)
