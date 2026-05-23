import math

class RobotBase:
    def __init__(self, nombre, capacidad_carga, x_inicial=0.0, y_inicial=0.0, yaw_inicial=0.0):
        self.__nombre = nombre
        self.__capacidad_carga = capacidad_carga
        self.__bateria = 100.0 
        self.__pos_x = x_inicial
        self.__pos_y = y_inicial
        self.__yaw = yaw_inicial
        self.__basura_recolectada = 0.0
        self.__step_dt = 0.1

        self.target_x = 5.0
        self.target_y = 5.0

#Este es el constructor que contiene atributos publicos y privados

    def get_nombre(self):
        return self.__nombre

    def get_bateria(self):
        return self.__bateria

    def get_pos_x(self):
        return self.__pos_x

    def get_pos_y(self):
        return self.__pos_y

    def get_yaw(self):
        return self.__yaw

    def get_basura_recolectada(self):
        return self.__basura_recolectada

#Estos son los getters 

    def _actualizar_pose(self, x, y, yaw):
        self.__pos_x = x
        self.__pos_y = y
        self.__yaw = yaw

    def _reducir_bateria(self, cantidad):
        self.__bateria -= cantidad
        if self.__bateria < 0:
            self.__bateria = 0

    def _recolectar_basura(self, cantidad):

        espacio_libre = (self.__capacidad_carga - self.__basura_recolectada)

        if cantidad > espacio_libre:
            cantidad = espacio_libre      

        self.__basura_recolectada += cantidad

#Estos son los metodos internos protegidos

    @staticmethod
    def calc_dist_to_goal(pos_x, pos_y, target_x, target_y):
        d = math.sqrt((target_x - pos_x)**2 + (target_y - pos_y)**2)
        return d

    @staticmethod
    def calc_yaw_error(pos_x, pos_y, yaw, target_x, target_y):
        angulo_meta = math.atan2(target_y - pos_y, target_x - pos_x)
        error = angulo_meta - yaw
        error_norm = ((error + math.pi) % (2 * math.pi)) - math.pi
        return error_norm

#metodos estaticos 

    def step(self, v, w):
        if self.__bateria <= 0:
            return 0.0, True

        yaw_nuevo = (self.__yaw + w*self.__step_dt)
        yaw_nuevo = ((yaw_nuevo + math.pi) % (2 * math.pi)) - math.pi
        x_nuevo = (self.__pos_x + v*math.cos(yaw_nuevo)*self.__step_dt)
        y_nuevo = (self.__pos_y + v*math.sin(yaw_nuevo)*self.__step_dt)
        self._actualizar_pose(x_nuevo, y_nuevo, yaw_nuevo)
        distancia = RobotBase.calc_dist_to_goal(self.__pos_x, self.__pos_y, self.target_x, self.target_y)
        error_angular = RobotBase.calc_yaw_error(self.__pos_x, self.__pos_y, self.__yaw, self.target_x, self.target_y)
        reward = (-distancia-abs(error_angular))
        llegamos = distancia <0.5
        if llegamos:
            reward +=100
        
        return reward, llegamos

#Hasta aca es la simulacion cinematica, el metodo step

    def mover(self):
        raise NotImplementedError("Las clases hijas deben implementar este metodo")

    def limpiar(self):
        raise NotImplementedError("Las clases hijas deben implementar este metodo")    

#Metodos abstractos
#Fin de la creacion de la clase RobotBase