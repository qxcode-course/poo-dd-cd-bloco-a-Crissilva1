class Calculadora:
      def __init__(self, batteryMax:int):
        self.batteryMax = batteryMax
        self.battery = 0
        self.display = 0.0
      
      def __str__ (self) -> str:
            return f"display = {self.display:.2f}, battery = {self.battery}"

      def charge (self, increment:int):
          if self.battery < self.batteryMax: 
             self.battery += increment
             if self.battery > self.batteryMax:# aqui verifica se a bateria passou do limite após o incremento
              self.battery = self.batteryMax # se sim, aqui freia e diz que deve estar no limite. 

      def sum (self, a:int , b:int):
            if self.battery ==0:
               print ("fail: bateria insuficiente")
            else:
               self.display = a + b
               self.battery -= 1 

      def div (self, a :int , b:int):
           if self.battery ==0:
               print ("fail: bateria insuficiente")
           elif b== 0 :
               print ("fail: divisao por zero")  
               self.battery -= 1
           else:
                 self.display = a / b
                 self.battery -= 1  

def main ():
    calculadora=None
    while True:
     line:str=input()
     print ("$" + line) #eco
     args: list[str]=line.split(" ") 
     if args [0]=="end":
            break
     if args [0] == "init":
         calculadora= Calculadora (int(args[1]))           
     if args [0] == "show":
         print (calculadora)
     if args[0] == "sum":
            calculadora.sum(int(args[1]), int(args[2]))
     if args [0] == "charge":
        calculadora.charge(int (args [1] ))
     if args [0] == "div":
        calculadora.div (int(args[1]), int(args[2]))
    

main ()         

              


               

   
           
            
               
         
      

      
      