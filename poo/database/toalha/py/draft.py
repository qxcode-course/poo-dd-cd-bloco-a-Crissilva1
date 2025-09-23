<<<<<<< HEAD
class Towel:    #this
    def __init__(self, color: str, size: str): # constructor
        self.color: str = color # atributos
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.getMaxWetness():
            print("toalha encharcada")
            self.wetness = self.getMaxWetness()

    def isDry(self) -> bool:
        return self.wetness == 0
    
    def wringOut(self) -> None:
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

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
            color = args[1]
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





 
=======
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
>>>>>>> 7a3d6ba5f6c2f28cabc5701885473ffbc3b0afcf


