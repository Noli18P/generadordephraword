import random


def generador():
    words = ['perro ', 'hola ', 'computadora ', 'caballo ', 'raton ', 'hamburguesa ', 'numero ', 'corazon ', 'laptop ', 'mitnik ', 'tableta ', 'granja ', 'higado ', 'hoja ', 'calzon ', 'chamarra ', 'internet ', 'escoba ', 'traje ', 'agua ', 'cerdo ','cabra ', 'automovil ', 'arte ', 'pintura ', 'textura ', 'chancla ', 'generador ', 'bruja ', 'chupacabras ', 'nahual ', 'tlacuache ', 'america ', 'europa ', 'london ', 'harry ', 'potter ', 'bocina ', 'lampara ', 'cama ', 'robot ', 'eliot ', 'alderson ', 'patata ', 'queso ', 'coco ', 'pasta ', 'platzi ']

    num_words = int(input('Dime un número: '))
    i = 0
    pw = []

    while i < num_words:
        pw.append(random.choice(words))
        i += 1
    password = ''.join(pw)

    return password


def menu():
    menu = """
Este generador de contraseñas, creara una lista de palabras tan larga como desees.
Tienes que ingresar un número y presionar enter.

La forma en la que esta creada este script es para que tu generes contraseñsas más seguras en base a
palabras aleatorias asi que de esta forma al atacante será mucho más dificil hackearte.

Estas palabras puedes cambiarlas como desees o quitar alguna si es que no te gusta o simplemente elegir otra!
Además de que puedes agregar números o cambiarla a mayusculas, recuerda que entre más rara la contraseña más 
complicado para el atacante.

Disfrutala!
    """
    print(menu)


def main():
    menu()

    contra = generador()
    print(contra)

    seleccion = input('Quieres continuar con esta contraseña o deseas que genere otra (s/n)')

    if seleccion == 's' or seleccion == 'si':
        main()
    else:
        print('Hasta luego')


if __name__ == '__main__':
    main()
