import turtle as t

#Funciones de movimiento de la tortuga
#Variables

rotation_value = 5
movement_value = 10
#Variables de botones

rotate_right_button = "d"
rotate_left_button = "a"
forward_button = "w"
back_button = "s"
up_button = "Up"
down_button = "Down"
right_button = "Right"
left_button = "Left"
up_right_button = "e"
up_left_button = "q"
down_right_button = "c"
down_left_button = "z"
set_movement_value_button = "m"
set_rotation_value_button = "r"
set_pen_color_button = "t"
set_pen_size_button = "y"
undo_button = "u"
clear_page_button = "p"
up_or_down_pen_button = "space"


# funciones usadas en codigo

def actual_position()->str:
    return f"Posiciones X:{t.xcor()} Y: {t.ycor()}"

def actual_angle()->str:
    return f"La rotación ahora es de: {t.heading()}° Grados"

# funciones
def undo()->None:
    t.undo()
    print("Se ha deshecho el último movimiento")
    print(actual_position())
    print(actual_angle())

def clear_page()->None:
    t.clear()
    print("Se ha limpiado la pantalla")
    print(actual_position())
    print(actual_angle())

#funciones del pincel

def pen_up_or_down(): 
    if t.isdown():
        t.penup()
    else:
        t.pendown()

    print(actual_position())
    print(actual_angle())

    t.listen()
    return

def set_pen_color():
    color = t.textinput("Color","Porfavor indica el color que quieres en ingles y en minusculas \nTambien puedes usar un codigo hexadecimal poniendo '#' al principio seguido de codigo")
    try:
        t.pencolor(color)
    except:
        print(f"Error color: '{color}' no válido")
    t.listen()

def set_pen_size():
    pen_size = t.numinput("Tamaño pincel","Porfavor ingresa un numero con el tamaño del pince que deseas")
    try:
        if pen_size <= 0:
            t.listen()
            return
    except:
        if pen_size == None:
            t.listen()
            return
    t.pensize(pen_size)
    t.listen()

# establecer valores

def set_movement_value():
    global movement_value
    print(movement_value)
    new_movement_value = t.numinput(title="Valor De Movimiento",prompt="Porfavor ingrese el valor de movimiento de la tortuga, el valor predeterminado es 10 pixeles",default=10)
    if new_movement_value != None:
        movement_value = new_movement_value
    print(movement_value)
    t.listen()

def set_rotation_value():
    global rotation_value
    print(rotation_value)
    new_rotation_value = t.numinput(title="Valor De Rotación",prompt="Porfavor ingrese el valor de rotación de la tortuga, el valor predeterminado es 5 pixeles",default=5)
    if new_rotation_value != None:
        rotation_value = new_rotation_value
    print(rotation_value)
    t.listen()


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
    t.goto(t.xcor()+movement_value,t.ycor()+movement_value)
    print(actual_position())

def move_up_left() -> None:
    t.goto(t.xcor()-movement_value,t.ycor()+movement_value)
    print(actual_position())

def move_down_right() -> None:
    t.goto(t.xcor()+movement_value,t.ycor()-movement_value)
    print(actual_position())

def move_down_left() -> None:
    t.goto(t.xcor()-movement_value,t.ycor()-movement_value)
    print(actual_position())