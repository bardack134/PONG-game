# Importa la clase Turtle del módulo turtle
from turtle import Turtle

# Define una clase llamada Paddle
class Paddle():
    
    # El método __init__ se llama automáticamente cuando se crea un nuevo objeto de la clase Paddle
    def __init__(self, position_x):
        # Crea un objeto Turtle para representar la paleta
        self.paddle = Turtle('square')

        # Levanta el lápiz para evitar dejar rastro al mover la paleta
        self.paddle.penup()

        # Cambia el color de la paleta a blanco
        self.paddle.color('white')
        
        # Ajusta el tamaño de la paleta
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        
        # Ubica la paleta en la posición inicial dada por position_x
        self.paddle.goto(position_x, 0)    
        
        # Orienta la paleta verticalmente
        self.paddle.setheading(90)
        
    # Define un método para mover la paleta hacia arriba
    def paddle_movement_up(self):
        # Mueve la paleta hacia arriba
        self.paddle.forward(20)
    
    # Define un método para mover la paleta hacia abajo
    def paddle_movement_down(self):
        # Mueve la paleta hacia abajo
        self.paddle.backward(20)
