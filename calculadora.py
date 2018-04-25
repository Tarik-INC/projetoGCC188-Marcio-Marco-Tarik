
def incremento(x):

    x += 1
    return x

def decremento(x):
	
	x -= 1
	return x
	

x = int(input("Primeiro Numero: "))
y = int(input("Segundo Numero: "))

def add (x, y):
	
	while(y):
		x = incremento(x)
		y = decremento(y)
	return x

soma = add(x,y)
print("A soma é: ", soma)

x = int(input("Primeiro Numero: "))
y = int(input("Segundo Numero: "))

def sub (x, y):
	
	while(y):
		x = decremento(x)
		y = decremento(y)
	return x

sub = sub(x,y)
print("A subtração e: ", sub)
