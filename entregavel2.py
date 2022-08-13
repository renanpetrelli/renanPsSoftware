
numero = int(input("Digite o valor do número: "));

#inicializando a variável que será dividida em números primos
numeroDecomposto = numero;

#inicializando a lista que receberá os valores primos que são divisores do número
listaDivisoresPrimos = [];

#Decomponto em números primos
while(numero % 2 ==0):
    numero = (numero/2);
    listaDivisoresPrimos.append(2);

while(numero % 3 == 0):
    numero = (numero/3);
    listaDivisoresPrimos.append(3);

while(numero % 5 == 0):
    numero = (numero/5);
    listaDivisoresPrimos.append(5);

while(numero % 7 == 0):
    numero = (numero/7);
    listaDivisoresPrimos.append(7);

while(numero % 11 == 0):
    numero = (numero/11);
    listaDivisoresPrimos.append(11);

#Como a decomposição foi feita em ordem crescente, o úlimo valor da lista será o maior
ultimo = len(listaDivisoresPrimos) -1;

#Se o número não tiver sido decomposto por nenhum primo, ele é primo
if(numero == numeroDecomposto):
    print("Número primo")
else:
    print("O maior divisor primo do número colocado é:  ", listaDivisoresPrimos[ultimo]);
