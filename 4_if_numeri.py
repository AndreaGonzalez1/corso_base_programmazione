n1 = int(input("Inserisci il primo numero"))
n2 = int(input("Inserisci il secondo numero"))

stampato = 0

if(n1 > 10):
    print("Fuori Scala")
    stampato = 1
     
if(n2 > 50):
    print("Troppo Grande")
    stampato = 1

if(stampato == 0):
    print("Tutto ok")
