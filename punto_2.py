class Inmuebles:
    def __init__(self,Id,Area,Dir,Pm):
        self.Id = Id
        self.Area = Area
        self.Dir =  Dir
        self.Pm = Pm
    def CalcularPrecioVenta(self):
        Precioventa = self.Area*self.Pm
        return Precioventa
    def datos1(self):
        print(f"Identificador Inmobiliario: {self.Id}")
        print(f"Área: {self.Area} m²")
        print(f"Dirección: {self.Dir}")
        print(f"Precio de Venta: ${round(self.CalcularPrecioVenta(),2)}")


class InmuebleVi(Inmuebles):
    def __init__(self, Id, Area, Dir, Pm, NumeroH, NumeroB):
        super().__init__(Id, Area, Dir, Pm)
        self.NumeroH = NumeroH
        self.NumeroB = NumeroB
    def datos2(self):
        super().datos1()
        print(f"Numero de Habitaciones: {self.NumeroH}")
        print(f"Numero de Baños: {self.NumeroB}")


class Casa(InmuebleVi):
    def __init__(self, Id, Area, Dir, Pm, NumeroH, NumeroB, NumeroP):
        super().__init__(Id, Area, Dir, Pm, NumeroH, NumeroB)
        self.NumeroP = NumeroP
    def datos3(self):
        super().datos2()
        print(f"Numero de Pisos: {self.NumeroP}")

class Apartamento(InmuebleVi):
    def __init__(self, Id, Area, Dir, Pm, NumeroH, NumeroB):
        super().__init__(Id, Area, Dir, Pm, NumeroH, NumeroB)
    def datos4(self):
        super().datos2()

class CasaR(Casa):
    def __init__(self, Id, Area, Dir, NumeroH, NumeroB, NumeroP,DistCabera,Alt):
        super().__init__(Id, Area, Dir, 1500000, NumeroH, NumeroB,NumeroP)
        self.DistCabera = DistCabera
        self.Alt = Alt
    def datos(self):
        super().datos3()
        print(f"Distancia de la Cabecera Municipal: {self.DistCabera}")
        print(f"Altitud: {self.Alt}")

class CasaU(Casa):
    def __init__(self, Id, Area, Dir, Pm, NumeroH, NumeroB, NumeroP):
        super().__init__(Id, Area, Dir, Pm, NumeroH, NumeroB,NumeroP)
    def datos5(self):
        super().datos3()

class ApartamentoFamiliar(Apartamento):
    def __init__(self, Id, Area, Dir, NumeroH, NumeroB,PrecioAdmin):
        super().__init__(Id, Area, Dir, 2000000, NumeroH, NumeroB)
        self.PrecioAdmin = PrecioAdmin
    def datos(self):
        super().datos4()
        print(f"Precio de Administración: ${round(self.PrecioAdmin,2)}")

class ApartaEstudio(Apartamento):
    def __init__(self, Id, Area, Dir, PrecioAdmin):
        super().__init__(Id, Area, Dir, 1500000, 1, 1)
    def datos(self):
        super().datos4()

class CasaCC(CasaU):
    def __init__(self, Id, Area, Dir, NumeroH, NumeroB, NumeroP,PrecioAdmin,Piscina,CampDepor):
        super().__init__(Id, Area, Dir, 2500000, NumeroH, NumeroB,NumeroP)
        self.PrecioAdmin = PrecioAdmin
        self.Piscina = Piscina
        self.CampDepor = CampDepor
    def datos(self):
        super().datos5()
        print(f"Precio de Administración: ${round(self.PrecioAdmin,2)}")
        print(f"¿Tiene Piscina?: {self.Piscina}")
        print(f"¿Tiene Campos Deportivos?: {self.CampDepor}")

class CasaIndep(CasaU):
    def __init__(self, Id, Area, Dir, NumeroH, NumeroB, NumeroP):
        super().__init__(Id, Area, Dir, 3000000, NumeroH, NumeroB,NumeroP)
    def datos(self):
        super().datos5()


class Local(Inmuebles):
    def __init__(self, Id, Area, Dir,Pm, Tipo):
        super().__init__(Id, Area, Dir,Pm)
        self.Tipo = Tipo
    def datos6(self):
        super().datos1()
        print(f"Tipo de Local: {self.Tipo}")

class LocalComercial(Local):
    def __init__(self, Id, Area, Dir, Tipo, CentroC):
        super().__init__(Id, Area, Dir,3000000,Tipo)
        self.CentroC = CentroC
    def datos(self):
        super().datos6()
        print(f"Centro Comercial: {self.CentroC}")

class  Oficina(Local):
      def __init__(self, Id, Area, Dir, Tipo, EsGobierno):
        super().__init__(Id, Area, Dir,3500000,Tipo)
        self.EsGobierno = EsGobierno
        def datos(self):
            super().datos6()
            print(f"¿Es Oficina Gubernamental?: {self.EsGobierno}")



nuevo = ApartamentoFamiliar(103067,120,"Avenida Santander 45-45",3,2,200000)
nuevo.datos()