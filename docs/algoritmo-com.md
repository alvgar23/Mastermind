# Algoritmo del ordenador

El archivo [mastermind_numcom.py](../mastermind_numcom.py) implementa un método heurístico y aleatorio para adivinar el número del jugador.

## Funcionamiento

El jugador introduce cuatro dígitos distintos. En cada ronda el ordenador propone una combinación, calcula muertos y heridos y utiliza `decision(dead, hurt, com_number)` para construir la siguiente.

- **0 muertos:** conserva tantos dígitos de la propuesta anterior como heridos haya, rellena los demás al azar y mezcla posiciones.
- **1 muerto:** elige aleatoriamente un dígito para mantenerlo en su posición; conserva además tantos otros como heridos.
- **2 muertos:** elige dos dígitos para mantener sus posiciones; añade los heridos y completa la combinación.
- **3 muertos:** elige tres posiciones para conservar y decide el cuarto dígito según los heridos.

Se emplean `random.choice`, `random.randint` y `random.shuffle`. Los bucles impiden dígitos repetidos y fuerzan las posiciones elegidas.

## Limitación fundamental

El programa **no sabe cuáles son realmente las posiciones acertadas**: elige cuáles conservar al azar. Tampoco mantiene una lista de combinaciones compatibles con **todas** las pistas anteriores, ni descarta sistemáticamente propuestas ya probadas.

Por tanto, aprovecha parcialmente la última pista, pero puede perder información y repetir intentos. El límite de **200 intentos no garantiza resolver** la combinación. No hay pruebas automatizadas ni estadísticas de éxito verificadas en este repositorio.

Esta descripción documenta la implementación original; no es una propuesta de algoritmo óptimo.