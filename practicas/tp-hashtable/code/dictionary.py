from algo1 import *

class Dictionary:
    head = None

class DictionaryNode:
    key = None
    value = None
    nextNode = None
    
def dictionary(m):
    dict = Array(m, 0)
    return dict

def hash(k, m):
    return (k % m)

def insert(D, key, value):
    k = hash(k, len(D))
