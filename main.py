# Importa las clases Turtle y Screen del módulo turtle
from turtle import Turtle, Screen

# Importa la clase Paddle del módulo my_paddle
from my_paddle import Paddle

from ball import Ball

from my_score import Score
# Crea un objeto de la clase Screen
screen = Screen()

# Configura el tamaño de la pantalla a 800 de ancho y 600 de alto
screen.setup(width=800, height=600)

# Cambia el color de fondo de la pantalla a negro
screen.bgcolor("black")

# Cambia el título de la ventana a "PONG game"
screen.title("PONG game")

# Desactiva la animación automática
screen.tracer(0)

# Crea un objeto de la clase Paddle para el paddle derecho en la posición x=350
paddle_right = Paddle(position_x=350)

# Crea un objeto de la clase Paddle para el paddle izquierdo en la posición x=-350
paddle_left = Paddle(position_x=-350)

#creamos objeto de la clase ball
ball=Ball()


# # Actualiza la pantalla para mostrar los objetos paddle_right y paddle_left
screen.update()

# Reactiva la animación automática
screen.tracer(1)

# La función listen() hace que la pantalla comience a escuchar los eventos del teclado
screen.listen()

# La función onkey() registra una función para que se llame cuando se presiona una tecla específica
# En este caso, cuando se presiona la tecla "Up", se llama al método paddle_movement_up del objeto paddle_right
screen.onkey(paddle_right.paddle_movement_up, "Up")

# Cuando se presiona la tecla "Down", se llama al método paddle_movement_down del objeto paddle_right
screen.onkey(paddle_right.paddle_movement_down, "Down")

# La función onkey() registra una función para que se llame cuando se presiona una tecla específica
# En este caso, cuando se presiona la tecla "w", se llama al método paddle_movement_up del objeto paddle_left
screen.onkey(paddle_left.paddle_movement_up, "w")

# Cuando se presiona la tecla "s", se llama al método paddle_movement_down del objeto paddle_left
screen.onkey(paddle_left.paddle_movement_down, "s")

game_is_on=True



screen.tracer(1)

#TODO Crear la clase score que herede de turtle, para registrar los puntajes de los jugadores

#Nuestra clase score recibe como parametro la posicionx y posiciony del objeto turtle
score_left=Score(-100,230)

score_right=Score(100,230)


print(f'la velocidad inciial es {ball.speedy}')

while game_is_on:  
    #llamamos a la funcion que controla el movimiento de la pelota
    ball.movement() 
    
    
    #TODO:DETECT COLLISION WITH THE WALL
    # Si la bola choca con la parte superior o inferior de la pantalla.    
    if ball.ycor() > 280 or ball.ycor() < -275:  
        
        # Desactiva la animación automática para evitar parpadeos.
        screen.tracer(0) 
        
        
        # Cambia la dirección de la bola cuando choca con la pared.
        ball.change_direction()  
        
        # Reactiva la animación automática.
        screen.tracer(1)  
        
    #TODO:DETECTAR EL CHOQUE DE LA PELOTA CON LAS RAQUETAS
    #distance() mide la distancia de mi ball hasta el centro de la paddle
  
    if ball.xcor() > 320 and ball.distance(paddle_right)<60 or ball.xcor() < -320 and ball.distance(paddle_left)<60:  
        
        # Desactiva la animación automática para evitar parpadeos.
        screen.tracer(0) 
             
        
        # Cambia la dirección de la bola cuando choca con una paleta.
        ball.change_direction_2() 
        
        # Reactiva la animación automática.
        screen.tracer(1) 
        
        #funcion que aumenta la velocidad de la ball
        ball.increase_speedy()
        
        print(f'la velocidad actual es {ball.speedy}')
        # print(ball.pos())
        # print(ball.distance(paddle_right))
    
    
    #TODO: DETECTAR CUANDO LA BOLA NO TOCA LA RAQUETA Y SE VA POR LOS LADOS    
    # Si la bola se sale de la pantalla por los lados.    
    elif ball.xcor() > 330:
        # Desactiva la animación automática para evitar parpadeos.
        screen.tracer(0) 
        
        #OTRA FORMA DE RESETAR LA PELOTA EN EL CENTRO CUANDO  LA RAQUETA NO GOLPEA LA PELOTA Y SE SALE POR LOS LADOS
        ball.reset_position()
        
        #si la ball se sale por la derecha el jugador de la izq anota un punto
        score_left.add_score() 
        
        # Reactiva la animación automática.
        screen.tracer(1)  
    
    
    elif ball.xcor() < -330: 
        #OTRA FORMA DE RESETAR LA PELOTA EN EL CENTRO CUANDO  LA RAQUETA NO GOLPEA LA PELOTA Y SE SALE POR LOS LADOS
        
        
        # Resetea la posición de la bola.
        ball.reset() 
        
        # Desactiva la animación automática para evitar parpadeos. 
        screen.tracer(0)  
        
        # Crea una nueva bola.
        ball=Ball()  
        
        #si la ball se sale por la izq el jugador de la derecha anota un punto
        score_right.add_score()
        # Reactiva la animación automática.
        screen.tracer(1)  
    
    
    #TODO: ESCOGEMOS GANADOR, EL PRIMER JUGADOR EN COMPLETAR 100 PUNTOS GANA    
    if score_left.score ==100:
        
        #la clase ball hereda de la clase turtle, por lo que usando la funcion hideturtle escondemos la ball
        ball.hideturtle()
        
        #mostramos un msj indicando que el jugador de la izq ha ganado
        score_left.end_game(0, 0,  winner= 'left player')
        
        #se finaliza el juego al haber un ganador
        game_is_on=False
        
    elif score_right.score ==100:
        
        #la clase ball hereda de la clase turtle, por lo que usando la funcion hideturtle escondemos la ball
        ball.hideturtle()
        
        #mostramos un msj indicando que el jugador de la izq ha ganado
        score_right.end_game(0, 0,  winner= 'right player')
        
        #se finaliza el juego al haber un ganador
        game_is_on=False
    
    
    
    



# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Cierra la ventana al hacer click en la pantalla
screen.exitonclick()    