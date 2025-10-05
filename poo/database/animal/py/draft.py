class Animal:
    def __init__(self,species:str, sound : str):
        self.species : str = species
        self.sound: str = sound
        self.age : int = 0
        self.maxAge : int = 4

    def __str__(self)->str:
            return f"{self.species}:{self.age}:{self.sound}"
        
    def ageBy (self, increment : int):
        self.age += increment
        if self.age >= self.maxAge :
           print (f"warning: {self.species} morreu")
           self.age = self.maxAge

    def makeSound (self):
        if self.age == 0:
            return "---"
        if self.age == 4:
            return "RIP"  
        return self.sound
    

        


def main():
    animal= Animal(" ", " ") # crio o objeto vazio para manipular com as entradas
    while True:#manter o usuario no loop para interagir com o animal
        line: str = input() #5 entrada de linha
        print ("$" + line) #eco
        args: list[str]= line.split (" ") # pergunta ao usuario oq fazer e quebra dá espaço as respostas
        if args [0]=="end": # aqui é necessario para saber se o usuario nâo quer mais interagir
            break
        if args [0]=="init":
            species= args[1]
            sound= args[2]
            animal=Animal(species,sound)
        elif args[0]=="show":
            print(animal)
        elif args [0]== "grow":
            increment: int = int (args[1])
            animal.ageBy (increment)
        elif args[0] == "noise":
            print(animal.makeSound())
    


main() #1           




