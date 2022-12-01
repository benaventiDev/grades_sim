

import random



class AlumnoAsignatura:
    def __init__(self, alumno = None, cantidad_notas = None, seed = None):
        self.alumno = alumno
        self.cantidad_notas = cantidad_notas
        self.notas = []
        self.notas.append(alumno.nombre)
        self.notas.append(alumno.carrera)
        random.seed(seed)
        total_notas = 0
        for x in range(int(self.cantidad_notas)):
            nota = random.randint(1, 7)
            self.notas.append(nota)
            total_notas = total_notas + nota
        self.prom = total_notas / int(cantidad_notas)
        self.notas.append(self.prom)

    def get_data(self):
        return  self.notas