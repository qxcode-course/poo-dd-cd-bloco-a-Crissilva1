class Animal:
    def __init__(self, species:str, age: int, sound: str ): 
        self.species =str=species
        self.age : int = 0
        self.sound = str= sound

    def __str__(self) -> str:
        return f"{sel.species}:{self.age}:{self.sound}"
    





def main():
    animal= Animal("", "")
    while True:
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




