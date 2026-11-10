# Estructura y funcionamiento

El repositorio contiene tres scripts Python independientes, sin biblioteca compartida, interfaz gráfica ni persistencia.

## Flujo común

1. Se genera o introduce una combinación secreta de cuatro elementos diferentes.
2. Se solicita o genera una propuesta.
3. `compare()` cuenta **dead** (misma posición) y **hurt** (elemento presente en otra posición).
4. `background()` añade la jugada a la lista global `background_list` y muestra el historial.
5. `game()` repite el ciclo hasta acertar o agotar los intentos.

## mastermind_numeros.py

`menu()` muestra instrucciones; `number_generator()` genera cuatro dígitos distintos; `user_number()` solicita y valida cada dígito; `compare()` evalúa el intento; `background()` registra el historial; `game()` controla **20 intentos**.

## mastermind_colores.py

`colors` contiene 11 colores: red, white, grey, green, brown, yellow, black, orange, blue, purple y pink. `color_generator()` elige cuatro distintos; `user_color()` recoge la propuesta, sin distinguir mayúsculas; `compare()`, `background()` y `game()` controlan las pistas, historial y **15 intentos**.

## mastermind_numcom.py

`user_number()` pide el secreto; `number_generator()` crea propuestas aleatorias; `decision()` genera la siguiente propuesta a partir de los muertos y heridos anteriores; `compare()` la evalúa; `background()` registra el historial; `game()` permite **200 intentos**.

Todos los scripts ejecutan `game(dead, hurt)` al final, también al importarlos. La comparación presupone elementos sin repetir. El historial no se guarda en disco.