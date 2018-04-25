
def incremento(x):

    x += 1
    return x

def decremento(x):
	
	x -= 1
	return x
	


print("Soma...")
x = int(input("Primeiro Numero: "))
y = int(input("Segundo Numero: "))

def add (x, y):
	
	while(y):
		x = incremento(x)
		y = decremento(y)
	return x

soma = add(x,y)
print("A soma é: ", soma)


print("Subtracao...")
x = int(input("Primeiro Numero: "))
y = int(input("Segundo Numero: "))

def sub (x, y):
	
	while(y):
		x = decremento(x)
		y = decremento(y)
	return x

sub = sub(x,y)
print("A subtração e: ", sub)


print("Multiplicacao...")
x = int(input("Primeiro Numero: "))
y = int(input("Segundo Numero: "))

def prod(x, y):
	
	y = y -1
	while(y):
		x = add(x,x)
		y = decremento(y)
	return x

multiplicacao = prod(x,y)
print("A multiplicacao é: ", multiplicacao)


print("Divisao inteira...")
x = int(input("Primeiro Numero: "))
y = int(input("Segundo Numero: "))

def mod(divisor, dividendo):
	
	i = 0
	while(divisor > 0):
		x = sub(divisor, dividendo)
		i = i +1
	return i

div = mod(x,y)
print("A divisão inteira é: ",div)




