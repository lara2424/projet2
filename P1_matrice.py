# trouver les coordonnées du plus haut point d'une matrice
import unittest
import random


def maxMatrice(matrice):
    max = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] > max:
                max = matrice[i][j]
    return max


def dicoMatrice(matrice):
    dico = dict()

    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] in dico:
                dico[matrice[i][j]] += 1
        dico["max"] = max
    return dico


def minMatriceOk(matrice):
    min = 999999
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] < min:
                max = matrice[i][j]
    return min


def maxMatriceOk(matrice):
    max = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] > max:
                max = matrice[i][j]
    return max


def dicoMatriceOk(matrice):
    max = maxMatriceOk(matrice)
    dico = dict()
    for i in range(max):
        dico[i] = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if matrice[i][j] in dico:
                dico[matrice[i][j]] += 1
        dico["max"] = max
    return dico


def makeMatrice():
    col = random.randint(0, 10)
    line = random.randint(0, 10)
    matrice = [[random.randint(0, 5) for i in range(col)] for j in range(line)]
    return matrice


class TestmaxMatrice(unittest.TestCase):

    def test_maxMatrice(self):
        matrice = makeMatrice()
        self.assertEqual(maxMatrice(matrice), maxMatriceOk(matrice),
                         "for the matrice : " + str(matrice) + "\n you return :" + str(
                             maxMatrice(matrice)) + " when it should be " + str(maxMatriceOk(matrice)))

    def test_dicoMatriceLen(self):
        matrice = makeMatrice()
        # verifier que chaque cle est présente meme à zero ! et que le nb correspondant est bon
        self.assertEqual(len(dicoMatrice(matrice)), len(dicoMatriceOk(matrice)),
                         "The number of key you have is not correct,\n make sure you have all key between the lowest and biggest number of the matrice")

    def test_dicoMatriceVal(self):
        matrice = makeMatrice()
        dico = dicoMatrice(matrice)
        dicoOk = dicoMatriceOk(matrice)
        for i in range(maxMatriceOk(matrice)):
            self.assertEqual(dico.get(i), dicoOk.get(i),
                             "At the key " + str(i) + " your have" + str(dico.get(i)) + " when it should be " + str(
                                 dicoOk.get(i)))


if __name__ == '__main__':
    unittest.main()
