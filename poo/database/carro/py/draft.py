class Carro:
    def __init__(self):
        self.pass5: int = 0
        self.km : int = 0
        self.passMax : int = 2
        self.gas : int = 0
        self.gasMax : int = 100

    def __str__ (self) -> str:
           return (f"pass: {self.pass5}, gas: {self.gas}, km: {self.km}")
       
    def enter (self):
        self.pass5 += 1
        if self.pass5 > self.passMax:
            print ("fail: limite de pessoas atingido")
            self.pass5 = self.passMax
        
    def leave (self):
        if self.pass5 == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.pass5 -= 1

            
         
    def fuel (self, increment : int):
        self.gas += increment
        if self.gas > 100 :
           self.gas = 100


    def drive (self,distance: int)-> None:
         if self.pass5 == 0:
             print ("fail: nao ha ninguem no carro")
             return
         if self.gas == 0:
             print ("fail: tanque vazio")
             return
         if distance<= self.gas :
             self.km += distance
             self.gas -= distance


         else:
             kmandado =self.gas
             self.km += kmandado
             self.gas=0
             print (f"fail: tanque vazio apos andar {kmandado} km")



def main():
    carro = Carro()
    while True: 
        line : str = input()     
        print ("$" + line)  
        args : list [str] = line.split (" ")   
        if args [0]=="end":
            break
        if args [0]== "show":
            print (carro)
        if args [0]== "enter":
            carro.enter()
        if args [0] == "leave":
            carro.leave()
        if args[0] == "fuel":
         increment = int(args[1]) 
         carro.fuel(increment)
        if args [0] == "drive" :
            distance = int (args[1]) 
            carro.drive (distance)

main()            
