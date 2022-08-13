#Tratando o valor recebido como uma string, facilitando a manipulação
numero = input("Digite o número desejado:  ");

if(len(numero) == 1):
    print("Número com menos de dois algarismos não são considerados");
else:
    #Colocando todos os componentes do número em ordem em uma lista
    elementosNumero = list(numero);

    #Invertendo a ordem da lista
    elementosNumero.reverse();

    #Inicializando a variável que receberá o valor invertido do número
    valorInvertido = "";

    #Concatenando os valores
    for valor in elementosNumero:
     valorInvertido += valor


    #transformando em inteiro
    numeroInicial = int(numero);
    numeroInvertido = int(valorInvertido);
    

    #Verificando se os número é igual ao seu invertido6
    if(numeroInicial == numeroInvertido):
      print("O número é palíndromo");
    else:
      print("O número não é palíndromo");




