import random

def run_game():
  lives = 6
  print("*" * 40)
  print("Bienvenido al juego de Adivinanzas")
  print("*" * 40)

  print("lives", lives)
  print("*" * 10)

  return options_game(lives)

def options_game(lives):
  number = (input("Regalame un número por favor => "))
  number = int(number)
  number_1 = (input("Regalame otro número por favor => "))
  number_1 = int(number_1)

  machine = random.randint(number, number_1)

  return options_2(number, number_1, lives, machine)

def options_2(number, number_1, lives, machine):

  guess = (input(f"Adivina el número que elegí yo entre {number} y {number_1} => "))  
  if not guess:
    print("No es un numero")
  else:
    guess = int(guess)    

  guess = rules(lives, guess, machine, number, number_1)

while True:  
  def rules(lives, guess, machine, number, number_1):
    lives -=1
    if guess > number and guess > number_1:
      print(f"Error coloca un numero entre {number} y {number_1}")
      print("*" * 40)
      print("lives", lives)
      return options_2(number, number_1, lives, machine)

    if guess < number_1 and guess < number:
      print(f"Error coloca un numero entre {number} y {number_1}")
      print("*" * 40)
      print("lives", lives)
      return options_2(number, number_1, lives, machine)

    elif lives == 0:
      print("Lo siento, has perdido el nùmero es ", machine)
      print("*" * 40)
      return final()

    elif guess == machine:
      print(f"Felicidades, adivinaste el numero es {machine}")
      print("*" * 40)
      print("lives", lives)
      return final()

    elif guess > machine:
      print("El numero es menor")
      print("*" * 40)
      print("lives", lives)
      options_2(number, number_1, lives, machine)

    elif guess < machine:
      print("El numero es mayor")
      print("*" * 40)
      print("lives", lives)
      options_2(number, number_1, lives, machine)

  def final():
    user = input("¿Quieres jugar de nuevo? (S/N) => ")
    user = user.upper()

    if user == "S":
      run_game()
    elif user == "N":
      print("Gracias por jugar")

  break
run_game()
