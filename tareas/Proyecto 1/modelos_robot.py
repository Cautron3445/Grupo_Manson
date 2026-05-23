from Robot_base import RobotBase
import random

class RobotTresRuedas(RobotBase):
    def __init__(self, nombre, radio_rueda):
        super().__init__(nombre, 20.0)
        self.ruedas_calibradas = False
        self.radio_rueda = radio_rueda

    def calibrar_giro(self):
        print(f"[{self.nombre()}] Calibrando giro con radio de rueda: {self.radio_rueda} ")
        self.ruedas_calibradas = True

    def mover(self):
        return self.step(v=0.8, w=0.2)

    def limpiar(self):
        self._reducir_bateria(2.0)
        cantidad_basura = random.uniform(0.5, 1.5)
        self._recolectar_basura(cantidad_basura)

class RobotOruga(RobotBase):
    def __init__(self, nombre, tension_oruga):
        super().__init__(nombre,50.0)
        self.tension_oruga = tension_oruga

    def ajustar_tension(self):
        print(f"[{self.get_nombre()}] Ajustando la tension de la oruga a {self.tension_oruga}.")

    def mover(self):
        return self.step(v=0.3, w=0.8)

    def limpiar(self):
        self._reducir_bateria(4.5)
        cantidad_basura = random.uniform(2.0,4.0)
        self._recolectar_basura(cantidad_basura)

class RobotDron(RobotBase):
    def __init__(self, nombre, altura_maxima):
        super().__init__(nombre, 5.0)
        self.altura_maxima = altura_maxima
        self.en_vuelo = False

    def despegar(self):
        print(f"[{self.get_nombre()}] Despegando a {self.altura_maxima}")
        self.en_vuelo = True
    
    def mover(self):
        if self.en_vuelo:
            return self.step(v=2.5, w=1.0)

        return 0.0, False

    def limpiar(self):
        if self.en_vuelo:
            self._reducir_bateria(3.0)
            cantidad_basura = random.uniform(0.1, 0.4)
            self._recolectar_basura(cantidad_basura)


