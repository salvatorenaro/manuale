import numpy as np
import logging
import sys
import math
import random
from dataclasses import dataclass
import platform
import socket
import geocoder
import webbrowser
from googletrans import Translator
import locale


"""IMPLEMENTAZIONE MANUALE DI MOLTE FUNZIONALITA DI NUMPY CODICE SVILUPPATO DA SALVATORE NARO ANCORA IN FASE DI SVILUPPO"""


  
@dataclass
class NumpyFunctions:        

    @staticmethod
    def version_python():
        try:
            REQUIRED_PYTHON_VERSION = (3,6)
            if sys.version_info < REQUIRED_PYTHON_VERSION:
                logging.error(f"Versione Python non supportata \n {sys.version}  \n   la tua versione")
                webbrowser.open("https://www.python.org/downloads/")
                sys.exit(1)
            else:
                nome_utente = socket.gethostname()
                version  = sys.version
                piattaforma = platform.system().lower()
                ip  = geocoder.ip('me')
                logging.warning("Versione Python Supportata \n {}".format(version))
                if piattaforma == 'windows':
                    print("Benvenuto da Windows, ",nome_utente,"!","Nazionalita: ", ip.country,  " , " , "Citta: ", ip.city)
                elif piattaforma == 'linux':
                    print("Benvenuto da Linux, ",nome_utente,"!","Nazionalita: ", ip.country," , ", "Citta: ", ip.city)
                elif piattaforma == 'darwin':
                    print(" Benvenuto da IOS, ",nome_utente,"!","Nazionalita: ", ip.country," , " ,"Citta: ", ip.city)
                else :
                    print(" Benvenuto da {}".format(piattaforma),nome_utente,"Nazionalita: ", ip.country, " , " , "Citta", ip.city)
        except Exception as e:
            logging.error(f"Errore {e}")


    @staticmethod
    def traduzione(messaggio):
            lingua = locale.getdefaultlocale()[0][:2]
            if lingua != 'it':
                translator = Translator()
                traduzione  = translator.translate(messaggio, dest=lingua)
                return traduzione.text
            return messaggio
    

    @staticmethod
    def clip():
        while True:
            controllo = ["Inserisci un numero", "Perfavore digiti un numero", "E richiesto un numero non una stringa"]
            controllo_numero = ['Numero di fine non puo essere minore del numero di inizio','Il numero di fine è minore,si prega di inserire un numero maggiore']
            frase_casuale = np.random.choice(controllo) 
            frase_casuale_numero = np.random.choice(controllo_numero)
            print("La matrice va da 0 a 9")
            utente = input("Inserisci un numero d'inizio: ")
            fine = input("Inserisci un numero di fine: ")
            try:
                if utente.isdigit() and fine.isdigit():
                    if int(fine) < int(utente):
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
                logging.error("Errore {}".format(e))
        
        array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y = []
        for i in range(0, len(array)):
            if array[i] > fine:
                array[i] = fine
            elif array[i] < utente:
                array[i] = utente
            y.append(array[i])
        print(y)

    

    @staticmethod
    def transpose():
        try:
            matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            copy = np.copy(matrix)
            print("\nMatrice iniziale:\n", matrix)
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    copy[i][j] = matrix[j][i]
            print("\nMatrice trasposta:\n", copy)
        except Exception as e:
            logging.error(f'Errore {e}')



    @staticmethod
    def diagonale():
        try:
            matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            print("Matrice iniziale (diagonale da destra):\n", matrix)
            print("\nDiagonali:")
            for i in range(len(matrix)):
                for j in range(i + 1):
                    matrix[i][j]  = matrix[i][j]
                print("{}".format(matrix[i][j]), end=" ")
        except Exception as e :
            logging.error(f'Errore{e}')

            

    @staticmethod
    def diagonale_sinistra():
        try  :
            matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            print("\nMatrice iniziale (diagonale da sinistra):\n", matrix)
            print("\nDiagonali:")
            for i in range(len(matrix)):
                for j in range(len(matrix) - i):
                    matrix[i][j]  = matrix[i][j]
                print("{}".format(matrix[i][j]), end=" ")        
        except Exception as e:
            logging.error(f'Errore {e}')

            

    @staticmethod
    def max():
        try:
            x = np.array([1,2,3,4,5,6,11,7,8,9,10])
            print("\nArray Iniziale \n {}".format(x))
            max_value = max(x)
            print("\n","Il valore massimo della matrice è: ", max_value)
        except Exception as e:
            logging.error(f'Errore {e}')



    @staticmethod
    def min():
        try:
            x = np.array([1,2,3,4,5,6,11,7,8,9,10])
            print("\nArray Iniziale \n {}".format(x))
            min_value = min(x)
            print("\n","Il valore minimo della matrice è: ", min_value)
        except Exception as e:
            logging.error(f'Errore {e}')



    @staticmethod
    def negative_to_positive():
        try:
            matrix = np.array([1,2,3,4,-1,5,6,11,-2,7,8,9,10])
            print("\nArray originale:", matrix)
            for i in range(len(matrix)):
                if matrix[i] < 0:
                    matrix[i] = matrix[i] - matrix[i] - matrix[i]
                print(matrix[i], end=" ")
            print("\n","Matrice dopo \n {}".format(matrix))
        except Exception as e:
            logging.error(f'Errore {e}')
        


    @staticmethod
    def sum():
        try:
            matrix = np.array([1,2,3,4,5,6,7,8,9,10])
            print("\nArray:", matrix)
            somma = 0
            for i in range(len(matrix)):
                somma += matrix[i]
            print("\n","La somma della matrice è: ", somma)
        except Exception as e:
            logging.error(f'Errore {e}')

     

    @staticmethod
    def mean():
        try:
            matrix =  np.array([1,2,3,4,5,6,7,8,9,10])
            print("\n","Matrice iniziale: \n {}".format(matrix))
            somma = 0
            for i in range(len(matrix)):
                somma = somma + matrix[i]
                y = somma / len(matrix)  
            print("\n","La media della matrice è: ", y)
        except Exception as e:
            logging.error(f'Errore {e}')
        


    @staticmethod
    def std():
        try:
            x = np.array([10, 8, 10, 8, 8, 4, 9, 10, 11])
            media = sum(x) / len(x)
            varianza = sum((xi - media) ** 2 for xi in x) / len(x)
            std = varianza ** 0.5
            print("\nArray:", x)
            print("Deviazione standard:", std)
        except Exception as e:
            logging.error(f'Errore {e}')

  


    @staticmethod
    def prodotto_scalare():
        try:
            x = np.array([7, 4, 4, 3, 2])
            b = np.array([5, 3, 4, 3, 2])
            if len(x) != len(b):
                raise ValueError("Le due matrici devono avere la stessa lunghezza per il prodotto scalare.")
            else:
                dot_manuale =  0
                for a, c in zip(x, b):
                    y = a * c
                    dot_manuale += y
                print("Il prodotto scalare è: ", dot_manuale)
        except Exception as e:
            logging.error(f'Error {e}')



    @staticmethod
    def sort():
        try  :
            x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 11, 21, 10])
            print("\nArray originale:", x)
            y = sorted(x)
            print("Ordinato:", y)
        except Exception as e:
            logging.error(f'Error {e}')



    @staticmethod
    def sorted_Array_Reverse():
        try:
            x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 11, 21, 10])
            print("Matrice iniziale: \n {}".format(x))
            y  = sorted(x)
            reverse = [f for f in y[::-1]]
            print("\n","Matrice dopo: \n {}".format(reverse))
        except Exception as e:
            logging.error(f'Error {e}')



   
    @staticmethod
    def zeros_array():
        try : 
            batch = int(input("\nInserisci numero di batch: "))
            righe = int(input("Inserisci numero di righe: "))
            colonne = int(input("Inserisci numero di colonne: "))
            x = np.array([0  for _ in range(batch) for _ in range(righe) for _ in range(colonne)]).reshape(batch,righe, colonne)
            print(x)
        except Exception as e:
            logging.error(f'Errore {e}')



    @staticmethod
    def ones_array():
        try:
            batch = int(input("\nInserisci numero di batch: "))
            righe = int(input("Inserisci numero di righe: "))
            colonne = int(input("Inserisci numero di colonne: "))
            x = np.array([1 for _ in range(batch) for _ in range(righe) for _ in range(colonne)]).reshape(batch,righe, colonne)
            print(x)
        except Exception as e:
            logging.error(f'Error {e}')



    @staticmethod
    def random_array():
        try:
            batch = int(input("\nInserisci numero di batch: "))
            righe = int(input("Inserisci numero di righe: "))
            colonne = int(input("Inserisci numero di colonne: "))
            x = np.array([random.randint(0,500) for _ in range(batch) for _ in range(righe) for _ in range(colonne)]).reshape(batch,righe,colonne)
            print(x)
        except Exception as e:
            logging.error(f'Error {e}')




    @staticmethod
    def full_array(): 
        try:    
            colonne = int(input("Inserisci numero di colonne: "))
            stampa = int(input("Inserisci il numero da stampare: "))
            x = np.array([colonne for _ in range(stampa)])
            print(x)
        except Exception as e:
            logging.error(f'Error {e}')




    @staticmethod
    def arange():
        try:
            start = int(input("\nInserisci numero iniziale: "))
            stop = int(input("Inserisci numero finale: "))
            step = int(input("Inserisci incremento: "))
            y = np.array([b for b in range(start , stop, step) ])
            print(y)
        except Exception as e:
            logging.error(f'Error {e}')

   
   
   
    @staticmethod
    def log10():
        try:
            num = int(input("\nInserisci numero per log10: "))
            print(math.log10(num))
        except Exception as e:
            logging.error(f'Error {e}')

  
  
    @staticmethod
    def log():
        try:
            num = int(input("\nInserisci numero per log: "))
            print(math.log(num))
        except Exception as e:
            logging.error(f'Error {e}')

 
 
    @staticmethod
    def cos():
        try:
            num = int(input("\nInserisci numero per coseno: "))
            print(math.cos(num))
        except Exception as e:
            logging.error(f'Error {e}')



    @staticmethod
    def sqrt():
        try:
            n = int(input("\nInserisci numero per radice quadrata: "))
            if n < 0:
                raise ValueError("Numero negativo")
            x = n
            for _ in range(1000):
                prev_x = x
                x = 0.5 * (x + n / x)
                if abs(x - prev_x) < 1e-10:
                    break
            print(x)
        except Exception as e:
            logging.error(f'Error {e}')

  
    
    @staticmethod
    def around():
        try:
            utente = int(input("Inserisci primo numero: "))
            utente2= int(input("Inserisci secondo numero: "))
            utente3 = int(input("Inserisci terzo numero: "))
            x = np.array((utente , utente2,utente3))
            print(x)
        except Exception as e:
              logging.error(f'Error {e}')




if __name__ == "__main__":
    np_func = NumpyFunctions()
    np_func.traduzione('Benvenuto nel mio codice ')
    np_func.version_python()
    np_func.clip()
    np_func.transpose()
    np_func.diagonale()
    np_func.diagonale_sinistra()
    np_func.max()
    np_func.min()
    np_func.mean()
    np_func.sorted_Array_Reverse()
    np_func.negative_to_positive()
    np_func.sum()
    np_func.std()
    np_func.prodotto_scalare()
    np_func.sort()
    np_func.zeros_array()
    np_func.ones_array()
    np_func.random_array()
    np_func.full_array()
    np_func.arange()
    np_func.log10()
    np_func.log()
    np_func.cos()
    np_func.sqrt()
    np_func.around()
