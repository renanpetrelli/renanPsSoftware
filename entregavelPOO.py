
#Classe auv com os atributos pedidos e o atributo lista de cameras
class auv:

    def __init__(self,thursters,sensores,anoConstrucao,nome,cameras):
        self.thursters = thursters
        self.sensores = sensores
        self.anoConstrucao = anoConstrucao
        self.nome = nome
        self.cameras = cameras
    
    def __repr__(self):
        r = "Nome {} thursters {} sensores {} ano construção {} cameras {}".format(self.nome,self.thursters,self.sensores,self.anoConstrucao,self.cameras)
        return r

    #retorna a quantidade de cameras que o AUV possui
    def quantidadeCameras(self):
        return len(self.cameras)

    

#Classe que possui informacao de todos os AUVs da Nautilus
class portifolioNautilus:

    def __init__(self,auvs):
        self.auvs = auvs

    #metodo exibicao AUVs por tabela
    def exibirAuvs(self):
     for auv in self.auvs:
        print(auv.nome,' ',auv.thursters,' ',auv.anoConstrucao,' ',auv.sensores,' ',auv.cameras)

    #metodo selecionar AUV pelo nome e exibir informacaoes individuais
    def selecionarAuvPeloNome(self,nome):
     dicionarioAuvs = {}
     for auv in self.auvs:
        dicionarioAuvs[auv.nome] = [auv]
     auvSelecionado = dicionarioAuvs[nome]

     return auvSelecionado
    
    #Ordenar em ordem decrescente os AUVs pelo ano de construcao
    def rankPorAnoConstrucao(self):
     dicionario = {}
     listaOrdenadaPeloAno =[]
     for auv in self.auvs:
        dicionario[auv.anoConstrucao] = [auv.nome]
    
     for ano in reversed(dicionario.keys()):
        listaOrdenadaPeloAno.append(dicionario[ano])
    
     return listaOrdenadaPeloAno

    #Exibir o nome do AUV e sua respectiva quantidade de cameras
    def listarAuvQuantidadeCameras(self):
     dicionario = {}
     for auv in self.auvs:
        dicionario[auv.nome] = [auv.quantidadeCameras()]
    
     return dicionario

     


#AUVs naurilus
#Instanciando Objetos
lua = auv(6,
['External pressure sensor','internal pressure sensor','higher front camera','Center front Camera', 'lower front camera','ground font camera'],
2022,
'lua',
['higher front camera','Center front Camera', 'lower front camera','ground font camera'])

brHue = auv(8,['pressure sensor','front camera','ground camera 1', 'ground camera 2'],2020,'brHue',
['front camera','ground camera 1', 'ground camera 2'])

#Criando lista de Objetos auv
listaAuvs = [lua,brHue]

#Instanciando o objeto portifolioNautilus
auvsNautilus = portifolioNautilus(listaAuvs)

auvsNautilus.exibirAuvs()


auvSelecionado = auvsNautilus.selecionarAuvPeloNome('brHue')
print(auvSelecionado)

rankAnoConstrucao = auvsNautilus.rankPorAnoConstrucao()
print(rankAnoConstrucao)

dicionarioAuvQuantidadeCameras = auvsNautilus.listarAuvQuantidadeCameras()
print(dicionarioAuvQuantidadeCameras)

