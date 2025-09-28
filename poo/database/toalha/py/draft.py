class Towel:    
    def __init__(self, color: str, size: str): # constructor
        self.color: str = color # atributos
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int) -> None: #none não retorna nada, aqui a toalha enxuga
        #determinada quantia- amount
        self.wetness += amount #a toalha molhada vai somar a quantia-amount de agua que precisa enxugar
        if self.wetness >= self.getMaxWetness(): #aqui relaciona a quantidade maxima de agua que ela absorve
            #até enxarcar
            print("toalha encharcada")
            self.wetness = self.getMaxWetness() # estorou o limite e enxarcou, aqui é necessario voltar ao 
            #limite

    def isDry(self) -> bool: #para saber se a toalha está seca, usa  booleano
        return self.wetness == 0 # se estiver seca é igual a 0, pois não está molhada
    
    def wringOut(self) -> None: # para secar a toalha
        self.wetness = 0 #zerar a umidade da toalha

    def getMaxWetness(self) -> int: # aqui não precisa do else, pois ao utilizar do return
        # ele sai da funçao e ja entrega o retorno que o usuario pedir, funçao declarada como inteiro
#precisa sempre de um retorno, utiliza támbem quando já sabe o valor definido, quando não retorna nada surge um undefinid
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0 #return undefinid

    def __str__(self) -> str: # toString
        return f"Cor:{self.color}, Tam:{self.size}, Umidade:{self.wetness}"
 



def main():#2
    toalha =Towel ("", "") #3 objeto manipulado
    while True:# 4 loop infinito 
        line: str = input() #5 entrada de linha
        args: list[str]= line.split (" ")
        if args [0]=="end":
            break
        elif args [0] =="new": # color size
            color = args[1] # aqui define os paraemtros de cor e tamanho ex a cor no argumento 1
            size = args[2]
            toalha = Towel (color,size)
        elif args[0]=="show":
            print(toalha)
        elif args [0]== "dry":# amount
            amount: int = int (args[1])
            toalha.dry (amount)
        else:
            print("fail:comando invalido")


main() #1           





 
class Towel:
    def __init__(self):
        self.color ="black"
        self.size = "p"
        self.wetness =0
    def __str__(self):
        return f"color:{self.color}, tam:{self.size}, hum:{self.wetness}"    

towel= Towel()
print(towel.color)
towel.color = "yellow"
print(towel.color)
print(towel.size)
print(towel.wetness)


