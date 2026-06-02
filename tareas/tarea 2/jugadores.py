
# Módulo de clases para el simulador de selección campeona del mundo.
# Contiene la clase padre Jugador y las clases hijas para diferentes posiciones.



class Jugador:
    """Clase padre que representa un jugador de fútbol con atributos comunes."""
    
    def __init__(self, nombre, edad, altura, dorsal):
        
        # Inicializa un jugador con sus atributos comunes.

        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dorsal = dorsal
    
    def correr(self):
        # Método que indica que el jugador está corriendo.
        return f"{self.nombre} está corriendo por la cancha."
    
    def mostrar_rol(self):
        # Método polimórfico que retorna el rol del jugador (genérico).
        return "Soy un jugador de fútbol."
    
    def concentrarse(self):
        # Método adicional: el jugador se concentra antes del partido.
        return f"{self.nombre} se está concentrando para el partido."
    
    def festejar_gol(self):
        # Método adicional: el jugador festeja después de un gol.
        return f"{self.nombre} festeja emocionado el gol."


class Portero(Jugador):
    """Clase hija que representa un portero, hereda de Jugador."""
    
    def __init__(self, nombre, edad, altura, dorsal, atajadas_historicas):
       
        # Inicializa un portero con sus atributos específicos.
     
        super().__init__(nombre, edad, altura, dorsal)
        self.atajadas_historicas = atajadas_historicas
        self.reflejos = "excelentes"
    
    def mostrar_rol(self):
        # Sobrescribe el método para mostrar el rol específico del portero.
        return f"{self.nombre} - Portero"
    
    def atajar(self):
        # Método específico: el portero ataja el balón.
        return f"{self.nombre} ha atajado el balón con sus {self.reflejos} reflejos."
    
    def distribuir_juego(self):
        # Método adicional: el portero distribuye el juego con los pies.
        return f"{self.nombre} distribuye el balón con precisión desde el área."


class Defensa(Jugador):
    """Clase hija que representa un defensa, hereda de Jugador."""
    
    def __init__(self, nombre, edad, altura, dorsal, balones_recuperados):
        
        # Inicializa un defensa con sus atributos específicos.
   
        super().__init__(nombre, edad, altura, dorsal)
        self.balones_recuperados = balones_recuperados
        self.velocidad = "muy rápida"
    
    def mostrar_rol(self):
        # Sobrescribe el método para mostrar el rol específico del defensa.
        return f"{self.nombre} - Defensa"
    
    def marcar(self):
        # Método específico: el defensa marca al rival.
        return f"{self.nombre} marca al atacante con su velocidad {self.velocidad}."
    
    def hacer_falta(self):
        # Método adicional: el defensa hace una falta para detener al rival.
        return f"{self.nombre} comete una falta táctica para detener el ataque."


class Mediocampista(Jugador):
    """Clase hija que representa un mediocampista, hereda de Jugador."""
    
    def __init__(self, nombre, edad, altura, dorsal, asistencias):
        
        # Inicializa un mediocampista con sus atributos específicos.
     
        super().__init__(nombre, edad, altura, dorsal)
        self.asistencias = asistencias
        self.visión = "de 360°"
    
    def mostrar_rol(self):
        # Sobrescribe el método para mostrar el rol específico del mediocampista.
        return f"{self.nombre} - Mediocampista"
    
    def dar_pase(self):
        # Método específico: el mediocampista da un pase.
        return f"{self.nombre} da un pase preciso con su visión {self.visión}."
    
    def recuperar_balon(self):
        # Método adicional: el mediocampista recupera el balón en la mitad.
        return f"{self.nombre} recupera el balón en el mediocampo."


class Delantero(Jugador):
    """Clase hija que representa un delantero, hereda de Jugador."""
    
    def __init__(self, nombre, edad, altura, dorsal, goles_anotados):
        
        # Inicializa un delantero con sus atributos específicos.
       
        super().__init__(nombre, edad, altura, dorsal)
        self.goles_anotados = goles_anotados
        self.potencia_remate = "devastadora"
    
    def mostrar_rol(self):
        # Sobrescribe el método para mostrar el rol específico del delantero.
        return f"{self.nombre} - Delantero"
    
    def patear_al_arco(self):
        # Método específico: el delantero patea hacia el arco.
        return f"{self.nombre} patea fuerte al arco con potencia {self.potencia_remate}."
    
    def hacer_control(self):
        # Método adicional: el delantero hace un control del balón.
        return f"{self.nombre} realiza un control perfecto del balón."
