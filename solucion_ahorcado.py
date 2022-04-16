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


def get_palabra_oculta(palabra_oculta):
    '''
    Obtiene de la lista "palabra_oculta"
    las letras, retornando un string de esa
    palabra.
    '''
    palabra = ''
    for i in range(len(palabra_oculta)):
        # Como la letra viene con el caracter seguido
        # de un '.', me quedo sólo con la letra.
        palabra += palabra_oculta[i][0:-1]
    return palabra


def ahorcado(palabra):
    '''
    Función que comprueba si el jugador ganó o no la partida
    dependiendo si adivinó la "palabra secreta" o si perdió
    porque superó el máximo de intentos permitidos.
    '''
    # Inicializo las variables y listas a utilizar.
    intentos = 0
    letras_usadas = []
    es_ganador = False     
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra, letras_usadas, intentos)
    return es_ganador


def imprimir_mensaje_resultado(es_ganador, nro_partida):
    '''
    Muestra un mensaje en consola dependiendo
    si el jugador ganó o no la partida.
    '''
    if es_ganador:
        print(f'\n¡Usted ah ganado la partida número {nro_partida+1}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'¡Usted ah perdido la partida número {nro_partida+1}!\n')


if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")

    # Leer la/las palabras secretas5 de un archivo csv.
    palabras_secretas = get_palabras_secretas('palabras.csv')
    cant_partidas = len(palabras_secretas)

    for i in range(cant_partidas):
        print('\n\nPalabra número', i+1)
        print('Máximo intentos permitidos:', MAX_CANT_INTENTOS)
        
        palabra_adivinar = palabras_secretas[i]['palabras']
        es_ganador = ahorcado(palabra_adivinar)
        imprimir_mensaje_resultado(es_ganador, i)
    
    print('\nNo quedan más palabras.')
    print("¡Terminó el juego!\n\n")

