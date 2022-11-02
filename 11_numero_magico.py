numero_magico = 7
numero = 0
output = "Game Over!"
i = 0
numero = int(input("Prova ad indovinare il numero magico: "))
while i < 10:    
    if(numero == numero_magico):
        output = "Complimenti, hai indovinato!"        
        break
    else:
        numero = int(input("hai sbagliato, ritenta: "))        
    i = i + 1
print(output)
 

lettera = input("press any key to exit")
