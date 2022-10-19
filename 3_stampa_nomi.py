# Ci sono 4 nomi: Alina, Bruno, Carlo, Dario.
# Chiedi una lettera all'utente.
# Stampa il nome corrispondente alla prima lettera. 
# Se non è nella lista stampa "you chose ... poorly".


lettera=input("inserisci una lettra: ")

if(lettera == "A"):
    print("hai scleto Alina")
    
else:
    if(lettera == "B"):
        print("Hai scelto Bruno")

    else:
        if(lettera == "C"):
            print("Hai scelto Carlo")

        else:
            if(lettera == "D"):
                print("Hai scleto Dario")

            else:
                print("Hai scelto poorly")




lettera=input("press any key to exit")