message: str = 'Inserisci un numero: '
number: int = int(input(message))

max = number
min = number

while number != 0:  
    if (number > max):
        max = number
    if (number < min):
        min = number
    number: int = int(input(message)) 
print("Max: ", max)
print("Min: ", min)
a=input("Press any key to exit")
