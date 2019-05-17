# Interpretador morse | Morse interpreter

Pequeño programa que interpreta cada letra con sus respectivas pulsaciones en morse. Envía la interpretación a un LED de un microcontrolador con Micropython.

Se ha probado con una ESP8266, en la que el LED se encuentra en el pin 16. Este pequeño programa te permite seleccionar el pin en el que se encuentre el LED, por lo que debería ser compatible con otras placas.

## Funciones

Véase las *issues* etiquetadas como [*Enhancement*](https://github.com/ivanhercaz/morseinterpreter-micropython/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) para una lista completa de las funciones y mejoras que se contemplan.

- [x] Enviar mensajes morse con un LED.
- [ ] Interpretar mensajes LED con un sensor (idea de [Juan Ignacio Rodríguez de León (Euribates)](https://github.com/euribates)).
- [ ] Pantalla lectora.

## Agradecimientos

Agradezco a [Matt Sheppard (mampersat)](https://github.com/mampersat) por su repositorio [micropython-morsecode](https://github.com/mampersat/micropython-morsecode), que me ha ayudado mucho con este.

## Demostración
![Demostración del interpretador](https://raw.githubusercontent.com/ivanhercaz/morseinterpreter-micropython/master/demo.gif)
