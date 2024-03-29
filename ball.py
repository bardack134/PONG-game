import random
from turtle import Turtle
# Define los ángulos de movimiento posibles para la bola.
BALL_MOVEMENT_RIGHT = [45,  -45]
BALL_MOVEMENT_LEFT = [135,  225]
# BALL_MOVEMENT = [45]  #esta linea es para pruebas

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()  # Inicializa la clase padre, que es Turtle.
        
        self.color('white')  # Establece el color de la bola a blanco.
        
        self.shape('square')  # Establece la forma de la bola a cuadrado.
        
        self.penup()  # Levanta el lápiz para que no se dibuje una línea cuando la bola se mueve.
        
        self.setheading(random.choice(BALL_MOVEMENT_RIGHT))  # Establece la dirección inicial de la bola a un ángulo aleatorio.
        # self.setheading(-45)
         
        print(self.heading()) 
         
        self.speed('normal')  # Establece la velocidad de la bola a la más lenta.
        
        self.speedy=2 #variable que determina la velocidad de la bola
    def movement(self):
        self.forward(self.speedy)# Mueve la bola hacia adelante en su dirección actual y define la velocidad de movimiento de la bola  
        
    
    #funcion que aumenta la velocidad de la ball
    def increase_speedy(self):
        self.speedy += 1 #aumentamos la velocidad de la ball en 1 
        
        self.forward(self.speedy)
        
    #cambia la direccion de la ball cuando esta choca la pared
    # x ejemplo el angulo de rebote seria -45, si choco con la pared con un angulo de 45
    def change_direction(self):
        # Obtiene la dirección actual de la bola.
        heading=self.heading()  
        
        # Cambia la dirección de la bola al ángulo opuesto.
        self.setheading(-1*int(heading))  
        
        # Mueve la bola hacia adelante en su nueva dirección.
        self.forward(10)  
        
        
    #cambia la posicion de la ball cuando esta chocka la raqueta derecha 
    def change_direction_2(self):
        
        # Obtiene la dirección actual de la bola.
        heading=self.heading()  
        
        if heading==315:
            # Si la bola se dirige hacia la raqueta de la derecha con un angulo de  315 grados, cambia su dirección a 225 grados.
            self.setheading(int(heading)+-90)  
            
            # Mueve la bola hacia adelante en su nueva dirección.
            self.forward(10)  
           
            
        if heading==45:
            # Si la bola se dirige hacia la raqueta derecha con un angulo de 45 grados, cambia su dirección 90
            self.setheading(int(heading)+90)  
            
            self.forward(10)  # Mueve la bola hacia adelante en su nueva dirección.
            
        if heading==225:
            # Si la bola se dirige hacia la raqueta de la izq con un angulo de entrada de 225 grados, cambia su dirección 90 grados
            self.setheading(int(heading)+90)  
            
            self.forward(10)  # Mueve la bola hacia adelante en su nueva dirección.
            
        if heading==135:
            # Si la bola se dirige hacia la raqueta de la izq con un angulo de entrada de 135 grados, cambia su dirección restando 90 grados
            self.setheading(int(heading)-90)  
            
            self.forward(10)  # Mueve la bola hacia adelante en su nueva dirección.
            
    
    def reset_position(self):
        # Establece la velocidad de la tortuga como la más rápida para ocultarla y moverla rápidamente
        self.speed('fastest')
        
        # Oculta la tortuga temporalmente mientras se mueve a la posición inicial
        self.hideturtle()
        
        # Mueve la tortuga a la posición (0, 0)
        self.goto(0, 0)
        
        # Muestra la tortuga después de moverla a la posición inicial
        self.showturtle()
        
        # Establece la velocidad de la tortuga como la más lenta para mostrar el movimiento suavemente
        self.speed('slowest')
        
        #Cuando la bola sale del lado derecho del jugador y se reinicia en la posición (0, 0), quiero que la bola comience en
        # dirección contraria es decir hacia el jugador de la izq"
        self.setheading(random.choice(BALL_MOVEMENT_LEFT))  
        
        
        
        
        print(self.heading()) 