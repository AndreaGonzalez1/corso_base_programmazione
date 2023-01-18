string=input("inserisci una parola: ")
l=len(string)
i=0
conta=0
while i < l:
    if string[i]=="a":
        conta=conta+1
    if string[i]=="e":
        conta=conta+1
    if string[i]=="i":
        conta=conta+1
    if string[i]=="o":
        conta=conta+1
    if string[i]=="u":
        conta=conta+1
        
    i=i+1
print(conta)