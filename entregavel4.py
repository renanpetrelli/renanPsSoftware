#Inicializando a lista que receberá todos os valores primos menores que 1000
#Inicializei com os valores 2,3,5,7,11
listaPrimos = [2,3,5,7,11];

numero = 12;

#Percorrendo todos os números menores que 100
while (numero < 1000):

    if(numero %2 ==0):
        numero += 1;
        continue;
    elif(numero %3 ==0):
        numero += 1;
        continue;
    elif(numero % 5 ==0):
        numero += 1;
        continue;
    elif(numero % 7 ==0):
        numero += 1;
        continue;
    elif(numero % 11 ==0):
        numero += 1;
        continue;
    else:

       listaPrimos.append(numero);
    
    numero += 1;

#Somando todoso os valores da lista com a função sum()
somaLista = sum(listaPrimos);
print(somaLista);