from trie import *

T = Trie()

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
print(T.root[0].isEndOfWord)
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