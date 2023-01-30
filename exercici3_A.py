'''
En aquest arxiu s’hi crearà una funció la qual li demanarà al client que indiqui un número entre 0 i 100 (utilitzar random.randange()):
Si endevina el número li sortirà un missatge de “Molt bé! Has endevinat el número!”
Si no endevina té dues opcions:
Que el número, indicat per l’usuari,sigui més petit. En aquest cas, el missatge serà
        “El número és més gran”. Tornarà a preguntar a l’usuari el nou número.
Que el número, indicat per l’usuari, sigui més gran. En aquest cas, el missatge serà
        “El número és més petit”: Tornarà a preguntar a l’usuari el nou número.
'''

import random

def rand100():
    numero = random.randrange(0, 101)

    numUsuari = int(input("Quin numero creus que ha sortit? "))

    if(numero==numUsuari):
        missatge = "Molt bé! Has endevinat el número.".format(a=numero)
    elif(numero<numUsuari):
        missatge = "El número es menor que el número escollit: {a} ".format(a=numUsuari)
    else:
        missatge = "El número es major que el número escollit: {a} ".format(a=numUsuari)


    return missatge
