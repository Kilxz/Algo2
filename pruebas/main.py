"""
L = [1,2,3,4,5,6,7,8]

condition = L.index(8)
print(condition)

for i in "hola":
    print(i)
"""

hola = "Holas"

print(hola[-1])

hola = hola[1:]
print(hola)

hola = "a"
hola[1:]
print(hola == "")
print("asdcadasdas")
print(hola)

def ImprimirLetra(T, letra):
    inicio = searchInL(letra)
    print(inicio.key)
    while inicio != None:
        inicio = inicio.head.value
        print(inicio.key)
        print("isEndOfWord?", inicio.isEndOfWord)
        inicio = inicio.children
    return

hola = "hola"
print(hola)
hola = hola + "ad"
print(hola)

newList = []
print(newList == None)
print(newList == [])


L = ["hola", "chau"]
L.insert(1, L[0])
print(L)
L = [1]
print(L[1] != None)
print(L[-1])