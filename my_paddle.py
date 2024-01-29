# Importa la clase Turtle del módulo turtle
from turtle import Turtle

# Define una clase llamada Paddle
class Paddle(Turtle):
    
    # El método __init__ se llama automáticamente cuando se crea un nuevo objeto de la clase Paddle
    def __init__(self, position_x):
        
        super().__init__()
        
        self.shape('square')

        # Levanta el lápiz para evitar dejar rastro al mover la paleta
        self.penup()

        # Cambia el color de la paleta a blanco
        self.color('white')
        
        # Ajusta el tamaño de la paleta
        self.shapesize(stretch_wid=1, stretch_len=5)
        
        # Ubica la paleta en la posición inicial dada por position_x
        self.goto(position_x, 0)    
        
        # Orienta la paleta verticalmente
        self.setheading(90)
        
        # self.paddle.pos()
        
    # Define un método para mover la paleta hacia arriba
    def paddle_movement_up(self):
        # Mueve la paleta hacia arriba
        self.forward(20)
    
    # Define un método para mover la paleta hacia abajo
    def paddle_movement_down(self):
        # Mueve la paleta hacia abajo
        self.backward(10)
