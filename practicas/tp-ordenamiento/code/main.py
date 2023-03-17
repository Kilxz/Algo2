
def ordenamiento4(L):
    len = length(L)
    currentNode = L.head
    for i in range(0, round(len/2)):
        currentNode = currentNode.nextNode
    valor = currentNode.value
    

def ContieneSuma(A, n):
    len = length(A)
    currentNode = A.head
    for i in range(0, len):
        number = n - currentNode.value
        currentNode2 = currentNode.nextNode
        for j in range(i + 1, len):
            if currentNode2.value == number:
                return True
            else:
                if currentNode2 != None:
                 currentNode2 = currentNode2.nextNode
        if currentNode != None:
            currentNode = currentNode.nextNode
    
    return False
