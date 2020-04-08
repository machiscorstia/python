from Funciones import calcularPromedio

class Alumno():
    def __init__(self, legajo, nombre, apellido, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.curso = curso
        self.calificaciones = {}  # key: object, value: list

    def agregarMateria(self, materia):
        """
            Agrega una nueva materia
            :parametro materia: object
            :return None
        """
        if not materia in self.calificaciones:
            materia.agregarAlumno(self)
            self.calificaciones[materia] = []

    def agregarCalificacion(self, materia, nota):
        """
            Agrega una nueva calificaciÃ³n a una materia
            :parametro materia: object
            :parametro nota: int
            :return None
        """
        if materia in self.calificaciones:
            notas = self.calificaciones[materia]
            notas.append(nota)
            self.calificaciones[materia] = notas

    def calificacion(self, materia):
        """
            Getter calificaciones
            :parametro materia: object
            :return dict
        """
        return self.calificaciones[materia]

    def promedio(self, materia):
        """
            Saca el promedio de una materia especifica.
            :parametro materia: object
            :return float
        """
        return calcularPromedio(self.calificaciones[materia])

    def promedioTotal(self):
        """
            Calcula el promedio de todas las materias que cursa
            :return float
        """
        notas = list(self.calificaciones.values())
        return calcularPromedio(notas)
