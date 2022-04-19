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


def validar_palabra(letras_usadas, palabra_oculta):
    '''
    Retorna si la palabra oculta ha sido descubierta
    '''
    validar = True
    for letra in palabra_oculta:
        if letra not in letras_usadas:
            validar = False
            break
    
    return validar


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
    
    while intentos < MAX_CANT_INTENTOS and not es_ganador:
        # Obtengo la letra y verifico que la misma esté
        # en la palabra a adivinar.
        letra = get_letra()

        # Compruebo que la letra ya no se ha ingresado anteriormente.
        # En caso de no estar la appendeo en la lista de letras_usadas.
        if letra in letras_usadas:
            print('Usted ya ingresó la letra "{}".'.format(letra))
        else:
            letra_favorable = verificar_letra(letra, palabra)

            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            if not letra_favorable:
                intentos += 1
            letras_usadas.append(letra) # Agregamos la letra
            palabra_oculta = interfaz.dibujar(palabra, letras_usadas, intentos)
            
            # En esta parte determinamos si el jugador gana o pierde la 
            # partida.
            if intentos == MAX_CANT_INTENTOS:
                es_ganador = False
            else:
                # Va a ganar si la palabra coincide con las letras
                # que el jugador ingresó. Esto ocurre únicamente si
                # adivinó la palabra antes de acabar con los intentos
                # permitidos.
                if validar_palabra(letras_usadas, palabra_oculta) == True:
                    es_ganador = True
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

