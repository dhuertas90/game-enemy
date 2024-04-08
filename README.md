# Juego Simple en Pygame

Este es un juego simple creado con Pygame donde controlas a un jugador y debes evitar a los enemigos (representados por cajas u objetos cuadrados) que caen desde arriba. El juego termina si el jugador colisiona con un enemigo.

## Requisitos

- Python 3.x
- Pygame (instalable a través de `pip install pygame`)

## Ejecución

Para ejecutar el juego, simplemente ejecuta el archivo `main.py` con Python:

python main.py


## Controles

- Flecha Izquierda: Mover el jugador hacia la izquierda.
- Flecha Derecha: Mover el jugador hacia la derecha.
- Barra Espaciadora: Iniciar el juego desde el menú principal.
- Tecla Q: Salir del juego desde el menú principal.

## Funcionalidades

- El jugador puede moverse horizontalmente usando las teclas de flecha.
- Los enemigos caen desde la parte superior de la pantalla y se mueven hacia abajo.
- El juego termina si el jugador colisiona con un enemigo.
- El juego incluye un menú principal con opciones para comenzar el juego o salir del mismo.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `main.py`: Archivo principal que contiene la función principal del juego.
- `modules/`: Carpeta que contiene los módulos `player.py` y `enemy.py` que definen las clases `Player` y `Enemy` respectivamente.
- `README.md`: Este archivo que describe el proyecto y su funcionalidad.


## Créditos

Este juego fue creado por David Huertas.