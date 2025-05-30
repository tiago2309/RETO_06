# RETO_06
Desarrollo de los ejercicios puestos en clase. Para cada punto se creo un programa individual en VS Code y asimismo se creo un notebook con la solución a todos los problemas. Además se hizo un diagrama de flujo para los primeros 3 puntos pero desde GitHub(Ya que no supe como hacerlo en VS Code y preferí hacerlo con mermaid directamente en el repo).

En esta parte solo veremos los diagramas de flujo ya que adjuntos están las soluciones de cada uno de los puntos

### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```mermaid
flowchart TD
    A["Inicio"] --> B["Inicar con num en 1"]
    B --> C{"¿Es 1 <= n <= 100?"}
    C -- Sí --> D["Imprimir (n^2)"]
    D --> E["Pasar al siguiente número (n+1)"]
    E --> C
    C -- No --> F["Fin"]
```

### 2. Imprimir un listado con los números impares y pares del 1 al 1000.

```mermaid
flowchart TD
    A["Inicio"] --> B["Leer n"]
    B --> C{"¿1 <= n <= 1000?"}
    C -- No --> Z["Fin"]
    C -- Sí --> D{"n % 2 == 0?"}
    
    D -- Sí --> E["Inicializar num = 2"]
    D -- No --> F["Inicializar num = 1"]

    E --> G["Mostrar num"]
    G --> H["num = num + 2"]
    H --> I{"¿num > 1000?"}
    I -- No --> G
    I -- Sí --> Z

    F --> J["Mostrar num"]
    J --> K["num = num + 2"]
    K --> L{"¿num > 1000?"}
    L -- No --> J
    L -- Sí --> Z

    Z["Fin"]

```

### 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```mermaid
flowchart TD
    A["Inicio"] --> B["Leer n"]
    B --> C{"¿n ≥ 2?"}
    C -- No --> Z["Fin"]
    C -- Sí --> D{"n % 2 == 0?"}
    
    D -- Sí --> E["Inicializar num = n"]
    D -- No --> F["Inicializar num = n - 1"]

    E --> G["Mostrar num"]
    G --> H["num = num - 2"]
    H --> I{"num ≥ 2?"}
    I -- Sí --> G
    I -- No --> Z

    F --> J["Mostrar num"]
    J --> K["num = num - 2"]
    K --> L{"num ≥ 2?"}
    L -- Sí --> J
    L -- No --> Z

    Z["Fin"]

```
