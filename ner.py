# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import nltk
import numpy
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

def get_continuous_chunks(text):
     chunked = ne_chunk(pos_tag(word_tokenize(text)))
     prev = None
     continuous_chunk = []
     current_chunk = []
     for i in chunked:
             if type(i) == Tree:
                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
             elif current_chunk:
                     named_entity = " ".join(current_chunk)
                     if named_entity not in continuous_chunk:
                             continuous_chunk.append(named_entity)
                             current_chunk = []
             else:
                     continue
     return continuous_chunk
 
     
with open('D:/books/test.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
     
my_sent = "WASHINGTON -- In the wake of a string of abuses by New York police officers in the 1990s, Loretta E. Lynch, the top federal prosecutor in Brooklyn, spoke forcefully about the pain of a broken trust that African-Americans felt and said the responsibility for repairing generations of miscommunication and mistrust fell to law enforcement."
print()

file = open("D:/books/output.txt", "w")
NEs = get_continuous_chunks(data)

for item in NEs:
  file.write("%s\n" % item)
  
file.close()