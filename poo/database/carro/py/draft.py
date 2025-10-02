class drive:
    def __init__(self):
       self.pass3: int = 0
       self.km: int = 0
       self.passMax: int = 2
       self.gas : int = 0
       self.gasMax : int = 100

    def __str__ (self) -> str:
           return (f"passagem:{self.pass3}, gas:{self.gas}, kilometro:{self.km}")
       
    def enter (self, enter:int)-> None :
        self.passMax +=1
        if self.passMax > 2:
           self.passMax = 2
           return 
        
    def leave (self,leave :int)-> None:
        self.passMax -=2
        if self.pass
