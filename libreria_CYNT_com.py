import numpy as np

# Función para imprimir matrices/vectores complejos de manera legible
def print_complex_matrix(matrix):
    for row in matrix:
        print([f"{elem.real} + {elem.imag}i" for elem in row])

# Adición de vectores complejos
def add_complex_vectors(vector1, vector2):
    return np.add(vector1, vector2)

# Prueba de adición de vectores complejos
vector_a = np.array([1 + 2j, 3 + 4j])
vector_b = np.array([2 - 1j, 1 - 3j])
result_add_vectors = add_complex_vectors(vector_a, vector_b)
print("Resultado de la adición de vectores complejos:")
print_complex_matrix(result_add_vectors)
print("\n")

# Inverso (aditivo) de un vector complejo
def inverse_complex_vector(vector):
    return np.negative(vector)

# Prueba de inverso de un vector complejo
result_inverse_vector = inverse_complex_vector(vector_a)
print("Resultado del inverso de un vector complejo:")
print_complex_matrix(result_inverse_vector)
print("\n")

# Multiplicación de un escalar por un vector complejo
def scalar_multiply_complex_vector(scalar, vector):
    return np.multiply(scalar, vector)

# Prueba de multiplicación de un escalar por un vector complejo
scalar = 2 + 3j
result_scalar_multiply = scalar_multiply_complex_vector(scalar, vector_a)
print(f"Resultado de la multiplicación por escalar ({scalar}) de un vector complejo:")
print_complex_matrix(result_scalar_multiply)
print("\n")

# Adición de matrices complejas
def add_complex_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

# Prueba de adición de matrices complejas
matrix_x = np.array([[1 + 2j, 3 + 4j], [5 + 6j, 7 + 8j]])
matrix_y = np.array([[2 - 1j, 1 - 3j], [4 - 2j, 3 - 1j]])
result_add_matrices = add_complex_matrices(matrix_x, matrix_y)
print("Resultado de la adición de matrices complejas:")
print_complex_matrix(result_add_matrices)
print("\n")

# Inversa (aditiva) de una matriz compleja
def inverse_complex_matrix(matrix):
    return np.negative(matrix)

# Prueba de inversa de una matriz compleja
result_inverse_matrix = inverse_complex_matrix(matrix_x)
print("Resultado de la inversa de una matriz compleja:")
print_complex_matrix(result_inverse_matrix)
print("\n")

# Multiplicación de un escalar por una matriz compleja
def scalar_multiply_complex_matrix(scalar, matrix):
    return np.multiply(scalar, matrix)

# Prueba de multiplicación de un escalar por una matriz compleja
scalar_matrix = 2 + 3j
result_scalar_multiply_matrix = scalar_multiply_complex_matrix(scalar_matrix, matrix_x)
print(f"Resultado de la multiplicación por escalar ({scalar_matrix}) de una matriz compleja:")
print_complex_matrix(result_scalar_multiply_matrix)
print("\n")

# Transpuesta de una matriz/vector
def complex_transpose(matrix):
    return np.transpose(matrix)

# Prueba de transpuesta de una matriz compleja
result_transpose_matrix = complex_transpose(matrix_x)
print("Resultado de la transpuesta de una matriz compleja:")
print_complex_matrix(result_transpose_matrix)
print("\n")

# Conjugada de una matriz/vector
def complex_conjugate(matrix):
    return np.conjugate(matrix)

# Prueba de conjugada de una matriz compleja
result_conjugate_matrix = complex_conjugate(matrix_x)
print("Resultado de la conjugada de una matriz compleja:")
print_complex_matrix(result_conjugate_matrix)
print("\n")

# Adjunta (daga) de una matriz/vector
def complex_adjoint(matrix):
    return np.transpose(np.conjugate(matrix))

# Prueba de adjunta de una matriz compleja
result_adjoint_matrix = complex_adjoint(matrix_x)
print("Resultado de la adjunta de una matriz compleja:")
print_complex_matrix(result_adjoint_matrix)
print("\n")

# Producto de dos matrices (de tamaños compatibles)
def matrix_multiply(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Prueba de producto de dos matrices
matrix_a = np.array([[1 + 2j, 3 + 4j], [5 + 6j, 7 + 8j]])
matrix_b = np.array([[2 - 1j, 1 - 3j], [4 - 2j, 3 - 1j]])
result_matrix_multiply = matrix_multiply(matrix_a, matrix_b)
print("Resultado del producto de dos matrices complejas:")
print_complex_matrix(result_matrix_multiply)
print("\n")

# Función para calcular la "acción" de una matriz sobre un vector
def matrix_vector_action(matrix, vector):
    return np.dot(matrix, vector)

# Prueba de la acción de una matriz sobre un vector
result_action_matrix_vector = matrix_vector_action(matrix_a, vector_a)
print("Resultado de la acción de una matriz sobre un vector complejo:")
print_complex_matrix(result_action_matrix_vector)
print("\n")

# Producto interno de dos vectores
def inner_product(vector1, vector2):
    return np.inner(vector1, vector2)

# Prueba de producto interno de dos vectores complejos
result_inner_product = inner_product(vector_a, vector_b)
print("Resultado del producto interno de dos vectores complejos:")
print(result_inner_product)
print("\n")

# Norma de un vector
def vector_norm(vector):
    return np.linalg.norm(vector)

# Prueba de norma de un vector complejo
result_vector_norm = vector_norm(vector_a)
print("Resultado de la norma de un vector complejo:")
print(result_vector_norm)
print("\n")

# Distancia entre dos vectores
def vector_distance(vector1, vector2):
    return np.linalg.norm(vector1 - vector2)

# Prueba de distancia entre dos vectores complejos
result_vector_distance = vector_distance(vector_a, vector_b)
print("Resultado de la distancia entre dos vectores complejos:")
print(result_vector_distance)
print("\n")

# Valores y vectores propios de una matriz
def eigenvalues_eigenvectors(matrix):
    return np.linalg.eig(matrix)

# Prueba de valores y vectores propios de una matriz compleja
eigenvalues, eigenvectors = eigenvalues_eigenvectors(matrix_a)
print("Valores propios de la matriz compleja:")
print(eigenvalues)
print("Vectores propios de la matriz compleja:")
print_complex_matrix(eigenvectors)
print("\n")

# Revisar si una matriz es unitaria
def is_unitary(matrix):
    return np.allclose(np.dot(matrix, np.conjugate(matrix.T)), np.identity(matrix.shape[0]))

# Prueba de si una matriz es unitaria
result_is_unitary = is_unit
result_is_unitary = is_unitary(matrix_x)
print("¿La matriz es unitaria?")
print(result_is_unitary)
print("\n")

# Revisar si una matriz es Hermitiana
def is_hermitian(matrix):
    return np.allclose(matrix, np.conjugate(matrix.T))

# Prueba de si una matriz es Hermitiana
result_is_hermitian = is_hermitian(matrix_x)
print("¿La matriz es Hermitiana?")
print(result_is_hermitian)
print("\n")

# Producto tensor de dos matrices/vectores
def tensor_product(matrix1, matrix2):
    return np.kron(matrix1, matrix2)

# Prueba de producto tensor de dos matrices complejas
result_tensor_product = tensor_product(matrix_x, matrix_y)
print("Resultado del producto tensor de dos matrices complejas:")
print_complex_matrix(result_tensor_product)
print("\n")

# Prueba de producto tensor de dos vectores complejos
result_tensor_product_vectors = tensor_product(vector_a, vector_b)
print("Resultado del producto tensor de dos vectores complejos:")
print_complex_matrix(result_tensor_product_vectors)
print("\n")
