from Funciones import *

class Curso():
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []
        self.materias = []

    def agregarAlumno(self, alumno):
        """
            :parametro alumno: object
            :return None
        """
        self.alumnos.append(alumno)

    def agregarMateria(self, materia):
        """
            :parametro materia: object
            :return None
        """
        self.materias.append(materia)

    def promedio(self):
        # :return float
        promedios = []
        for alumno in self.alumnos:
            promedios.append(alumno.promedioTotal())
        return calcularPromedio(promedios)