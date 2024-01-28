import random
from turtle import Turtle

BALL_MOVEMENT = [45, -45]

class Ball(Turtle):
    
    def __init__(self):
        
        super().__init__()
        
        self.color('white')
        
        self.shape('square')
        
        self.penup()
        
              
        #TODO: Cambiar despues para que la posicion en la que empiezaq la pelota sea aleatoria
        self.setheading(random.choice(BALL_MOVEMENT))
        # self.setheading(-45)
         
        self.speed('slowest')
        
    def movement(self):
        self.forward(10)  
        
    
    def change_direction(self):
        heading=self.heading() 
        self.setheading(-1*int(heading))    
        self.forward(10)