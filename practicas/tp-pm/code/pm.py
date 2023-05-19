import dictionary
#O(n)
def existChar(String, c):
    for i in range(len(String)):
        if String[i] == c:
            return True
    return False

def isPalindrome(String):
    n = len(String)
    for i in range(0, round(n/2)):
        if String[i] != String[-(i+1)]:
            return False
    return True

def getBiggestIslandLen(String):
    biggest = 1
    char = String[0]
    aux = 1
    for i in range(1, len(String)):
        if String[i] != char:
            if aux > biggest:
                biggest = aux
            char = String[i]
            aux = 1
        else:
            aux += 1
    return biggest

def isAnagram(String, String2):
    if len(String) != len(String2):
        return False
    m = ord("z") - ord("a")
    hashtable = dictionary.dictionary(m)
    for i in range(len(String)):
        dictionary.insert(hashtable, ord(String[i]), String[i])
    for i in range(len(String2)):
        if dictionary.search(hashtable, ord(String2[i])) == None:
            return False
        else:
            dictionary.delete(hashtable, ord(String2[i]))
    return True

def verifyBalancedParentheses(String):
    n = len(String)
    contador = 0
    for i in range(0, n):
        if String[i] == "(":
            contador += 1
        if String[i] == ")":
            contador -= 1
        if contador < 0:
            return False
    if contador == 0:
        return True
    else:
        return False
    
def reduceLen(String):
    n = len(String)
    newString = ""
    aux = String[0]
    for i in range(1, n):
        if String[i] != aux:
            if aux is not None:
                newString = newString + aux
            aux = String[i]
            if i == n-1:
                newString = newString + String[i]
        else:
            aux = None
    return newString

def isContained(String, String2):
    n = len(String)
    for i in range(0, n):
        if String[i] == String2[0]:
            String2 = String2[1:]
            if String2 == "":
                return True
    return False

def isPatternContained(String, String2, c):
    n = len(String)
    for i in range(0, n):
        if String[i] == String2[0]:
            String2 = String2[1:]
        elif String2[0] == c:
            String2 = String2[1:]
        
        if String2 == "":
            return True
    return False


"""
Crea la lista pi, el primer elemento es 0. Luego en el for
comienza comparando el primer elemento con el segundo, si son iguales
se le coloca k + 1 al elemento i. Luego de eso se sigue comparando el elemento P[k+1] con el P[i]. Si k es
mayor que 0 y el elemento P[k] es diferente del elemento P[i] entonces dentro del while k vuelve a ser 0.
"""
def kmp(P):
    m = len(P)
    pi = [0] * m
    pi[0] = 0
    k = 0
    for i in range (1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k-1]
        if P[k] == P[i]:
            k = k + 1
        pi[i] = k
    return pi
