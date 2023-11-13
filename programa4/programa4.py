import random
import modulos

# bot = random.randint(0, 1)

# if bot == 0:
#     lado = "cara"
# else:
#     lado = "cruz"

# decision = input("Elige entre cara o cruz: ")

# if decision == lado:
#     print("HA SALIDOOOOOOOOO" + " " + lado)
#     print("HAS GANADO")
# else:
#     print("HA SALIDOOOOOOOOO" + " " + lado)
#     print("HAS PERDIDO")

nombres = ["Jorge", "Irene", "Saiko", "Rolly"]

bot = random.choice(nombres)

print(f"Hoy paga la cuenta {bot}")

