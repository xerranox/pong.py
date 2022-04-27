#Libreias
import turtle

#Ventana
ventana = turtle.Screen()
ventana.title("X Pong By: xerranox")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

#Puntuacion
puntuacion1 = 0
puntuacion2 = 0

#Copyright
Copyright = turtle.Turtle()
Copyright.speed(0)
Copyright.color("White")
Copyright.penup()
Copyright.hideturtle()
Copyright.goto(0, -290)
Copyright.write("       By: xerranox", align="left", font=("Courier", 25, "normal"))

#Jugador1
jugador1 = turtle.Turtle()
jugador1.speed(0)
jugador1.shape("square")
jugador1.color("white")
jugador1.penup()
jugador1.goto(-350, 0)
jugador1.shapesize(stretch_wid=5, stretch_len=1)

#Jugador2
jugador2 = turtle.Turtle()
jugador2.speed(0)
jugador2.shape("square")
jugador2.color("white")
jugador2.penup()
jugador2.goto(350, 0)
jugador2.shapesize(stretch_wid=5, stretch_len=1)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)

#Velocidad de la pelota
pelota.dx = 0.1
pelota.dy = 0.1

#Marcador
punt = turtle.Turtle()
punt.speed(0)
punt.color("white")
punt.penup()
punt.hideturtle()
punt.goto(0, 260)
punt.write("Jugador 1: 0 || Jugador 2: 0", align="center", font=("Courier", 25, "normal"))

#Movimiento de la pala
def jugador1_up():
	y = jugador1.ycor()
	y += 20
	jugador1.sety(y)

def jugador1_down():
	y = jugador1.ycor()
	y -= 20
	jugador1.sety(y)

def jugador2_up():
	y = jugador2.ycor()
	y += 20
	jugador2.sety(y)

def jugador2_down():
	y = jugador2.ycor()
	y -= 20
	jugador2.sety(y)

#Teclado
ventana.listen()
ventana.onkeypress(jugador1_up, "w")
ventana.onkeypress(jugador1_down, "s")
ventana.onkeypress(jugador2_up, "Up")
ventana.onkeypress(jugador2_down, "Down")

#Juego
while True:
	ventana.update()

	pelota.setx(pelota.xcor() + pelota.dx)
	pelota.sety(pelota.ycor() + pelota.dy)

	#Choque pared
	if pelota.ycor() > 290:
		pelota.dy *= -1
	if pelota.ycor() < -290:
		pelota.dy *= -1

	if pelota.xcor() > 390:
		pelota.goto(0,0)
		pelota.dx *= -1
		puntuacion1 += 1
		punt.clear()
		punt.write(f"Jugador 1: {puntuacion1} ||Jugador 2: {puntuacion2}", align="center", font=("Courier", 25, "normal"))

	if pelota.xcor() < -390:
		pelota.goto(0,0)
		pelota.dx *= -1
		puntuacion2 += 1
		punt.clear()
		punt.write(f"Jugador 1: {puntuacion1} ||Jugador 2: {puntuacion2}", align="center", font=("Courier", 25, "normal"))

	#Choque pala
	if ((pelota.xcor() > 340 and pelota.xcor() < 350)
			and (pelota.ycor() < jugador2.ycor() + 50
			and pelota.ycor() > jugador2.ycor() - 50)):
		pelota.dx *= -1

	if ((pelota.xcor() < -340 and pelota.xcor() > -350)
			and (pelota.ycor() < jugador1.ycor() + 50
			and pelota.ycor() > jugador1.ycor() - 50)):
		pelota.dx *= -1