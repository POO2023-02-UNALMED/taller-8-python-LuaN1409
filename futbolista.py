from deportista import Deportista

class Futbolista(Deportista):
    
    _listaFutbolistas = []
    
    def __init__(self, nombre, edad, altura, sexo, deporte, años, goles, tarjetas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo, "Futbol", años)
        self._golesMarcados = goles
        self._tarjetaRojas = tarjetas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)
    
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self, goles):
        self._golesMarcados = goles
        
    def getTarjetasRojas(self):
        return self._tarjetaRojas
    
    def setTarjetasRojas(self, tarjetas):
        self._tarjetasRojas = tarjetas
        
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
    
    @classmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas
    
    @classmethod
    def setListaFutbolistas(cls, futbolistas):
        cls._listaFutbolistas = futbolistas
        
    def __str__(self):
        cadena = "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.getNombre(), self.getDeporte(), str(self.getEdad()), str(self.getAñosPracticando()))
        return cadena
    
    if __name__ == "__main__":
     futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
     print(futbolista.__str__())
    