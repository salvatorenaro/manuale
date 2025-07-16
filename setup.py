import numpy as np
import logging
import sys
from dataclasses import dataclass
import platform

""""IMPLEMENTAZIONE MANUALE DI MOLTE FUNZIONALITA DI NUMPY CODICE ANCORA IN FASE DI LAVORAZIONE"""




@dataclass
class Clip:
    while True:
        controllo =  ["Inserisci un numero", "Perfavore digiti un numero", "E richiesto un numero non una stringa"]
        controllo_numero  = ['Numero di fine non puo essere minore del numero di inizio','Il numero di fine è minore,si prega di inserire un numero maggiore']
        frase_casuale  = np.random.choice(controllo) 
        frase_casuale_numero  =  np.random.choice(controllo_numero)
        print("La matrice va da 0 a 9")
        utente = input("Inserisci un numero d' inizio: ")
        fine = input("Inserisci un numero di fine:  ")
        try:
            if utente.isdigit() and fine.isdigit():
                if fine < utente :
                    logging.error(frase_casuale_numero)
                    continue
                else:
                    utente = int(utente)
                    fine = int(fine)
                    break
            else:
                logging.error(frase_casuale)
                continue
        except Exception as e:
            logging.error("Errorre {}".format(e))
    def __init__(self):
        self.array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
    def  clip(self, n = fine, start = utente):
        try:
            if n:
                y = []
                for i in range(0 , len(self.array)):
                    if self.array[i] > n:
                        self.array[i] = n
                    elif self.array[i] < start:
                        self.array[i]  = start
                    else:
                        self.array[i] = self.array[i]
                    y.append(self.array[i])
                print(y)
        except Exception as e:
            print("errore {}".format(e))   



@dataclass
class Transpose:
    matrix = np.array([[1, 2, 3], 
                        [4, 5, 6],
                        [7, 8, 9]])
    copy = np.copy(matrix)
    lenght  = len(matrix)
    def __init__(self):
            pass
    def transpose(self, lenght = lenght , copy = copy, matrix = matrix):
        print("\n","Matrice iniziale: \n {}".format(matrix))
        for i in range(lenght):
            for j in range(lenght):
                copy[i][j]  = matrix[j][i]
        print("\n","Transposizione della matrice dopo\n")
        print(copy)



@dataclass       
class Diagonale:
    matrix = np.array([[1, 2, 3],  
                        [4, 5, 6],
                        [7, 8, 9]])
    def __init__(self):
        pass
    def diagonale(self, matrix = matrix):
        print("Matrice iniziale(diagonale da destra): \n {}".format(matrix))
        print("\n","Matrice dopo(diagonale da destra)","\n",)
        for i in range(len(matrix)):
            for j in range(i + 1):
                matrix[i][j] = matrix[i][j] 
            print("{}".format(matrix[i][j]), end=" ")



@dataclass
class DiagonaleSinistra:
    matrix = np.array([[1, 2, 3],  
                        [4, 5, 6],
                        [7, 8, 9]])
    def __init__(self):
        pass
    def diagonale_sinistra(self, matrix = matrix):
        print("\nMatrice iniziale(diagonale da sinistra): \n {}".format(matrix))
        print("\n","Matrice dopo(diagonale da sinistra)","\n",)
        for i in range(len(matrix)):
            for j in range(len(matrix) - i):
                matrix[i][j] = matrix[i][j] 
            print("{}".format(matrix[i][j]), end=" ")        


@dataclass    
class Max:
    x =  np.array([1,2,3,4,5,6,11,7,8,9,10])
    def __init__(self):
        pass
    def max(self,matrix = x):
        print("\n","Matrice iniziale: \n {}".format(matrix))
        max_value = max(matrix)
        print("\n","Il valore massimo della matrice è: ", max_value)
    


@dataclass
class Min: 
    x =  np.array([1,2,3,4,5,6,11,7,8,9,10])
    def __init__(self):
        pass
    def min(self,matrix = x):
        print("\n","Matrice iniziale: \n {}".format(matrix))
        min_value = min(matrix)
        print("\n","Il valore minimo della matrice è: ", min_value)  


@dataclass
class from_negative_to_positive:
    x =  np.array([1,2,3,4,-1,5,6,11,-2,7,8,9,10])
    def __init__(self):
        pass
    def negative_to_positive(self, matrix = x):
        print("\n","Matrice iniziale: \n {}".format(matrix))
        for i in range(len(matrix)):
            if matrix[i] < 0:
                matrix[i] = matrix[i] - matrix[i] - matrix[i]
            print(matrix[i], end=" ")
        print("\n","Matrice dopo \n {}".format(matrix))



@dataclass
class Sum:
    x =  np.array([1,2,3,4,5,6,7,8,9,10])
    def __init__(self):
        pass
    def sum(self,matrix = x):
        print("\n","Matrice iniziale: \n {}".format(matrix))
        somma = 0
        for i in range(len(matrix)):
            somma += matrix[i]
        print("\n","La somma della matrice è: ", somma)


@dataclass
class Mean:
    x =  np.array([1,2,3,4,5,6,7,8,9,10])
    def __init__(self):
        pass
    def mean(self,matrix = x):
        print("\n","Matrice iniziale: \n {}".format(matrix))
        somma = 0
        for i in range(len(matrix)):
            somma = somma + matrix[i]
            y = somma / len(matrix)  
        print("\n","La media della matrice è: ", y)


@dataclass
class StandardDeviation:
    x = np.array([10, 8, 10, 8, 8, 4, 9, 10, 11])
    def __init__(self):
        pass
    def std(self, matrix = x):
        print("\n","Matrice iniziale: \n {}".format(matrix))
        media = sum(matrix) / len(matrix)
        varianza = sum((xi - media) ** 2 for xi in matrix) / len(matrix)
        std = varianza ** 0.5
        print(std)
        print("\n","La deviazione standard della matrice è: ", std)


@dataclass
class ProdottoScalare:
    x = np.array([7, 4, 4, 3, 2])
    b = np.array([5, 3, 4, 3, 2])

    def __init__(self):
        pass

    def prodotto_scalare(self, x = x , b = b):
        print("Matrice 1\n {}".format(x))
        print("\nMatrice 2 \n {}".format(b))
        dot_manuale = 0
        if len(x) != len(b):
            raise ValueError("Le due matrici devono avere la stessa lunghezza per il prodotto scalare.")
        else:
            for a, c in zip(x, b):
                y = a * c
                dot_manuale += y
            print("Il prodotto scalare è: ", dot_manuale)



@dataclass
class SortedArray:
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 11, 21, 10])
    def __init__(self):
        pass
    def sorted_array(self, matrix = x):
        print("Matrice iniziale: \n {}".format(matrix))
        sorted = sorted(matrix)
        print("\n","Matrice dopo: \n {}".format(sorted))


@dataclass
class SortedArrayReverse:
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 11, 21, 10])
    def __init__(self):
        pass
    def sorted_array_reverse(self, matrix = x):
        print("Matrice iniziale: \n {}".format(matrix))
        y  = sorted(matrix)
        reverse = [f for f in y[::-1]]
        print("\n","Matrice dopo: \n {}".format(reverse))


@dataclass
class ZerosArray:
    batch  = int(input("Inserisci un numero di batch: "))
    utente = int(input("Inserisci un numero di righe: "))
    utente2 = int(input("Inserisci un numero di colonne: "))
    def __init__(self):
        pass
    def zeros_array(self,batch = batch, utente = utente, utente2 = utente2):
        x = np.array([0  for _ in range(batch) for _ in range(utente) for _ in range(utente2)]).reshape(batch,utente, utente2)
        print(x)


@dataclass
class OnesArray:
    batch = int(input("Inserisci un numero di batch: "))
    utente = int(input("Inserisci un numero di righe: "))
    utente2 = int(input("Inserisci un numero di colonne: "))
    def __init__(self):
        pass
    def zeros_array(self, batch = batch, utente = utente, utente2 = utente2):
        x = np.array([1 for _ in range(batch) for _ in range(utente) for _ in range(utente2)]).reshape(batch,utente, utente2)
        print(x)


@dataclass
class RandomArray:
    batch = int(input("Inserisci un numero di batch: "))
    utente = int(input("Inserisci un numero di righe: "))
    utente2 =  int(input("Inserisci un numero di colonne: "))
    def __init__(self):
        pass
    def random_array(self,batch = batch , utente = utente, utente2 = utente2):
        import random
        x = np.array([random.randint(0,500) for _ in range(batch) for _ in range(utente) for _ in range(utente2)]).reshape(batch,utente,utente2)
        print(x)


@dataclass
class FULL:
    utente = int(input("Inserisci il numero di colonne: "))
    utente2 = int(input("Inserisci il numero da stampare: "))
    def __init__(self):
        pass
    def full(self, utente = utente , utente2 = utente2):
        x = np.array([utente for _ in range(utente2)])
        print(x)



@dataclass
class ARANGE:
    utente = int(input("Inserisci il numero d'inizio: "))
    utente2 = int(input("Inserisci il numero di fine: "))
    andamento = int(input("inserisci l'incremento: "))
    def __init__(self):
        pass

    def ARANGE(self, utente  = utente , utente2 = utente2 , andamento = andamento):
        y = np.array([b for b in range(utente , utente2, andamento) ])
        print(y)


@dataclass
class LOG10:
    utente =  int(input('Inserisci un  numero per il logaritmo base 10: '))
    def __init__(self):
        pass
    def log10(self, utente = utente):
        import math
        x  = math.log10(utente)
        print(x)


@dataclass
class LOG:
    utente =  int(input('Inserisci un  numero per il logaritmo base : '))
    def __init__(self):
        pass
    def log(self, utente = utente):
        import math
        x  = math.log(utente)
        print(x)


@dataclass
class COS:
    utente =  int(input('Inserisci un  numero per il coseno : '))
    def __init__(self):
        pass
    def cos(self, utente = utente):
        import math
        x  = math.cos(utente)
        print(x)


@dataclass
class SQRT:
    n = int(input("inserisci un numero per la radice quadrata: "))
    def __init__(self):
        pass
    def sqrt(self , n = n):
        if n < 0:
            raise ValueError("Impossibile calcolare la radice quadrata di un numero negativo.")
        if n == 0:
            n = 0
        x = n
        for _ in range(1000):
            prev_x = x
            x = 0.5 * (x + n / x)
            if abs(x - prev_x) < 1e-10 :
                    break
        print(x)


@dataclass
class AROUND:
    utente = int(input("Inserisci primo numero: "))
    utente2= int(input("Inserisci secondo numero: "))
    utente3 = int(input("Inserisci terzo numero: "))
    def __init__(self):
        pass
    def around(self , utente = utente, utente2 = utente2, utente3 = utente3):
        x = np.array((utente , utente2,utente3))
        print(x)



if __name__ == "__main__":
    start = Clip()
    start.clip()
    enter = Transpose()
    enter.transpose()
    diagonale  = Diagonale()
    diagonale.diagonale()
    diagonale_da_sinistra = DiagonaleSinistra()
    diagonale_da_sinistra.diagonale_sinistra()
    max_value = Max()
    max_value.max()
    min_value = Min()
    min_value.min()
    negative_to_positive = from_negative_to_positive()
    negative_to_positive.negative_to_positive()
    somma = Sum()
    somma.sum()
    media = Mean()
    media.mean()
    std = StandardDeviation()
    std.std()
    prodotto_scalare = ProdottoScalare()
    prodotto_scalare.prodotto_scalare()
    sorted_array = SortedArray()
    sorted_array.sorted_array()
    sorted_array_reverse = SortedArrayReverse()
    sorted_array_reverse.sorted_array_reverse()
    zero = ZerosArray()
    zero.zeros_array()
    ones = OnesArray()
    ones.zeros_array()
    random  = RandomArray()
    random.random_array()
    full = FULL()
    full.full()
    arange = ARANGE()
    arange.ARANGE()
    log10 = LOG10()
    log10.log10()
    log = LOG()
    log.log()
    coseno = COS()
    coseno.cos()
    sqrt = SQRT()
    sqrt.sqrt()
    around = AROUND()
    around.around()

        
