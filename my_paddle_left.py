from turtle import Turtle

class Paddle_left():
    
    def __init__(self):
        # Crea un objeto Turtle para representar la paleta derecha
        self.paddle = Turtle('square')

        # Levanta el lápiz para evitar dejar rastro al mover la paleta
        self.paddle.penup()

        # Cambia el color de la paleta a blanco
        self.paddle.color('white')
        
        # Ajusta el tamaño de la paleta
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        
        # Ubica la paleta en la posición inicial en el lado derecho de la pantalla
        self.paddle.goto(-350, 0)    
        
        
        # Orienta la paleta verticalmente
        self.paddle.setheading(90)
        
    def paddle_movement_up(self):
        # Mueve la paleta hacia arriba
        self.paddle.forward(20)
    
    def paddle_movement_down(self):
        # Mueve la paleta hacia abajo
        self.paddle.backward(20)

       
   
            

            
        
        
        
        
        
            
            
           
            