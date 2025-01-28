# punto 3 ejercicio practica 4

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,nombre_cientifico, sonido, alimentos, habitat):
        self.nombre_cientifico = nombre_cientifico
        self.sonido = sonido
        self.alimentos = alimentos
        self.habitat = habitat

    @abstractmethod
    def nombre_cientifico2(self):
        pass

    @abstractmethod
    def sonido2(self):
        pass

    @abstractmethod
    def alimentos2(self):
        pass

    @abstractmethod
    def habitat2(self):
        pass

class Canido(Animal):
    def __init__(self,nombre_cientifico, sonido, alimentos, habitat):
        super().__init__(nombre_cientifico, sonido, alimentos, habitat)
    def nombre_cientifico2(self):
        return self.nombre_cientifico
    def sonido2(self):
        return self.sonido
    def alimentos2(self):
        return self.alimentos
    def habitat2(self):
        return self.habitat

class Felino(Animal):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat):
        super().__init__(nombre_cientifico, sonido, alimentos, habitat)
    def nombre_cientifico2(self):
        return self.nombre_cientifico
    def sonido2(self):
        return self.sonido
    def alimentos2(self):
        return self.alimentos
    def habitat2(self):
        return self.habitat


class Gato(Felino):
    def __init__(self):
        super().__init__("Felis silvestris catus", "Maullido", "Ratones", "Domestico" )
       
class Perro(Canido):
    def __init__(self):
        super().__init__("Canis lupus familiaris", "Ladrido", "Carnivoro","Domestico")
       
class Lobo(Canido):
    def __init__(self):
        super().__init__("Canis lupus", "Aullido", "Carnivoro", "Bosque")

class Leon(Felino):
    def __init__(self):
        super().__init__("Panthera leo", "Rugido", "Carnivoro", "Pradera")
       
if __name__ == "__main__":
    animales = [Gato(),Perro(),Lobo(),Leon()]
    for animal in animales:
        print(animal.nombre_cientifico2())
        print("Sonido:", animal.sonido2())
        print("Alimentos:", animal.alimentos2())
        print("Habitat:", animal.habitat2())
        print(" ")