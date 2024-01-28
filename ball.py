from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        
        super().__init__()
        
        self.color('white')
        
        self.shape('square')
        
        self.penup()
        
        #TODO: Cambiar despues para que la posicion en la que empiezaq la pelota sea aleatoria
        self.setheading(45)
        
        self.speed('slowest')
        
    def movement(self):
        self.forward(10)  