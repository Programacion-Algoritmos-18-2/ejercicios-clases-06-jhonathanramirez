
import abc
class PersonaEquipo(metaclass=abc.ABCMeta):
    """
    se define la clases abstracta 
    """
    def __int__(self, nom):
        self nombre = nom
    __metaclass__ = abc.ABCMeta 

    @abc.abstractmethod
    def entremamiento():
        pass
class Entrenador(PersonaEquipo):
    def __int__(self, n):
        super(Entrenador, self).__int__(n)
        self.codigo_entrenado = ""
    def agregar_codigo_entrenador(self, cod_ent):  
        self.codigo_entrenador = cod_ent

    def obtener_codigo_entrenador(self):
        return self.codigo_entrenador    

    def entrenamiento(self):
        print ("Yo %s, entrenador soy el director del entrenamiento")

class MedicoEquipo (PersonaEquipo):
   
    def __int__(self):
        super(MedicoEquipo, self).__int__(n)
    def agregar_titulo(self, t):  
        self.titulo = t

    def obtener_titulo(self):
        return self.titulo
    def entrenamiento(self):
        print ("Yo %s, medico, atiendo a los jugadores en el entrenamiento.")

class Presidente_Equipo (PersonaEquipo):

    def __int__(self):
        super(Presidente_Equipo, self).__int__(n)
        self.numero_propiedades = ""

    def agregar_numero_propiesdades(self, num):  
        self.numero_propiedades = num

    def obtener_numero_propiedades(self):
        return self.numero_propiedades

    def entrenamiento(self):
        print ("Yo %s, presidente, pongo el dinero para el entrenamiento.")

class Futbolista(PersonaEquipo):
    def __int__(self):
        super(Futbolista, self).__int__(n)

    def entrenamiento(self):
        print ("Yo %s, futbolista, hago práctica en el entrenamiento")
