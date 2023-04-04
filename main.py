from Alumno import Alumno

if __name__ == '__main__':
    alumno = Alumno()

    alumno.nombre = 'Humberto'
    alumno.nota = 80

    print(f'Nombre: {alumno.nombre}')
    print(f'Calificación: {alumno.nota}')