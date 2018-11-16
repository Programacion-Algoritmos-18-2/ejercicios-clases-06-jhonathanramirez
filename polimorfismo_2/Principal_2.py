from paquete.polimorfismo_2 import *
#p = PersonaEquipo("Luis")

f = Futbolista("Antonio")
e = Entrenador("Jose")
p =Presidente_Equipo("Francisco")
m = MedicoEquipo("Ramon")
lista = [f,e,p,m]
for l in lista:
	l.entrenamiento()