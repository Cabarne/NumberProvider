from random import randint
from time import sleep

class NumberProvider: 
    def __init__(self,min=-100,max=100): 
        if type(min) != int and type(max) != int:
            print ("ERROR")
        else:
            self.min = min
            self.max = max

    def generate(self):
        return randint(self.min,self.max)

    def whenPositive(self, positiveCB):
        self.positiveCB = positiveCB
        
    def whenNegative(self, negativCB):
        self.negativCB = negativCB
        
    def start (self):
        while True:
            number = self.generate()
            if number >= 0:
                self.positiveCB(number)              
            if number < 0:
                self.negativCB(number)   
            sleep(1)