

continuaIncluindoElemento = True;
lista = [];

while(continuaIncluindoElemento):

  lista.append(int(input("Digite um numero para adicionar a lista: ")));

  resposta = input("Deseja continuar preenchendo valores na lista? ( 's' para sim , qualquer outra tecla para encerrar)");

  if(resposta !='s'):
    continuaIncluindoElemento = False;


print("lista:")

for elemento in lista:
    print(elemento);

ultimo = len(lista) -1;

if(lista[0] == lista[ultimo]):
    print("O primeiro e o ultimo são iguais")
else:
    print("o primeiro e o ultimo nao sao iguais")