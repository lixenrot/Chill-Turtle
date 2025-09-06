import turtle as t
import Turtle_buttons_and_functions as tf
import Turtle_Properties as tp


#1 Valores de la pantalla

t.setup(1.0,1.0,0,0)

#2 Propiedades De La Tortuga

t.speed(tp.speed)
t.shape(tp.shape)
t.resizemode(tp.resize_mode)
t.shapesize(*tp.shape_size)
t.color(tp.shape_color)

#3 propiedades del lapiz

t.pensize(3)
t.pencolor("#ff2acd") #el color del lapiz es diferente al de la tortuga

#4 funciones de la tortuga

t.onscreenclick(t.goto)

#5 movimiento de la tortuga

t.onkeypress(tf.right_rotation, tf.rotate_right_button)
t.onkeypress(tf.left_rotation, tf.rotate_left_button)
t.onkeypress(tf.move_forward, tf.forward_button)
t.onkeypress(tf.move_back, tf.back_button)
t.onkeypress(tf.move_up, tf.up_button)
t.onkeypress(tf.move_down, tf.down_button)
t.onkeypress(tf.move_left, tf.left_button)
t.onkeypress(tf.move_right, tf.right_button)
t.onkeypress(tf.move_up_right, tf.up_right_button)
t.onkeypress(tf.move_up_left, tf.up_left_button)
t.onkeypress(tf.move_down_right, tf.down_right_button)
t.onkeypress(tf.move_down_left, tf.down_left_button)
t.onkeypress(tf.undo, tf.undo_button)
t.onkeypress(tf.increase_movement_value, tf.increase_movement_button)
t.onkeypress(tf.increase_rotation_value, tf.increase_rotation_button)
t.onkeypress(tf.decrease_movement_value, tf.decrease_movement_button)
t.onkeypress(tf.decrease_rotation_value, tf.decrease_rotation_button)













t.listen()
t.mainloop()