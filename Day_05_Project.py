import random  # Importa o módulo random para gerar elementos aleatórios

# Lista com todas as letras maiúsculas e minúsculas
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Lista com os números de 0 a 9
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Lista com os símbolos e caracteres do teclado
simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
            '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>',
            '/', '?', '`', '~']

'''
Easy model: Gera uma senha de forma simples concatenando as escolhas aleatórias

print('Welcome to the PyPassword Generator!')
nr_letras = int(input('How many letters would you like in your password?\n'))  # Recebe o número de letras
nr_simbolos = int(input('How many symbols would you like?\n'))  # Recebe o número de símbolos
nr_numeros = int(input('How many numbers would you like?\n'))  # Recebe o número de números

password = ''  # Inicializa uma string vazia para construir a senha

# Adiciona letras aleatórias à senha
for char in range(0, nr_letras):
    password += random.choice(letras)

# Adiciona símbolos aleatórios à senha
for char in range(0, nr_simbolos):
    password += random.choice(simbolos)

# Adiciona números aleatórios à senha
for char in range(0, nr_numeros):
    password += random.choice(numeros)

print(password)  # Imprime a senha gerada
'''

# Hard model: Gera uma senha com elementos aleatórios e embaralha a ordem

password_list = []  # Inicializa uma lista vazia para armazenar os caracteres da senha

print('Welcome to the PyPassword Generator!')
# Recebe o número de letras
nr_letras = int(input('How many letters would you like in your password?\n'))
nr_simbolos = int(input('How many symbols would you like?\n')
                  )  # Recebe o número de símbolos
nr_numeros = int(input('How many numbers would you like?\n')
                 )  # Recebe o número de números

# Adiciona letras aleatórias à lista
for char in range(0, nr_letras):
    password_list.append(random.choice(letras))

# Adiciona símbolos aleatórios à lista
for char in range(0, nr_simbolos):
    password_list.append(random.choice(simbolos))

# Adiciona números aleatórios à lista
for char in range(0, nr_numeros):
    password_list.append(random.choice(numeros))

print(password_list)  # Imprime a lista de caracteres antes de embaralhar
random.shuffle(password_list)  # Embaralha a ordem dos caracteres na lista
print(password_list)  # Imprime a lista de caracteres após o embaralhamento

# Concatena os caracteres da lista em uma string final
password = ''
for char in password_list:
    password += char

print(f'Your password is: {password}')  # Imprime a senha final
