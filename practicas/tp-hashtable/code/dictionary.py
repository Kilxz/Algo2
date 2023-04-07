from algo1 import *

class DictionaryNode:
    
def dictionary(m):
    dict = Array(m, 0)
    return dict

def hash(k, m):
    return (k MOD m)

def insert(D, key, value):
    k = hash(k, len(D))
