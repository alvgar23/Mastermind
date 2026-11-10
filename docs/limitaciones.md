# Limitaciones del código original

Observaciones realizadas mediante lectura del código; no se han ejecutado pruebas de regresión.

- El menú de `mastermind_numeros.py` promete **10 intentos**, pero el juego permite **20**.
- Los ejemplos de los menús contienen contadores de intentos que no siempre coinciden con los límites programados.
- `mastermind_numeros.py` y `mastermind_colores.py` utilizan `get_ipython().magic("clear")`: fuera de una sesión IPython pueden fallar.
- Todos los archivos ejecutan una partida al importarse, porque llaman a `game()` directamente al final.
- `background_list` es global y no se reinicia al iniciar otra partida dentro de la misma sesión.
- La validación de números usa `int()` y puede responder mal ante algunas entradas inesperadas.
- La comparación está diseñada para combinaciones sin elementos repetidos.
- La lógica está duplicada entre las versiones y no existen pruebas automatizadas.
- La variante del ordenador solo utiliza la pista anterior para decidir; no comprueba todas las restricciones acumuladas.
- En la rama `dead == 1 and hurt == 1` de `mastermind_numcom.py` queda un `print(n1)` de depuración.
- No existe almacenamiento permanente del historial.
- No hay datos de rendimiento reproducibles para afirmar porcentajes de éxito.

El objetivo de estos documentos es conservar y explicar el proyecto tal como fue escrito, **no corregir ni modernizar su código**.