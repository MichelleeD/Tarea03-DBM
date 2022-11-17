import Evaluador
import os

expresion_infija = ""

def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    print("\tEste programa convierte expreciones")
    print("\t")
    print("\tSe muestra la expresion en forma Postfija")
    print("_________________________________________")


def convertir(expresion_infija):
    expresion_infija = list(expresion_infija.upper())
    expresion_postfija = []
    return Evaluador.evaluar(expresion_infija, 100, expresion_postfija)


while True:
    # Mostramos el menu
    menu()

    # Solicitamos una opción al usuario
    expresion_infija = input("Digite la expresion: ")
    print("Expresion Guardada!")
    input("pulsa ENTER para continuar...")
    if expresion_infija == "":
        print("No ha ingresado una expresion")
        input("pulsa ENTER para continuar...")
    else:
        print(convertir(expresion_infija))
        input("pulsa una tecla para salir...")
    break