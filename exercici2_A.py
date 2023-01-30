'''
Funció on demanarà que insereixin un nom dels 5 que es proposin.
Depenent del nom que indiqui s’hi mostrarà, per consola, un missatge diferent.
Si es passa un nom no adeqüat s’ha d’indicar que el nom no està a la llista.
'''

def cincNoms():
    #DEMANO EL VALOR DEL USUARI
    llistaNoms = ["Escolastica", "Marina", "Eulalia", "Josep Maria", "Juan Daniel"]

    print("Aqui hi han la llista amb els noms seleccionats: ",  llistaNoms)

    #DEMANO AL USUARI EL NOM QUE ESCULL
    nom = input("Inserta el nom: ")

    if(nom == llistaNoms[0]): #ESCOLASTICA
        missatgeNoms = "La {a} és la dona casada amb el sabater, tots dos d'origen extremeny".format(a=nom)
    elif (nom == llistaNoms[1]): #MARINA
        missatgeNoms = "La {a} és la més simpatica de les germanes".format(a=nom)
    elif (nom == llistaNoms[2]): #EULALIA
        missatgeNoms = "La {a} és la més queixica de tota la familia".format(a=nom)
    elif (nom == llistaNoms[3]): #JOSEP MARIA
        missatgeNoms = "El {a} està amb el seu Xoco".format(a=nom)
    elif (nom == llistaNoms[4]): #JUAN DANIEL
        missatgeNoms = "El {a} mai es presenta com a tal, sempre Dany".format(a=nom)
    else: #QUALSEVOL ALTRE
        missatgeNoms ="{a} no existeix dins de la llista, ens sap greu.".format(a=nom)


    return missatgeNoms
