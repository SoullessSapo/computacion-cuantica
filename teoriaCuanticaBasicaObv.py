import math

import numpy as np


def calculatePos(v, p):
    modu = np.linalg.norm(v)
    x = np.linalg.norm(v[p])
    return x ** 2 / modu ** 2


def probTrans(v1, v2):
    v2 = np.array(v2)
    v2 = v2.conjugate()
    v2 = v2.transpose()
    inner = np.dot(v1, v2)
    return inner / (np.linalg.norm(v1) * np.linalg.norm(v2))
    
def is_hermitian(matrix):
    return np.allclose(matrix, np.conjugate(matrix.T))

def media_varianza(m,v):
    ver = is_hermitian(m)
    print(v)
    print(m)
    print("ver", ver)
    if ver:
        v = np.array(v)
        media = np.dot(m, v)
        media = media.conjugate()
        media = np.dot(media, v.transpose())
        ma = [[0 for x in range(2)] for x in range(2)]
        ma[0][0], ma[1][1] = media, media
        ma = np.array(ma)
        var = m - ma
        var = np.dot(var,var)
        var = np.dot(v, var)
        var = np.dot(var, v)
        return media, var

def main():
    v = np.array([-3 - 1j, -2j, 1j, 2])
    pos = 2
    print(calculatePos(v, pos))
    v1 = math.sqrt(2) / 2 * np.array([1, 1j])
    v2 = math.sqrt(2) / 2 * np.array([1j, -1])
    v1 = np.array(v1)
    v2 = np.array(v2)
    print(probTrans(v1, v2))


main()
