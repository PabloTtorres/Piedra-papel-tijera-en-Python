import random
import time 
 
while True:
  mano = ["Piedra,", "Papel", "Tijera"]
  x = random.randint(0,2)


  print("Pierda papel o tijera")
  time.sleep(1)
  print("0 = piedra")
  print("1 = papel")
  print("2 = tijera")
  time.sleep(1)
  print("1, 2, 3")
  time.sleep(2)
  print("Afuera!")
  mano2 = int(input())
  ia = ""

  if mano2 == 0:
    eleccion = "Piedra"
  elif mano2 == 1:
    eleccion = "Papel"
  elif mano2 == 2:
    eleccion = "Tijera"
  print("Tu eleccion es", eleccion)

  if x == 0:
    ia = "Piedra"
  elif x == 1:
    ia = "Papel"
  elif x == 2:
    ia = "Tijera"
  print("La computadora elijio", ia)
  time.sleep(1)
  print("...")

  if eleccion == "Piedra" and ia == "Papel":
    print("Perdiste!")
  elif eleccion == "Papel" and ia == "Tijera":
    print("Perdiste!")
  elif eleccion == "Piedra" and ia == "Tijera":
    print("Ganaste!")
  elif eleccion == "Papel" and ia == "Piedra":
    print("Ganaste")
  elif eleccion == "Tijera" and ia == "Papel":
    print("Ganaste")
  elif eleccion == "Tijera" and ia == "Piedra":
    print("Perdiste!")
  elif eleccion == ia:
    print("Empate")

  jn = input("Quieres jugar de nuevo? y/n  ")
  if jn.lower() != "y":
    break
