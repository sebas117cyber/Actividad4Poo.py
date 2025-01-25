# punto 4 ejercicio 4.4

from abc import ABC, abstractmethod


class Ciclista(ABC):
    def __init__(self, ID, Nombre, Acumtiempo: float = 0):
        self.ID = ID
        self.Nombre = Nombre
        self.AcumTiempo = Acumtiempo

    def IDENT(self):
        return self.ID

    def NOM(self):
        return self.Nombre

    def Acumtiempo(self):
        return self.AcumTiempo

    def tiempoAcumu(self, Tiempo):
        self.AcumTiempo = Tiempo

    @abstractmethod
    def impreDat(self):
        pass

    @abstractmethod
    def impretipo(self):
        pass


class Velocista(Ciclista):
    def __init__(self, ID, Nombre, Acumtiempo: float, PotenMedia: float, VeloMedia: float):
        super().__init__(ID, Nombre, Acumtiempo)
        self.PotenMedia = PotenMedia
        self.VeloMedia = VeloMedia

    def Potenciamed(self):
        return self.PotenMedia

    def potenciaset(self, Potencia):
        self.PotenMedia = Potencia

    def Velomediaget(self):
        return self.VeloMedia

    def VelomediaSet(self, mediavelos):
        self.VeloMedia = mediavelos

    def impreDat(self):
        print(f"ID: {self.ID}\nNombre: {self.Nombre}\n"
              f"Potencia promedio: {self.PotenMedia}N\n"
              f"Velocidad promedio: {self.VeloMedia} km/h")

    def impretipo(self):
        return "Es Velocista"


class Escalador(Ciclista):
    def __init__(self, ID, Nombre, Acumtiempo: float, AceleraMedia: float, RampaGra: float):
        super().__init__(ID, Nombre, Acumtiempo)
        self.AceleraMedia = AceleraMedia
        self.RampaGra = RampaGra

    def AceleraGet(self):
        return self.AceleraMedia

    def AceleraSet(self, MediaAcelera):
        self.AceleraMedia = MediaAcelera

    def RampaGet(self):
        return self.RampaGra

    def RampaSet(self, Grado):
        self.RampaGra = Grado

    def impreDat(self):
        print(f"ID: {self.ID}\nNombre: {self.Nombre}\n"
              f"Aceleración promedio: {self.AceleraMedia} m/s²\n"
              f"Rampa soportada: {self.RampaGra}°")

    def impretipo(self):
        return "Es Escalador"


class Contrarreloj(Ciclista):
    def __init__(self, ID, Nombre, Acumtiempo: float, VelMax: float):
        super().__init__(ID, Nombre, Acumtiempo)
        self.VelMax = VelMax

    def velmaxGet(self):
        return self.VelMax

    def tiempoAcumu(self, VelMaxima):
        self.VelMax = VelMaxima

    def impreDat(self):
        print(f"ID: {self.ID}\nNombre: {self.Nombre}\n"
              f"Velocidad máxima: {self.VelMax} km/h")

    def impretipo(self):
        return "Es Contrarreloj"


class GruposCiclis:
    SumaCiclistas = 0

    def __init__(self, Nombrequip, Pais):
        self.Nombrequip = Nombrequip
        self.Pais = Pais
        self.Ciclislist = []

    def Equipoget(self):
        return self.Nombrequip

    def Equiposet(self, Nombrequi):
        self.Nombrequip = Nombrequi

    def Paisget(self):
        return self.Pais

    def Paisset(self, Paisorigen):
        self.Pais = Paisorigen

    def añadir(self, ciclista: Ciclista):
        self.Ciclislist.append(ciclista)
        self.totalTiempo()

    def totalTiempo(self):
        GruposCiclis.SumaCiclistas = sum(i.Acumtiempo() for i in self.Ciclislist)

    def sumaGet(self):
        return GruposCiclis.SumaCiclistas

    def listaNombres(self):
        return [i.NOM() for i in self.Ciclislist]

    def Busqueda(self, ID):
        for i in self.Ciclislist:
            if i.IDENT() == ID:
                i.impreDat()
                return
        print("Ciclista no encontrado")

    def imprequipo(self):
        print(f"Equipo: {self.Nombrequip}\nPaís: {self.Pais}\n"
              f"Suma de tiempos: {GruposCiclis.SumaCiclistas} minutos\n")
        print("Ciclistas:")
        for ciclista in self.Ciclislist:
            print(f"- {ciclista.NOM()}")


Equipo = GruposCiclis("Macondo", "Siberia")
velocista = Velocista(2, "Ramiro Aguirre", 54, 12, 45)
escalador = Escalador(4, "Yamile Hincapié", 76, 21, 25)
contrarreloj = Contrarreloj(3, "Paul Lennon", 32, 56)
participante75 = Velocista(75, "Julian Piedra", 243, 21, 62)

Equipo.añadir(participante75)
Equipo.añadir(velocista)
Equipo.añadir(escalador)
Equipo.añadir(contrarreloj)

Equipo.imprequipo()

try:
    numbusca = int(input("Ingrese el ID del ciclista deseado: "))
    Equipo.Busqueda(numbusca)
except ValueError:
    print(" El ID ingresado debe ser entero")
