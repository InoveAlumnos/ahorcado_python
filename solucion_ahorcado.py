# Python Inicial [Python]
# Ejercicio integrador

# Autor: Inove Coding School
# Version: 2.0

# Importamos módulos y librerías necesarias.
import interfaz
import csv


# Defino una constante global con la cantidad
# máxima de intentos.
MAX_CANT_INTENTOS = 7


def get_palabras_secretas(csvfilename):
    '''
    Lee las palabras secretas presentes
    en un archivo csv y las retorna
    como una lista de diccionarios.
    '''
    with open(csvfilename, 'r') as csvfile:
        data = list(csv.DictReader(csvfile))
    return data


def verificar_letra(letra, palabra):
    '''
    Función que verifica si la letra
    pertenece a la palabra a adivinar.
    '''
    if letra in palabra:
        return True
    else:
        return False


def get_letra():
    '''
    Función que permite ingresar una letra
    por consola y la retorna.
    '''
    letra = str(input('Ingresar una letra: ')).lower()
    return letra


if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")

    # Leer la/las palabras secretas5 de un archivo csv.
    palabras_secretas = get_palabras_secretas('palabras.csv')
    cant_partidas = len(palabras_secretas)

    for i in range(cant_partidas):
        print('\n\nPalabra número', i+1)
        print('Máximo intentos permitidos:', MAX_CANT_INTENTOS)
        
        palabra_adivinar = palabras_secretas[i]['palabras']
    
    print('\nNo quedan más palabras.')
    print("¡Terminó el juego!\n\n")

