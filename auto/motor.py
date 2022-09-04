class Motor:

    def __init__(self, tipoCombustible=None, cilindrada=None, potencia=None, torque=None, ):
        self.tipoCombustible = tipoCombustible
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.torque = torque

    def setFabricarMotor(self, codigoMotor, nombreMotor):
        with open('./auto/recursos/listaMotores.txt','a') as nuevoMotor:
            data = f'{codigoMotor}|{nombreMotor}|{self.tipoCombustible}|{self.cilindrada}|{self.potencia}|{self.torque}\n'
            nuevoMotor.write(data)
            nuevoMotor.close()
            print('Motor creado')
    def  getObtenerMotor(self, codigoMotor):
        with open('./auto/recurso/listaMotores.txt','r') as motores:
            for motor in motores:
                detalles = motor.split('|')
                if (codigoMotor == detalles[0]):
                    motores.close()
                    return detalles
                else:
                    motores.close()
                    return 'Motor no encontrado'

    def getListaMotores(self):
        with open('./auto/recursos/listaMotores.txt','r') as motores:
            for motor in motores:
                print(motor)
                
        