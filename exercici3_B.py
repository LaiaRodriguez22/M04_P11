"""
En este programa te pedirá que ingreses tu edad y tus ingresos, dependiendo de ello
te retornará si es necesario que hagas la declaración o NO.
"""
def Hacienda ():
    edad = int(input("Introduce tu edad: ")) #Variable para almacenar la edad
    ingresos = int(input("Introduce tus ingresos: ")) # Variable para almacenar los ingresos
    if(edad>=18 and ingresos>1200): # Si los ingresos y la edad son mayores a unos valores determinados:
        mensaje = ("Es necesario que hagas la declaración, ya que tienes {edad} y tus ingresos son de {ingresos}".format(edad=edad,ingresos=ingresos))
    else:
        mensaje = ("Aun no puedes hacer la declaración")
    return mensaje
