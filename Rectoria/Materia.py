from Funciones import *

class Materia():
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def agregarAlumno(self, alumno):
        """
            :parametro alumno: object
            :return None
        """
        if not alumno in self.alumnos:
            self.alumnos.append(alumno)

    def promedio(self):
        """
            Calcula el promedio de todos los alumnos que cursan la materia
            :return float
        """
        promedios = []
        for alumno in self.alumnos:
            promedios.append(alumno.promedio(self))
        return calcularPromedio(promedios)
