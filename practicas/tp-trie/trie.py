
class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False


def searchInL(L, element):
    long = len(L)
    for i in range(0, long):
        if L[i].key == element:
            return i
    return None

def insert(T, element):

    if T.root == None:
        L = []
        T.root = L
    else:
        L = T.root
    return insertR(T.root, L, element)

def insertR(LastNode, L, element):
    condition = searchInL(L, element[0])

    if condition == None:
        TNode = TrieNode()
        TNode.key = element[0]
        
        TNode.parent = LastNode
        if len(element) == 1:
            TNode.children = None
        else:
            newList = []
            TNode.children = newList
        L.append(TNode)
    else:
        TNode = L[condition]

    if len(element) != 1:
        element = element[1:]
        if condition == None:
            insertR(TNode, newList, element)
        else:
            if TNode.children == None:
                newList = []
                TNode.children = newList
            insertR(L[condition], L[condition].children, element)
        return
    else:
        TNode.isEndOfWord = True
        return

def search(T, element):
    return searchR(T.root, element)

def searchR(L, element):
    if L == None:
        return False
    
    condition = searchInL(L, element[0])
    
    if condition == None:
        return False
    
    if len(element) != 1:
        element = element[1:]
        return searchR(L[condition].children, element)
    else:
        if L[condition].isEndOfWord == True:
            return True
        else:
            return False


def searchForLastNode(T, element):
    return searchForLastNodeR(T.root, element)

def searchForLastNodeR(L, element):
    condition = searchInL(L, element[0])
    if condition == None:
        return False
    
    if len(element) != 1:
        element = element[1:]
        return searchForLastNodeR(L[condition].children, element)
    else:
        if L[condition].isEndOfWord == True:
            return L[condition]
        else:
            return False


def delete(T, element):
    condition = search(T, element)
    if condition == False:
        return False
    finalNode = searchForLastNode(T, element)
    finalNode.isEndOfWord = False
    
    return deleteR(T, finalNode, element)

def deleteR(T, finalNode, element):

    if finalNode.children != None:
        finalNode.isEndOfWord = False
        return True
    else:
        if finalNode.isEndOfWord == False:
            if finalNode.parent == T.root:
                T.root.remove(finalNode)
                return True
            parentNode = finalNode.parent
            parentList = parentNode.children
            parentList.remove(finalNode)

            if len(parentList) ==  0:
                parentNode.children = None
            return deleteR(T, finalNode.parent, element)
        else:
            return True


