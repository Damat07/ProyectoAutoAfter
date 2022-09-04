from auto.motor import Motor
from auto.auto import Auto
print('**********************************************************************')
print('**********************Consecionaria CoderHouse :D*********************')
print('**********************************************************************')

print('Opciones (1: Construir motor, 2: Fabricar Auto, 3:Comprar Auto)')
opcion = int(input('opcion: '))

if (opcion == 1):
    
    codigoMotor = input('Codigo motor: ')
    nombreMotor = input('Nombre motor: ')
    
    tipoCombustible = input('Tipo de combustible: ')
    cilindrada = input('Cilindrada: ')
    potencia = input('Potencia: ')
    torque = input('Torque: ')

    nuevoMotor = Motor(tipoCombustible, cilindrada, potencia, torque)
    nuevoMotor.setFabricarMotor(codigoMotor,nombreMotor)

elif (opcion == 2):

    codigoAuto = input('Codigo auto: ')
    nombreAuto = input('Nombre auto: ')
    
    ruedas = input('Cant. de ruedas: ')
    puertas = input('Cant. de puertas: ')
    tipo = input('Tipo de auto: ')

    nuevoAuto = Auto(ruedas, puertas, tipo)
    nuevoAuto.getListaMotores()
    codigoMotor = input('Codigo motor: ')
    nuevoAuto.setFabricarAuto(codigoAuto, nombreAuto, codigoMotor)

elif (opcion == 3):

    nuevoAuto = Auto()
    nuevoAuto.getListarAutos()

    codigoAuto = input('Codigo auto: ')

    nuevoAuto.getComprarAuto(codigoAuto)