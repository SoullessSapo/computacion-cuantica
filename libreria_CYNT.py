import numpy as np

def producto_tensor(m1,m2):
    m1 = np.array(m1)
    m2 = np.aray(m2)
    return np.tensordot(m1,m2)
def main():
    numero_fila = int(input("indique el numero de filas que va a tener la primera matriz"))
    m1 = []
    m2 = []
    for i in range(numero_fila):
        fila = map(int,input("vaya insertando fila de la matriz").split())
        m1.append(fila)
    numero_fila = int(input("indique el numero de filas que va a tener la segunda matriz"))
    for i in range(numero_fila):
        fila = map(int, input("vaya insertando fila de la matriz").split())
        m2.append(fila)
    print(producto_tensor(m1,m2))
main()