import machine
import time

# Código morse
MORSE = {"A": ".-",
         "B": "-...",
         "C": "-.-.",
         "D": "-..",
         "E": ".",
         "F": "..-.",
         "G": "--.",
         "H": "....",
         "I": "..",
         "J": ".---",
         "K": "-.-",
         "L": ".-..",
         "M": "--",
         "N": "-.",
         "Ñ": "--.--",
         "O": "---",
         "P": ".--.",
         "Q": "--.-",
         "R": ".-.",
         "S": "...",
         "T": "-",
         "U": "..-",
         "V": "...-",
         "W": ".--",
         "X": "-..-",
         "Y": "-.--",
         "Z": "--..",
         "0": "-----",
         "1": ".----",
         "2": "..---",
         "3": "...--",
         "4": "....-",
         "5": ".....",
         "6": "-....",
         "7": "--...",
         "8": "---..",
         "9": "----.",
         ".": ".-.-.-",
         ",": "-.-.--",
         "?": "..--..",
         '"': ".-..-.",
         "!": "--..--",
         " ": " "}


def pinLed(pin):
    return machine.Pin(pin, machine.Pin.OUT)


def flash(pin, sec):
    pin.value(False)
    time.sleep(sec)
    pin.value(True)
    time.sleep(sec)

    return


def send(pin,
         message="Bienvenido!",
         short=0.5):
    """
        message: mensaje a interpretar (por defecto: Hola mundo!")
        pinLed: pin en el que se encuentra el led que iluminar
            (por defecto: 16)
        short: representa la duración de la pulsación corta
            (por defecto: 0.5 segundos)
    """

    print(message)

    # Apaga el led en caso de que esté encendido
    if pin.value == False:
        pin.value(True)

    # Tiempo que el LED está encendido según el tipo de pulsación (corta, larga o espacio)
    long = short * 3
    space = short * 2

    for letter in message:
        code = MORSE.get(letter.upper())

        for e in code:
            print("{} >> {}".format(letter, e))

            if e == ".":
                flash(pin, short)

            if e == "-":
                flash(pin, long)

            if e == " ":
                flash(pin, space)

try:
    send(pin=pinLed(16))

except KeyboardInterrupt:
    print("Se ha interrumpido el programa")

else:
    print("Programa finalizado")
