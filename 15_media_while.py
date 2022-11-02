tot=0
i=0
while True:
    n=int(input("inserisci un numero "))
    if(n==0):
        break
    else:
        tot=tot+n
        i=i+1
print(tot/i)
