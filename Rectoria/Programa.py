from Alumno import Alumno
from Curso import Curso
from Materia import Materia

Matematica = Materia("Matematica")
Geografia = Materia("Geografia")

Sexto = Curso("6to Computacion")
Quinto = Curso("5to Computacon")

Silvio = Alumno(1, "Silvio", "Cabral", "6to Computacion")
Alex = Alumno(2, "Alexis", "Viera", "6to Computacion")

Sexto.agregarMateria(Matematica)
Sexto.agregarAlumno(Silvio)
Sexto.agregarAlumno(Alex)

Alex.agregarMateria(Matematica)
Silvio.agregarMateria(Matematica)
Silvio.agregarMateria(Geografia)

Alex.agregarCalificacion(Matematica, 10)
Alex.agregarCalificacion(Matematica, 3)
Silvio.agregarCalificacion(Geografia, 4)
Silvio.agregarCalificacion(Matematica, 4)
Silvio.agregarCalificacion(Matematica, 7)

print(f"Promedio en Matematica {Silvio.promedio(Matematica)}")
print(f"Promedio en Geografia {Silvio.promedio(Geografia)}")
print(f"Promedio total de Silvio {Silvio.promedioTotal()}")
print(f"Promedio total de Alex {Alex.promedioTotal()}")


print(f"Promedio total de sexto {Sexto.promedio()}")
print(f"Promedio total de quinto {Quinto.promedio()}")
