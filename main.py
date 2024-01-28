from turtle import Turtle, Screen

from my_paddle_left import Paddle_left

from my_paddle_right import Paddle_right

# Crea un objeto de la clase Screen
screen = Screen()

# Configura el tamaño de la pantalla a 800 de ancho y 600 de alto
screen.setup(width=800, height=600)

# Cambia el color de fondo de la pantalla a negro
screen.bgcolor("black")

# Cambia el título de la ventana a "PONG game"
screen.title("PONG game")

# Configuramos el rastreo de animación en 0 para desactivar las actualizaciones automáticas
screen.tracer(0)

# Creamos un objeto de la clase paddle_right en my_paddle_right.py
paddle_right = Paddle_right()

# Creamos un objeto de la clase paddle_left en my_paddle_left.py
paddle_left = Paddle_left()

# Actualizamos la pantalla para mostrar el objeto paddle_right
screen.update()

# Restauramos el rastreo de animación a 1 para activar las actualizaciones automáticas
screen.tracer(1)

# La función listen() hace que la pantalla comience a escuchar los eventos del teclado
screen.listen()

# La función onkey() registra una función para que se llame cuando se presiona una tecla específica
# En este caso, cuando se presiona la tecla "Up", se llama al método paddle_movement_up 
screen.onkey(paddle_right.paddle_movement_up, "Up")

# Cuando se presiona la tecla "Down", se llama al método paddle_movement_down
screen.onkey(paddle_right.paddle_movement_down, "Down")

# La función onkey() registra una función para que se llame cuando se presiona una tecla específica
# En este caso, cuando se presiona la tecla "Up", se llama al método paddle_movement_up 
screen.onkey(paddle_left.paddle_movement_up, "w")

# Cuando se presiona la tecla "Down", se llama al método paddle_movement_down
screen.onkey(paddle_left.paddle_movement_down, "s")

# Permite que el programa continúe ejecutándose hasta que hagamos clic en la pantalla
# Debemos crear un objeto de la clase Screen() para usar el método exitonclick()
# Cierra la ventana al hacer clic en la pantalla
screen.exitonclick()
