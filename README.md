# Mastermind — Heridos y muertos

Proyecto en Python creado en noviembre de 2020 con tres variantes del juego Mastermind. Esta documentación describe el **código original**, sin modificar su funcionamiento.

## Reglas

Se debe acertar una combinación ordenada de cuatro elementos **sin repetir**.

- **Dead (muerto):** elemento correcto en la posición correcta.
- **Hurt (herido):** elemento correcto en una posición distinta.

Se gana con cuatro muertos.

## Versiones

| Archivo | Modalidad | Intentos reales |
| --- | --- | --- |
| [mastermind_numeros.py](mastermind_numeros.py) | Adivinar cuatro dígitos del 0 al 9 | 20 |
| [mastermind_colores.py](mastermind_colores.py) | Adivinar cuatro colores diferentes entre 11 disponibles | 15 |
| [mastermind_numcom.py](mastermind_numcom.py) | El ordenador adivina los cuatro dígitos elegidos por el usuario | 200 |

Las tres versiones muestran un historial de intentos. Los números se manejan como cadenas, por lo que pueden comenzar por cero.

## Ejecución

Se necesita Python 3. Para la variante del ordenador:

```bash
python mastermind_numcom.py
```

Las variantes de números y colores dependen de IPython para limpiar la pantalla:

```bash
python -m pip install ipython
ipython
```

Dentro de IPython, ejecutar `%run mastermind_numeros.py` o `%run mastermind_colores.py`. Ejecutarlas directamente con Python convencional puede fallar por la llamada a `get_ipython().magic("clear")`.

## Documentación técnica

- [Estructura y funcionamiento](docs/funcionamiento.md)
- [Algoritmo del ordenador](docs/algoritmo-com.md)
- [Limitaciones conocidas](docs/limitaciones.md)

## Estado

Proyecto histórico de aprendizaje. No incluye pruebas automatizadas. Esta documentación se ha preparado mediante revisión estática del código, sin afirmar resultados de rendimiento no medidos.