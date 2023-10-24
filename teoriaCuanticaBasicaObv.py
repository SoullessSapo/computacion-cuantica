import numpy as np

class SistemaCuantico:
    def __init__(self, num_posiciones, estado_inicial):
        """
        Inicializa un sistema cuántico.

        Parámetros:
        - num_posiciones (int): Número de posiciones discretas en el sistema.
        - estado_inicial (numpy.ndarray): Vector ket que representa el estado inicial del sistema.

        """
        self.num_posiciones = num_posiciones
        self.estado = estado_inicial

    def probabilidad_en_posicion(self, posicion):
        """
        Calcula la probabilidad de encontrar la partícula en una posición específica.

        Parámetros:
        - posicion (int): La posición para la cual se calculará la probabilidad.

        Retorna:
        - probabilidad (float): Probabilidad de encontrar la partícula en la posición dada.
        """
        if 0 <= posicion < self.num_posiciones:
            return np.abs(self.estado[posicion]) ** 2
        else:
            return 0

    def probabilidad_de_transicion(self, estado_final):
        """
        Calcula la probabilidad de transición entre dos estados cuánticos.

        Parámetros:
        - estado_final (numpy.ndarray): El estado cuántico final.

        Retorna:
        - probabilidad (float): Probabilidad de transición desde el estado inicial al estado final.
        """
        return np.abs(np.dot(self.estado, estado_final.conj())) ** 2

def amplitud_de_transicion(estado_inicial, estado_final):
    """
    Calcula la amplitud de transición entre dos estados cuánticos.

    Parámetros:
    - estado_inicial (numpy.ndarray): El estado cuántico inicial.
    - estado_final (numpy.ndarray): El estado cuántico final.

    Retorna:
    - amplitud (float): Amplitud de transición entre los estados inicial y final.
    """
    return np.abs(np.dot(estado_final.conj(), estado_inicial)) ** 2

def es_hermitiana(matriz):
    """
    Comprueba si una matriz es Hermitiana (autoadjunta).

    Parámetros:
    - matriz (numpy.ndarray): La matriz que se va a comprobar.

    Retorna:
    - es_hermitiana (bool): True si la matriz es Hermitiana, False en caso contrario.
    """
    return np.allclose(matriz, matriz.conj().T)

def media_y_varianza(observable, estado):
    """
    Calcula la media y la varianza de un observable en un estado dado.

    Parámetros:
    - observable (numpy.ndarray): La matriz que describe el observable.
    - estado (numpy.ndarray): El estado cuántico en el que se realiza la medición.

    Retorna:
    - media (float): Valor medio del observable en el estado dado.
    - varianza (float): Varianza del observable en el estado dado.
    """
    if es_hermitiana(observable):
        media = np.real(np.dot(estado.conj(), np.dot(observable, estado)))
        varianza = np.real(np.dot(estado.conj(), np.dot(observable ** 2, estado))) - media ** 2
        return media, varianza
    else:
        return None

def autovalores_y_probabilidades_de_transicion(observable, estado, estados_finales):
    """
    Calcula los autovalores y las probabilidades de transición de un observable en un estado dado.

    Parámetros:
    - observable (numpy.ndarray): La matriz que describe el observable.
    - estado (numpy.ndarray): El estado cuántico en el que se realiza la medición.
    - estados_finales (list of numpy.ndarray): Lista de estados cuánticos finales.

    Retorna:
    - autovalores (numpy.ndarray): Los autovalores de la matriz observable.
    - probabilidades_de_transicion (list of float): Lista de probabilidades de transición a los estados finales.
    """
    if es_hermitiana(observable):
        autovalores, autovectores = np.linalg.eig(observable)
        probabilidades_de_transicion = [np.abs(np.dot(estado.conj(), autovector) ** 2) for autovector in estados_finales]
        return autovalores, probabilidades_de_transicion
    else:
        return None

def evolucion_del_sistema(estado_inicial, matrices_de_evolucion):
    """
    Calcula el estado final del sistema a partir de una serie de matrices de evolución.

    Parámetros:
    - estado_inicial (numpy.ndarray): El estado inicial del sistema.
    - matrices_de_evolucion (list of numpy.ndarray): Lista de matrices de evolución temporal.

    Retorna:
    - estado_final (numpy.ndarray): El estado final del sistema después de aplicar las matrices de evolución en secuencia.
    """
    estado = estado_inicial
    for matriz in matrices_de_evolucion:
        estado = np.dot(matriz, estado)
    return estado

# Ejemplos de modelado de problemas

def problema_4_3_1(estado_inicial, estado_final):
    """
    Resuelve el Problema 4.3.1: Calcula la amplitud de transición entre dos estados cuánticos.

    Parámetros:
    - estado_inicial (numpy.ndarray): El estado cuántico inicial.
    - estado_final (numpy.ndarray): El estado cuántico final.

    Retorna:
    - amplitud (float): Amplitud de transición entre los estados inicial y final.
    """
    return amplitud_de_transicion(estado_inicial, estado_final)

def problema_4_3_2(estado_inicial, observable, estados_finales):
    """
    Resuelve el Problema 4.3.2: Calcula los autovalores y las probabilidades de transición de un observable.

    Parámetros:
    - estado_inicial (numpy.ndarray): El estado cuántico inicial.
    - observable (numpy.ndarray): La matriz que describe el observable.
    - estados_finales (list of numpy.ndarray): Lista de estados cuánticos finales.

    Retorna:
    - autovalores (numpy.ndarray): Los autovalores de la matriz observable.
    - probabilidades_de_transicion (list of float): Lista de probabilidades de transición a los estados finales.
    """
    autovalores, probabilidades_de_transicion = autovalores_y_probabilidades_de_transicion(observable, estado_inicial, estados_finales)
    return autovalores, probabilidades_de_transicion

def problema_4_4_1(observable):
    """
    Resuelve el Problema 4.4.1: Comprueba si una matriz es Hermitiana.

    Parámetros:
    - observable (numpy.ndarray): La matriz que se va a comprobar.

    Retorna:
    - es_hermitiana (bool): True si la matriz es Hermitiana, False en caso contrario.
    """
    return es_hermitiana(observable)

def problema_4_4_2

    """
    Resuelve el Problema 4.4.2: Calcula la media, la varianza y las probabilidades de transición de un observable en un estado dado.

    Parámetros:
    - observable (numpy.ndarray): La matriz que describe el observable.
    - estado (numpy.ndarray): El estado cuántico en el que se realiza la medición.
    - estados_finales (list of numpy.ndarray): Lista de estados cuánticos finales.

    Retorna:
    - media (float): Valor medio del observable en el estado dado.
    - varianza (float): Varianza del observable en el estado dado.
    - probabilidades_de_transicion (list of float): Lista de probabilidades de transición a los estados finales.
    """
    media, varianza = media_y_varianza(observable, estado)
    probabilidades_de_transicion = [amplitud_de_transicion(estado, estado_final) for estado_final in estados_finales]
    return media, varianza, probabilidades_de_transicion

# Ejemplo de uso

if __name__ == "__main__":
    # Crear un sistema cuántico
    num_posiciones = 3
    ket_inicial = np.array([0.5, 0.3, 0.2], dtype=complex)
    sistema = SistemaCuantico(num_posiciones, ket_inicial)

    # Calcular probabilidad en una posición
    probabilidad = sistema.probabilidad_en_posicion(1)
    print(f"La probabilidad de encontrar la partícula en la posición 1 es {probabilidad:.2f}")

    # Calcular probabilidad de transición
    ket_final = np.array([0.1, 0.6, -0.4], dtype=complex)
    prob_transicion = sistema.probabilidad_de_transicion(ket_final)
    print(f"La probabilidad de transición al estado final es {prob_transicion:.2f}")

    # Resolver el Problema 4.3.1
    amplitud = problema_4_3_1(ket_inicial, ket_final)
    print(f"Amplitud de transición entre los estados iniciales y finales: {amplitud:.2f}")

    # Resolver el Problema 4.3.2
    matriz_observable = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]], dtype=complex)
    estados_finales = [ket_final, np.array([0.2, -0.4, 0.8], dtype=complex)]
    autovalores, probabilidades = problema_4_3_2(ket_inicial, matriz_observable, estados_finales)
    print(f"Autovalores del observable: {autovalores}")
    print(f"Probabilidades de transición a los estados finales: {probabilidades}")

    # Resolver el Problema 4.4.1
    es_observable_hermitiana = problema_4_4_1(matriz_observable)
    print(f"La matriz observable es Hermitiana: {es_observable_hermitiana}")

    # Resolver el Problema 4.4.2
    media, varianza, probabilidades_transicion = problema_4_4_2(matriz_observable, ket_inicial, estados_finales)
    print(f"Media del observable: {media:.2f}")
    print(f"Varianza del observable: {varianza:.2f}")
    print(f"Probabilidades de transición a los estados finales: {probabilidades_transicion}")
Este código en Python incluye una serie de clases y funciones que modelan un sistema cuántico, resuelven los desafíos y problemas mencionados y proporcionan ejemplos de uso. Puedes adaptarlo y ampliarlo según tus necesidades.





