# Importa las clases Turtle y Screen del módulo turtle
from turtle import Turtle, Screen

# Importa la clase Paddle del módulo my_paddle
from my_paddle import Paddle

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

# Actualiza la pantalla para mostrar los objetos paddle_right y paddle_left
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

# Permite que el programa continúe ejecutándose hasta que hagamos clic en la pantalla
# Cierra la ventana al hacer clic en la pantalla
screen.exitonclick()
