import numpy as np
import matplotlib.pyplot as plt
import unittest
# Experimento de las canicas con coeficiente booleanos
def canicas_booleanas(matriz_estado_inicial, matriz_transicion, pasos):
    estado_actual = matriz_estado_inicial
    for _ in range(pasos):
        estado_actual = np.dot(matriz_transicion, estado_actual)
    return estado_actual

# Experimento de las múltiples rendijas clásico probabilístico
def rendijas_clasico_probabilistico(matriz_transicion, matriz_probabilidades_inicial, pasos):
    estado_actual = matriz_probabilidades_inicial
    for _ in range(pasos):
        estado_actual = np.dot(matriz_transicion, estado_actual)
    return estado_actual

# Experimento de las múltiples rendijas cuántico
def rendijas_cuantico(matriz_transicion, vector_estado_inicial, pasos):
    estado_actual = vector_estado_inicial
    for _ in range(pasos):
        estado_actual = np.dot(matriz_transicion, estado_actual)
    return estado_actual

# Función para graficar un vector de estados
def graficar_probabilidades(vector_estado, etiquetas, titulo, nombre_archivo):
    plt.bar(range(len(vector_estado)), vector_estado)
    plt.xticks(range(len(etiquetas)), etiquetas)
    plt.title(titulo)
    plt.xlabel("Estado")
    plt.ylabel("Probabilidad")
    plt.savefig(nombre_archivo)
    plt.show()

# Ejemplo de uso
class TestExperimentos(unittest.TestCase):
    def test_canicas_booleanas(self):
        matriz_transicion_canicas = np.array([[0, 0, 1, 0],
                                              [0, 1, 0, 0],
                                              [1, 0, 0, 0],
                                              [0, 0, 0, 1]], dtype=float)
        vector_estado_inicial_canicas = np.array([1, 0, 0, 0], dtype=float)
        resultado_canicas = canicas_booleanas(matriz_transicion_canicas, vector_estado_inicial_canicas, 1)
        self.assertTrue(np.allclose(resultado_canicas, [0., 0., 1., 0.], atol=1e-6))

    def test_rendijas_clasico_probabilistico(self):
        matriz_transicion_rendijas = np.array([[0, 1/2, 1/2],
                                               [0, 1, 0],
                                               [0, 0, 1]], dtype=float)
        vector_probabilidades_inicial_rendijas = np.array([1, 0, 0], dtype=float)
        resultado_rendijas_clasico = rendijas_clasico_probabilistico(matriz_transicion_rendijas, vector_probabilidades_inicial_rendijas, 1)
        self.assertTrue(np.allclose(resultado_rendijas_clasico, [0., 0., 0.], atol=1e-6))

    def test_rendijas_cuantico(self):
        matriz_transicion_rendijas_cuantico = np.array([[0, 1/np.sqrt(2), 1/np.sqrt(2)],
                                                        [1/np.sqrt(2), 0, 1/np.sqrt(2)],
                                                        [1/np.sqrt(2), 1/np.sqrt(2), 0]], dtype=complex)
        vector_estado_inicial_rendijas_cuantico = np.array([1, 0, 0], dtype=complex)
        resultado_rendijas_cuantico = rendijas_cuantico(matriz_transicion_rendijas_cuantico, vector_estado_inicial_rendijas_cuantico, 1)
        self.assertTrue(np.allclose(resultado_rendijas_cuantico, [0. + 0j, 0.70710678 + 0j, 0.70710678 + 0j], atol=1e-6))

if __name__ == "__main__":
    unittest.main()