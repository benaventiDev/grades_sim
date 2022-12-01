import csv
import string

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from data.Alumno import Alumno
from data.Asignatura import Asignatura
from data.AlumnoAsignatura import AlumnoAsignatura

alumnos = []  # array.array()
asignaturas = []  # array.array()
alumno_asignatura = []  # array.array()


def main():
    load_alumnos()
    load_asignaturas()
    #IMPORTANTE! NUMERO SEED
    seed = 12345
    count = 0
    for asignatura in asignaturas:
        for alumno in alumnos:
            asignatura.add_alumno_asignatura(AlumnoAsignatura(alumno, asignatura.cantidad_notas, seed + count))
            count = count + 1
    for asignatura in asignaturas:
        asignatura.generate_csv()
    draw_image()


def draw_image():
    for asignatura in asignaturas:
        count = 0
        lineY = []
        lineX = []
        for al_as in asignatura.als_asigs:
            prom = float(al_as.prom)
            lineY.append(prom)
            lineX.append(count)
            count = count + 1
        plt.plot(lineX, lineY, label=asignatura.nombre)

    ticks = []
    students = []
    count = 0
    for alumno in alumnos:
        students.append(alumno.nombre.split()[0])
        ticks.append(count)
        count = count + 1
    plt.xticks(ticks, students)
    plt.title("Grafico Final")
    plt.xlabel('Alumnos')
    plt.ylabel('Resultado')
    plt.gca().set_ylim(0, 7)
    plt.legend()
    plt.show()
    plt.savefig('finalgraph.png')


def load_alumnos():
    #IMPORTANTE! RUTA DE ALUMNOS
    with open('/home/benaventi/Downloads/Alumnos.csv') as csv_file:
        csv_reader = csv.reader(csv_file)  # , delimiter=',')
        counter = 0
        for row in csv_reader:
            if counter != 0:
                alumno = Alumno(row[0], row[1], row[2])
                alumnos.append(alumno)
            counter = counter + 1


def load_asignaturas():
    #IMPORTANTE! RUTA DE ASIGNATURAS
    with open('/home/benaventi/Downloads/Asignaturas.csv') as csv_file:
        csv_reader = csv.reader(csv_file)  # , delimiter=',')
        counter = 0
        for row in csv_reader:
            if counter != 0:
                asignatura = Asignatura(row[0], row[1], row[2])
                asignaturas.append(asignatura)
            counter = counter + 1


if __name__ == "__main__":
    main()

# Alumno
# nombre, root, carrera

# Asignatura
# Asignatura, Codigo, cantidad de notas
