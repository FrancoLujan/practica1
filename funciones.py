import os
import pickle
import random

import clase


def validar_op(inferior, n, superior):
    op = n
    while op < inferior or op > superior:
        print("opcion no contemplada:")
        op = int(input("prueba una opcion valida: "))
    return op


def validar_cantidad(n):
    cantidad = n
    while cantidad <= 0:
        print(f"porfavor ponga un valor mayor a {n}")
        cantidad = int(input("cantidad de alumnos:"))
    return cantidad


def lista_alumnos(n):
    vec = []
    nombres = "franco", "facundo", "maria", "juan", "vale", "jose", "mili", "ana", "zendaya", "barbie"
    carrera = "ing.sistemas", "ing.civil", "ing.industrial", "arquitectura", "medicina", \
              "nutricionista", "filosofia"
    sexo = "M", "F"
    for i in range(n):
        nom = random.choice(nombres)
        edad = random.randint(18, 35)
        legajo = random.randint(10000, 99999)
        carr = random.choice(carrera)
        sex = random.choice(sexo)
        vec.append(
            clase.Alumno(nom, edad, legajo, carr, sex)
        )

    return vec


def muestra_individual(vec, pos):
    print(f"nombre: {vec[pos].nombre}", end="|")
    print(f"edad: {vec[pos].edad}", end="|")
    print(f"legajo: {vec[pos].legajo}", end="|")
    print(f"carrera {vec[pos].carrera}", end="|")
    print(f"sexo: {vec[pos].sexo}", end="|")
    print()


def muestra(vec):
    for i in range(len(vec)):
        muestra_individual(vec, i)


def ordenar_nombres(vec):
    for i in range(len(vec) - 1):
        for j in range(i + 1, len(vec)):
            if vec[j].nombre < vec[i].nombre:
                vec[i], vec[j] = vec[j], vec[i]


def tratamiento_caracteres(texto):
    abreviacion = ""
    for i in texto:
        abreviacion += i
        if abreviacion == "ing.":
            return True


def cuantos_ingenieros(vec):
    contador = 0
    sistemas = 0
    civil = 0
    industrial = 0
    for i in range(len(vec)):
        if tratamiento_caracteres(vec[i].carrera):
            contador += 1
            if vec[i].carrera == "ing.sistemas":
                sistemas += 1
            elif vec[i].carrera == "ing.industrial":
                industrial += 1
            elif vec[i].carrera == "ing.civil":
                civil += 1

    porcentaje_sistemas = round(100 * sistemas / contador, 2)
    porcentaje_industrial = round(100 * industrial / contador, 2)
    porcentaje_civil = round(100 * civil / contador, 2)

    print(f"{contador} de futuros ingenieros")
    print(f" un {porcentaje_sistemas}% de sistemas")
    print(f" un {porcentaje_industrial}% de industrial %")
    print(f" un {porcentaje_civil}% de civil")


def buscar_legajo(vec, leg):
    for i in range(len(vec)):
        if vec[i].legajo == leg:
            return i
    return -1


def buscar_nombre(vec, nom, enc):
    izq = 0
    der = len(vec) - 1
    while izq <= der:
        c = (izq + der) // 2
        if nom == vec[c].nombre:
            enc.append(vec[c])
        if nom < vec[c].nombre:
            der = c - 1
        else:
            izq = c + 1


def grabar_medicos(vec):
    archivo = "alumnos"
    canal = open(archivo, "wb")
    for i in range(len(vec)):
        if vec[i].edad > 25 and vec[i].carrera == "medicina":
            pickle.dump(vec[i], canal)
    canal.close()
    return archivo


def leer_archivo(nom_archivo):
    if not os.path.exists(nom_archivo):
        print(f"el archivo {nom_archivo} no existe")
    else:
        canal = open(nom_archivo, "rb")
        tamanio = os.path.getsize(nom_archivo)

        while canal.tell() < tamanio:
            lib = pickle.load(canal)
            print(f"nombre: {lib.nombre}", end="|")
            print(f"edad: {lib.edad}", end="|")
            print(f"legajo: {lib.legajo}", end="|")
            print(f"carrera {lib.carrera}", end="|")
            print(f"sexo: {lib.sexo}", end="|")
            print()
