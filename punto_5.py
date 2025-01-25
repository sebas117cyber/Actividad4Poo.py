# punto 5

class Datos:
    def __init__(self, Nombre=None, Apellidos=None, Direccion=None, Telefono=None):
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.lista = []
    
    def Agregar(self):
        if self.Nombre == None and self.Apellidos == None and self.Direccion == None and self.Telefono == None:
            print("Por favor, no dejar espacios vacíos.")
            return
        
        Persona = f"{self.Nombre} {self.Apellidos} | Dirección: {self.Direccion} | Teléfono: {self.Telefono}"
        self.lista.append(Persona)
        print("Se agregaron los datos correctamente.")
        return Persona
    
    def EliminarU(self, numero):
        if 0 <= numero < len(self.lista):
            eliminado = self.lista.pop(numero)
            print(f"Se han eliminado los datos de {eliminado}.")
        else:
            print("La posición ingresada no se encuentra en la lista.")

    def EliminarT(self):
        self.lista.clear()
        print("Se han eliminado todos los datos.")
    
    def Mostrarlista(self):
        x = 0
        if len(self.lista) == 0:
            print("La lista está vacía.")
        else:
            print("Lista de Personas:")
            for Persona in (self.lista):
                print(f"{x+1}: {Persona}")
                x += 1
                

sistema = Datos()

respuesta = input("¿Deseas iniciar el sistema?: ").lower()

if respuesta == "si" or respuesta == "sí":
    while True:
        print("Menu de Opciones.")
        print("1- Agregar nuevos datos.")
        print("2- Mostrar la lista.")
        print("3- Eliminar datos (Solo una persona).")
        print("4- Eliminar todos los datos.")
        print("5- Salir")

        Opcion = input("Seleccione una opción: ")

        if Opcion == "1":
            nombre = input("Ingrese el nombre: ")
            apellidos = input("Ingrese los apellidos: ")
            direccion = input("Ingrese la dirección: ")
            telefono = input("Ingrese el teléfono: ")
            persona = Datos(nombre,apellidos,direccion,telefono)
            persona.Agregar()
            sistema.lista.append(persona.Agregar())
        elif Opcion == "2":
            sistema.Mostrarlista()
        elif Opcion == "3":
            sistema.Mostrarlista()
            numero = int(input("Ingrese el numero de la persona a eliminar: "))
            if 0 <= numero - 1 < len(sistema.lista):
                sistema.EliminarU(numero - 1)
            else:
                print("Por favor, ingrese un número que esté en la lista.")
        elif Opcion == "4":
            sistema.EliminarT()
        elif Opcion == "5":
            print("Sistema cerrado correctamente.")
            break
        else:
            print("Ingrese una opción válida para continuar.")
else:
    print("Sistema cerrado correctamente.")