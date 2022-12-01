import csv




class Asignatura:
    def __init__(self, nombre = None, codigo = None, cantidad_notas = None):
        self.nombre = nombre
        self.codigo = codigo
        self.header = ['Alumno', 'Carrera']
        self.cantidad_notas = cantidad_notas
        self.als_asigs = []
        for x in range(int(cantidad_notas)):
            numero_nota = f'Nota {x + 1}'
            self.header.append(numero_nota)
        self.header.append('Promedio')

    def printA(self):
        print(f'{self.nombre} {self.codigo} {self.cantidad_notas} {len(self.als_asigs)}')



    def add_alumno_asignatura(self, al_asig):
        self.als_asigs.append(al_asig)

    def generate_csv(self):
        with open(f'resultado_{self.codigo}.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)

            # write the data
            for al_asig in self.als_asigs:
                writer.writerow(al_asig.get_data())