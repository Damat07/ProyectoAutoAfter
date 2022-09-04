from auto.motor import Motor


class Auto(Motor):

    def __init__(self, ruedas=None, puertas=None, tipo=None):
        self.ruedas = ruedas
        self.puertas = puertas
        self.tipo = tipo 

    def setFabricarAuto(self, codigoAuto, nombreAuto, codigoMotor):
        with open('./auto/recursos/listaAutos.txt','a') as nuevoAuto:
            data = f'{codigoAuto}|{nombreAuto}|{self.ruedas}|{self.puertas}|{self.tipo}|{codigoMotor}\n'
            nuevoAuto.write(data)
            nuevoAuto.close()
    def getComprarAuto(self, codigoAuto):
        with open('./auto/recursos/listaAutos.txt','r') as autos:
            for auto in autos:
                detalles = auto.split('|')
                if (codigoAuto == detalles[0]):
                    autos.close()
                    print(f'Compraste un {detalles[1]}')
                    break
            else:
                autos.close()
                return 'Auto no encontrado'

    def getListarAutos(self):
        with open('./auto/recursos/listaAutos.txt','r') as autos:
            for auto in autos:
                print(auto)