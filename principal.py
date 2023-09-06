"""
crear una lista  alumnos (nombre, edad, legajo, carrera, sexo).
edad (18, 35)
legajo (10000, 99999)
carreras(ing.sistemas, arquitectura, ing.civil, medicina, nutricionista, filosofia, ing.industrial)
crear un menu de opciones
1- cargar una cantidad de n alumnos n ingresado por teclado
2- mostrar imformacion del alumno en una linea
3- ordenar los alumnos nombre
4- contar cuantos estudiantes de ingenieria hay y el porcentaje de estudiantes en cada ingenieria
5- buscar alumno por legajo mostrar el primero que encuentre y si no encuntra dar un mensaje
6- buscar alumnos por nombre, mostrar y si no encuntra dar un mensaje
7- crear un archivo binario con todos los estudiantes de medicina mayores a 25 años
8- mostrar archivo binario pero solo los alumnos masculinos

tener en cuenta validaciones
"""

import funciones


def principal():
    op = 0
    alumnos = None
    archivo = ""
    while op != -1:

        print("\n1- cargar alumnos")
        print("2- mostrar alumnos")
        print("3- ordenar alumnos por nombre")
        print("4- cantidad de alumnos de ingenieria y porcentaje en cada de una de ellas")
        print("5- buscar alumno por legajo ")
        print("6- buscar alumnos por su nombre")
        print("7- crear archivos binarios con estudiantes de medicina mayores a 25 años ")
        print("8- mostrar el archivo del punto 7 pero solo a los alumnos masculinos")
        print("9- salir \n")

        op = int(input("escoje una de las opciones:"))  # validar
        op = funciones.validar_op(1, op, 9)

        if op == 1:  # validar para que todo funcione
            n = int(input("cantidad de alumnos"))
            n = funciones.validar_cantidad(n)
            alumnos = funciones.lista_alumnos(n)

        elif alumnos is not None:
            if op == 2:
                funciones.muestra(alumnos)
            elif op == 3:
                funciones.ordenar_nombres(alumnos)
            elif op == 4:
                funciones.cuantos_ingenieros(alumnos)
            elif op == 5:
                x = int(input("legajo a buscar:"))
                encontrado = funciones.buscar_legajo(alumnos, x)
                if encontrado != - 1:
                    print("se encontro")
                    funciones.muestra_individual(alumnos, encontrado)
                else:
                    print(f"lo siento pero el legajo {x}, no se encuntra registrado...")
            elif op == 6:
                x = input("nombre a buscar:")
                nom_encontrados = []
                funciones.buscar_nombre(alumnos, x, nom_encontrados)
                if len(nom_encontrados) >= 1:
                    funciones.muestra(nom_encontrados)
                else:
                    print(f"no se encontro a nadie con ese nombre {x}")
            elif op == 7:
                archivo = funciones.grabar_medicos(alumnos)
                print("se creo el archivo con exito")

            elif op == 8:  # validar punto 7
                funciones.leer_archivo(archivo)
            elif op == 9:
                op = - 1
        else:
            print("ingrese la opcion 1 primero...")

    print("salio del programa...")


if __name__ == "__main__":
    principal()
