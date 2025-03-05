from abc import ABC, abstractmethod

# Clase abstracta Pokemon
class Pokemon(ABC):
    def __init__(self, num_pokedex, nombre, peso, sexo, temporada, tipo):
        self.num_pokedex = num_pokedex
        self.nombre = nombre
        self.peso = peso
        self.sexo = sexo
        self.temporada = temporada
        self.tipo = tipo

    def atacarPlacaje(self):
        print(f"Soy {self.nombre} y estoy atacando con Placaje.")
    
    def atacarArañazo(self):
        print(f"Soy {self.nombre} y estoy atacando con Arañazo.")
    
    def atacarMordisco(self):
        print(f"Soy {self.nombre} y estoy atacando con Mordisco.")

# Interfaces de ataques
class IElectrico(ABC):
    def atacarImpactrueno(self):
        print(f"Soy {self.nombre} y estoy atacando con Impactrueno.")
    
    def atacarPunioTrueno(self):
        print(f"Soy {self.nombre} y estoy atacando con Puño Trueno.")
    
    def atacarRayo(self):
        print(f"Soy {self.nombre} y estoy atacando con Rayo.")
    
    def atacarRayoCarga(self):
        print(f"Soy {self.nombre} y estoy atacando con Rayo Carga.")

class IPlanta(ABC):
    def atacarParalizar(self):
        print(f"Soy {self.nombre} y estoy atacando con Paralizar.")
    
    def atacarDrenaje(self):
        print(f"Soy {self.nombre} y estoy atacando con Drenaje.")
    
    def atacarHojaAfilada(self):
        print(f"Soy {self.nombre} y estoy atacando con Hoja Afilada.")
    
    def atacarLatigoCepa(self):
        print(f"Soy {self.nombre} y estoy atacando con Látigo Cepa.")

class IFuego(ABC):
    def atacarPunioFuego(self):
        print(f"Soy {self.nombre} y estoy atacando con Puño Fuego.")
    
    def atacarAscuas(self):
        print(f"Soy {self.nombre} y estoy atacando con Ascuas.")
    
    def atacarLanzallamas(self):
        print(f"Soy {self.nombre} y estoy atacando con Lanzallamas.")

class IAgua(ABC):
    def atacarHidrobomba(self):
        print(f"Soy {self.nombre} y estoy atacando con Hidrobomba.")
    
    def atacarPistolaAgua(self):
        print(f"Soy {self.nombre} y estoy atacando con Pistola de Agua.")
    
    def atacarBurbuja(self):
        print(f"Soy {self.nombre} y estoy atacando con Burbuja.")
    
    def atacarHidropulso(self):
        print(f"Soy {self.nombre} y estoy atacando con Hidropulso.")

# Clases de Pokémon
class Pikachu(Pokemon, IElectrico):
    def __init__(self):
        super().__init__(25, "Pikachu", 6, "Macho", 1, "Eléctrico")

class Charmander(Pokemon, IFuego):
    def __init__(self):
        super().__init__(4, "Charmander", 8.5, "Macho", 1, "Fuego")

class Bulbasaur(Pokemon, IPlanta):
    def __init__(self):
        super().__init__(1, "Bulbasaur", 6.9, "Macho", 1, "Planta")

class Squirtle(Pokemon, IAgua):
    def __init__(self):
        super().__init__(7, "Squirtle", 9, "Macho", 1, "Agua")

# Crear instancias de los Pokémon
pikachu = Pikachu()
charmander = Charmander()
bulbasaur = Bulbasaur()
squirtle = Squirtle()

# Llamar a los métodos
pikachu.atacarPlacaje()
pikachu.atacarImpactrueno()

charmander.atacarArañazo()
charmander.atacarLanzallamas()

bulbasaur.atacarMordisco()
bulbasaur.atacarHojaAfilada()

squirtle.atacarPlacaje()
squirtle.atacarHidrobomba()
