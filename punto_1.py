# Ejercicio 4.1

class cuentabancaria():
    def __init__(self, Saldo,  Tasaanual):
        self.Saldo = Saldo
        self.Numconsigna = 0
        self.Numretiros = 0
        self.Tasaanual = Tasaanual
        self.Comisionmes = 0.0

    def consignar(self, Canti: float):
        if Canti >= 0:
            self.Saldo += Canti
            self.Numconsigna += 1
        else:
            print("El valor a consignar no es valido")

    def retirar(self, Cantidad: float):
        if Cantidad <= self.Saldo:
            self.Saldo -= Cantidad
            self.Numretiros += 1
        else:
            print("El valor de retiro supera su saldo")
    
    def calinteres(self):
        mesInteres = (self.Saldo * self.Tasaanual) / 12
        return mesInteres

    def extracto(self):
        self.Saldo -= self.Comisionmes
        ganainter = self.calinteres()
        self.Saldo += ganainter
        return self.Comisionmes

    def Imprecion(self):
        print(f"Saldo disponible: $ {round(self.Saldo, 2)}")
        print(f"# de consignaciones: {self.Numconsigna}")
        print(f"# de retiros: {self.Numretiros}")
        print(f"Comision por mes: ${round(self.Comisionmes, 2)}")

class cuentaAhorros(cuentabancaria):
    def __init__(self, Saldo, Tasaanual):
        super().__init__(Saldo, Tasaanual)
        self.Veractivo = self.Saldo >= 10000

    def consignar(self, Cantidad: float):
        if self.Veractivo:
            super().consignar(Cantidad)
        else:
            print("su cuenta no se encuentra activa")

    def retirar(self, Cantidad: float):
        if self.Veractivo:
            super().retirar(Cantidad)
        else:
            print("su cuenta no se encuentra activa")

    def extracto(self):
        if self.Numretiros > 4:
            self.Comisionmes += (self.Numretiros - 4) * 1000
        super().extracto()
    
    def Imprecion(self):
        super().Imprecion()
        if self.Veractivo == True:
            print("Su cuenta esta activa")
        else:
            print("su cuenta esta inactiva")

class cuentaCorriente(cuentabancaria):
    def __init__(self, Saldo, Tasaanual):
        super().__init__(Saldo, Tasaanual)
        self.Sobregiro = 0.0

    def retirar(self, Cantidad: float):
        if Cantidad <= self.Saldo:
            super().retirar(Cantidad)
        else:
            deuda = Cantidad - self.Saldo
            self.Sobregiro += deuda
            self.Saldo = 0
            self.Numretiros += 1

    def consignar(self, Cantidad: float):
        if self.Sobregiro > 0:
            if Cantidad >= self.Sobregiro:
                Cantidad -= self.Sobregiro
                self.Sobregiro = 0
            else:
                self.Sobregiro -= Cantidad
                Cantidad = 0
        super().consignar(Cantidad)

    def Imprecion(self):
        super().Imprecion()
        print(f"valor en deuda: ${round(self.Sobregiro)}")


micuenta = cuentaAhorros(20000, 4.6)
micuenta.consignar(530000)
micuenta.consignar(5000)
micuenta.retirar(54000)
micuenta.retirar(4000)
micuenta.retirar(15000)
micuenta.retirar(25000)
micuenta.retirar(2000)
micuenta.retirar(24000)
micuenta.extracto()
micuenta.Imprecion()

''''
corriente = cuentaCorriente(45000, 6.2)
corriente.consignar(20000)
corriente.retirar(100000)
corriente.Imprecion()
'''