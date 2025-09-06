import turtle as t

#Funciones de movimiento de la tortuga
#Variables

rotation_value = 5
movement_value = 10

#Variables de botones

rotate_right_button = "Right"
rotate_left_button = "Left"
forward_button = "Up"
back_button = "Down"
up_button = "w"
down_button = "s"
right_button = "d"
left_button = "a"
up_right_button = "e" 
up_left_button = "q"
down_right_button = "c"
down_left_button = "z"
increase_movement_button = "i"
increase_rotation_button = "o"
decrease_rotation_button = "l"
decrease_movement_button = "k"
undo_button = "u"

#Funciones

def actual_position()->str:
    return f"Posiciones X:{t.xcor()} Y: {t.ycor()}"

def actual_angle()->str:
    return f"La rotación ahora es de: {t.heading()}° Grados"

def undo()->None:
    t.undo()
    print("Se ha deshecho el último movimiento")
    print(actual_position())
    print(actual_angle())
    
#Aumentar-disminuir Variables

def increase_rotation_value()->None:
    global rotation_value
    rotation_value += 1
    print(f"El valor de la rotación es: {rotation_value}")

def increase_movement_value()->None:
    global movement_value
    movement_value += 1
    print(f"El valor del movimiento es: {movement_value} ")

def decrease_movement_value()->None:
    global movement_value
    movement_value -= 1
    print(f"El valor del movimiento es: {movement_value} ")

def decrease_rotation_value()->None:
    global rotation_value
    rotation_value -= 1
    print(f"El valor de la rotación es: {rotation_value}")

#rotaciones

def right_rotation()-> None:
    t.right(rotation_value)
    print(actual_angle())


def left_rotation()-> None:
    t.left(rotation_value)
    print(actual_angle())

#movimientos sin eje fijo

def move_forward()-> None:
    t.forward(movement_value)
    print(actual_position())

def move_back ()-> None:
    t.back(movement_value)
    print(actual_position())

#movimientos RIGHT,LEFT,UP,DOWN (EJE FIJO)

def move_right()-> None:
    t.setx(t.xcor() + movement_value)
    print(actual_position())

def move_left ()-> None:
    t.setx(t.xcor() - movement_value)
    print(actual_position())

def move_up()-> None:
    t.sety(t.ycor() + movement_value)
    print(actual_position())

def move_down()-> None:
    t.sety(t.ycor() - movement_value)
    print(actual_position())

#movimiento diagonal

def move_up_right() -> None:
    t.setx(t.xcor() + movement_value)
    t.sety(t.ycor() + movement_value)
    print(actual_position())

def move_up_left() -> None:
    t.setx(t.xcor() - movement_value)
    t.sety(t.ycor() + movement_value)
    print(actual_position())

def move_down_right() -> None:
    t.setx(t.xcor() + movement_value)
    t.sety(t.ycor() - movement_value)
    print(actual_position())

def move_down_left() -> None:
    t.setx(t.xcor() - movement_value)
    t.sety(t.ycor() - movement_value)
    print(actual_position())

