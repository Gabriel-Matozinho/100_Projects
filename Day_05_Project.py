import random

# Lista com todo o alfabeto
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Lista com os números de 0 a 9
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Lista com os símbolos e caracteres do teclado
simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
            '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>',
            '/', '?', '`', '~']

password = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password\n"))
# nr_symbols = int(input("How many symbols would you like\n"))
# nr_numbers = int(input("How many numbers would you like\n"))

for nr_letters in letras:
    random.choice(password(letras.append))
print(password)
