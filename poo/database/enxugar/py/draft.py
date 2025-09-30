class Towel:
    def __init__ (self, color:str, size:str):
        self.color= str = color
        self.size = str = size
        self.wetness: int =0

    def dry(self, amount:int) : # não pode fazer operação dentro do parametro
        self.wetness +=amount  

    def  wringOut (self)-> None: 
        self.wetness =0   

    def  getMaxWetness(self)->int:
        if self.size == "P":
            return 10
        if self.size == "M" :
            return 20
        if self.size == "G" :
            return 30
        return 0
    def isDry (self)-> bool:
            return self.wetness==0         
    
    def __str__(self) -> str: # toString
        return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}"
    


def main ():
    toalha =Towel ("", "")
    while True:
        line:str=input()
        print ("$" + line) #eco
        args: list[str]=line.split(" ")
        if args[0]=="end":
            break
        elif args [0]== "criar": #color,size 
            color = args[1]
            size = args[2]
            toalha = Towel(color , size)
        elif args [0]== "mostrar":
            print(toalha)
        elif args [0]== "dry":# amount
            amount: int = int (args[1])
            toalha.dry (amount)
        else:
            print("sim")

main()            
