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
