from turtle import Turtle

# Constantes que definen características del programa como tipo de letra y tamaño de letra.
# Se colocan aquí por si se desean modificar en el futuro sin tener que buscarlas dentro del código.
ALIGMENT = 'center'  # Alineación del texto en el centro.

FONT = ('Courier', 42, 'bold')  # Tipo de fuente, tamaño y estilo del texto.

class Score(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        
        # Configuración inicial de la clase Score
        # Color del texto.
        self.color('white') 
        
        # Oculta la tortuga.
        self.hideturtle()  
        
         # Levanta el lápiz.
        self.penup() 
        
        # Establece la posición inicial del marcador.
        self.setposition(position_x, position_y)  
        
        # Inicializa el puntaje en cero.
        self.score = 0 
        
        self.update_scoreboard()
         
    # Método para actualizar el marcador en la pantalla
    def update_scoreboard(self):
        # Borra el dibujo de la tortuga de la pantalla. No mueve la tortuga.
        # El estado y posición de la tortuga así como los todos los dibujos de las otras tortugas no son afectados.
        self.clear() 
        
        # Escribe el puntaje actual en la pantalla utilizando la fuente y alineación definidas.
        self.write(f"{self.score}", False, align=ALIGMENT, font=FONT)         
        
        
    # Método para sumar puntaje
    def add_score(self):  
        # Limpia el marcador actual.  
        self.clear()  
        
        # Incrementa el puntaje en 10.
        self.score += 10  
        
        # Actualiza el marcador en la pantalla.
        self.update_scoreboard()  
    
    #funcion de findel juego y muestra mensaje indicando el ganador    
    def end_game(self, position_x, position_y, winner):
        
             
        # Establece la posición inicial de la tortuga.
        self.setposition(position_x, position_y)  
         

        # Color del texto.
        self.color('white') 
        
        # Escribe el ganador del juego en la pantalla, el jugador se pasa como parametro 'winner' utilizando la fuente y alineación definidas.
        self.write(f"{winner} is the winner", False, align=ALIGMENT, font=('Courier', 20, 'bold'))  