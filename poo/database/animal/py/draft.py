class Animal: #construtor, é direcionado na criação de um objeto, no exemplo
#o animal, que vai ser atribuido as suas caracteristicas
    def __init__(self, species:str, sound: str ): 
        self.species =str=species
        self.sound = str= sound
        self.age: int=0

    def __str__(self) -> str: # o toString é para transformar a classe/objeto
        #em texto, realizando toda a conversão
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy(self, increment:int)->None: # o def sempre inicializa uma variavel
       self.age += increment
       if self.age >=4:
           print (f"warning: {self.species} morreu")

    def makeSound(self)->str:
        if self.age ==0:
            return  "---"
        elif self.age==4:
            return "RIP"
        else:
            return self.sound
       





def main():
    animal= Animal("", "") # crio o objeto vazio para manipular com as entradas
    while True:#manter o usuario no loop para interagir com o animal
        line: str = input() #5 entrada de linha
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




