from trie import *
import trieLinkedList
import linkedlist

T = Trie()

#CASOS DE PRUEBA PARA TRIE CON LISTAS DE PHYTON
print("-_-_-_-_- TRIE CON LISTAS DE PYTHON -_-_-_-_- ")
print("=========== PRUEBA Insert una palabra =========== ")
insert(T, "Aps")
print("Inserto aps")
print(T.root)
print(T.root[0].key)
print(T.root[0].children[0].key)
print(T.root[0].children[0].children[0].key)

print(" ")
print("=========== PRUEBA Insert dos palabras =========== ")
insert(T, "App")
print("Inserto App")
print(T.root)
print(T.root[0].key)
print(T.root[0].children[0].key)
print(T.root[0].children[0].children[1].key)

print(" ")
print("=========== PRUEBA isEndOfWord =========== ")
insert(T, "a")
print("Inserto a")
print(T.root[1].isEndOfWord)
print(T.root[0].children[0].isEndOfWord)

print(" ")
print("=========== PRUEBA search =========== ")

print("Busco a")
print(search(T, "a"))
print(" ")

print("Busco ap")
print(search(T, "ap"))
print(" ")

print("Busco app")
print(search(T, "app"))
print(" ")

print("Busco aps")
print(search(T, "aps"))
print(" ")

print("Busco App")
print(search(T, "App"))
print(" ")

print("Busco Aps")
print(search(T, "Aps"))
print(" ")

print(" ")
print("=========== PRUEBA delete =========== ")
print("Inserto temaiken, tema y te")
insert(T, "temaiken")
insert(T, "tema")
insert(T, "te")

print(" ")
print(" Delete de temaiken ")
print(delete(T, "temaiken"))

print(" ")
print("Encuentro te?")
print(search(T, "te"))
print("Encuentro tema?")
print(search(T, "tema"))
print("Encuentro temaiken?")
print(search(T, "temaiken"))

print(" ")
print("Inserto lodo y lodoso")
insert(T, "lodo")
insert(T, "lodoso")
print("Encuentro lodo?")
print(search(T, "lodo"))
print("Encuentro lodoso?")
print(search(T, "lodoso"))
delete(T, "lodo")
print("Despues del delete de lodo")
print("Encuentro lodo?")
print(search(T, "lodo"))
print("Encuentro lodoso?")
print(search(T, "lodoso"))

print(" ")
print("=========== PRUEBA IMPRIMIR (PUNTO 4) =========== ")
A = Trie()
print("Inserto art, amo, ac, amor, acer")
insert(A, "art")
insert(A, "amo")
insert(A, "ac")
insert(A, "amor")
insert(A, "acer")
print("Imprimo palabras que empiecen con a y tengan una longitud de 3")
imprimir(A, "a", 3)


print(" ")
print("=========== PRUEBA GETWORDS =========== ")
L = Trie()
K = Trie()
O = Trie()
I = Trie()
P = Trie()
listaaux = ["hola", "ho", "holas", "amigo", "amiga", "gato", "perro", "gat", "tema"]
listaaux2 = ["tema", "gat", "perro", "gato", "amiga", "amigo", "holas", "ho", "hola"]
listaaux3 = ["hola", "ho", "holas", "amigo", "amiga", "Gato", "perro", "gat", "tema"]
listaaux4 = ["hola", "ho", "holas", "amigo", "amiga", "gatO", "perro", "gat", "tema"]
listaaux5 = ["hola", "ho", "holas", "amigo", "amiga", "gatos", "perro", "gat", "tema"]
for i in listaaux:
    insert(L, i)
for i in listaaux2:
    insert(K, i)
for i in listaaux3:
    insert(O, i)
for i in listaaux4:
    insert(I, i)
for i in listaaux5:
    insert(P, i)
B = getWords(L)
C = getWordsBackwards(L)
print(B)
print(C)

print(" ")
print("=========== PRUEBA PUNTO 5 equal(T) =========== ")
print("Son iguales Trie L con K?")
print(equal(L, K))
print("Son iguales Trie L con O?")
print(equal(L, O))
print("Son iguales Trie L con I?")
print(equal(I, L))
print("Son iguales Trie L con P?")
print(equal(P, L))

print(" ")
print("=========== PRUEBA PUNTO 6 invertidas(T) =========== ")
print("Existen palabras invertidas en L?")
print(invertidas(L))
print("Inserto agima")
insert(L, "agima")
print("Existen palabras invertidas en L?")
print(invertidas(L))
T = None
T = Trie()
L = None
K = None
O = None

#CASOS DE PRUEBA PARA TRIE CON LINKEDLIST
print(" ")
print("-_-_-_-_- TRIE CON LINKEDLISTS -_-_-_-_- ")
print("=========== PRUEBA Insert una palabra =========== ")
trieLinkedList.insert(T, "Aps")
print("Inserto Aps")
print(T.root)
print(T.root.head.value.key)
print(T.root.head.value.children.head.value.key)
print(T.root.head.value.children.head.value.children.head.value.key)

print(" ")
print("=========== PRUEBA Insert dos palabras =========== ")
trieLinkedList.insert(T, "App")
print("Inserto App")
print(T.root)
print(T.root.head.value.key)
print(T.root.head.value.children.head.value.key)
print(T.root.head.value.children.head.value.children.head.value.key)

print(" ")
print("=========== PRUEBA isEndOfWord =========== ")
trieLinkedList.insert(T, "a")
print("Inserto a")
print(T.root.head.value.key)
print(T.root.head.value.isEndOfWord)
print(T.root.head.nextNode.value.key)
print(T.root.head.nextNode.value.isEndOfWord)


print(" ")
print("=========== PRUEBA search =========== ")

print("Busco a")
print(trieLinkedList.search(T, "a"))
print(" ")

print("Busco ap")
print(trieLinkedList.search(T, "ap"))
print(" ")

print("Busco Ap")
print(trieLinkedList.search(T, "Ap"))
print(" ")

print("Busco app")
print(trieLinkedList.search(T, "app"))
print(" ")

print("Busco App")
print(trieLinkedList.search(T, "App"))
print(" ")

print("Busco Aps")
print(trieLinkedList.search(T, "Aps"))
print(" ")

print(" ")
print("=========== PRUEBA delete =========== ")
print("Inserto temaiken, tema y te")
trieLinkedList.insert(T, "temaiken")
trieLinkedList.insert(T, "tema")
trieLinkedList.insert(T, "te")

print(" ")
print("Delete de temaiken ")
print(trieLinkedList.delete(T, "temaiken"))

print(" ")
print("Encuentro te?")
print(trieLinkedList.search(T, "te"))
print("Encuentro tema?")
print(trieLinkedList.search(T, "tema"))
print("Encuentro temaiken?")
print(trieLinkedList.search(T, "temaiken"))

print(" ")
print("Inserto lodo y lodoso")
trieLinkedList.insert(T, "lodo")
trieLinkedList.insert(T, "lodoso")
print("Encuentro lodo?")
print(trieLinkedList.search(T, "lodo"))
print("Encuentro lodoso?")
print(trieLinkedList.search(T, "lodoso"))
trieLinkedList.delete(T, "lodo")
print("Despues del delete de lodo")
print("Encuentro lodo?")
print(trieLinkedList.search(T, "lodo"))
print("Encuentro lodoso?")
print(trieLinkedList.search(T, "lodoso"))

print(" ")
print("=========== PRUEBA IMPRIMIR (PUNTO 4) =========== ")
A = Trie()
print("Inserto art, amo, ac, amor, acer")
trieLinkedList.insert(A, "art")
trieLinkedList.insert(A, "amo")
trieLinkedList.insert(A, "ac")
trieLinkedList.insert(A, "amor")
trieLinkedList.insert(A, "acer")
print("Imprimo palabras que empiecen con a y tengan una longitud de 3")
trieLinkedList.imprimir(A, "a", 3)

print(" ")
print("=========== PRUEBA GETWORDS =========== ")
L = Trie()
K = Trie()
O = Trie()
I = Trie()
P = Trie()
listaaux = ["hola", "ho", "holas", "amigo", "amiga", "gato", "perro", "gat", "tema"]
listaaux2 = ["tema", "gat", "perro", "gato", "amiga", "amigo", "holas", "ho", "hola"]
listaaux3 = ["hola", "ho", "holas", "amigo", "amiga", "Gato", "perro", "gat", "tema"]
listaaux4 = ["hola", "ho", "holas", "amigo", "amiga", "gatO", "perro", "gat", "tema"]
listaaux5 = ["hola", "ho", "holas", "amigo", "amiga", "gatos", "perro", "gat", "tema"]
for i in listaaux:
    trieLinkedList.insert(L, i)
for i in listaaux2:
    trieLinkedList.insert(K, i)
for i in listaaux3:
    trieLinkedList.insert(O, i)
for i in listaaux4:
    trieLinkedList.insert(I, i)
for i in listaaux5:
    trieLinkedList.insert(P, i)
B = trieLinkedList.getWords(L)
C = trieLinkedList.getWordsBackwards(L)
linkedlist.printlist(B)
linkedlist.printlist(C)

print(" ")
print("=========== PRUEBA PUNTO 5 equal(T) =========== ")
print("Son iguales Trie L con K?")
print(trieLinkedList.equal(L, K))
print("Son iguales Trie L con O?")
print(trieLinkedList.equal(L, O))
print("Son iguales Trie L con I?")
print(trieLinkedList.equal(I, L))
print("Son iguales Trie L con P?")
print(trieLinkedList.equal(P, L))

print(" ")
print("=========== PRUEBA PUNTO 6 invertidas(T) =========== ")
print("Existen palabras invertidas en L?")
print(trieLinkedList.invertidas(L))
print("Inserto agima")
trieLinkedList.insert(L, "agima")
print("Existen palabras invertidas en L?")
print(trieLinkedList.invertidas(L))
T = None
T = Trie()
L = None
K = None
O = None