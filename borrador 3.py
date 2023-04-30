from os import system;system("cls")
import time
database = [
    {1: ["2+2",{"A":"4","B":"3","C":"7","D":"8"},"A",2.5],2: ["3*4",{"A":"4","B":"12","C":"8","D":"15"},"B",2.5]},
    #0 preguntas, respuestas y porcentaje
    {1234:"didier",4567: "Oscar"}, #1 nombresDocentes
    {3456: ["Nicolas",[]],6543: ["Danny",[]]},#2 nombresEstudiantes
    {}] #3 notas final

comprobante = False
comprobante2 = False
cont = 0
data = ["A","B","C","D"]
def sistema():# mirar
    while True:
        print('''
    +------------------------+
    |    Menu del sistema    | 
    +------------------------+
    | 1. Docente             |
    | 2. Estudiante          |
    +------------------------+''')
        while True:
            try:
                rol_usuario = int(input("\n¿Señor usuario que rol es usted?: ")) # intentar aplicar strip
            except:
                print("Error")
                continue
            if rol_usuario <= 0 or rol_usuario > 2:
                print("Error")
                continue
            else:
                break
        if rol_usuario == 1:
            docente(database,comprobante)
        elif rol_usuario == 2:
            estudiante(database,comprobante)
            
def docente(database,comprobante): # revisar
    while True:
        while True:
            try:
                codigoVdocente = int(input("\nSeñor docente por favor ingrese su codigo de identificacion: "))
            except: # intentar aplicar strip()
                print("Error")
                continue
            if codigoVdocente < 0:
                print("Error")
                continue
            else:
                break
        for j in database[2].keys():
            if codigoVdocente == j:
                comprobante = True
                break
        if (comprobante):
            print(f"\nLo lamentamos docente pero su codigo es identico al del estudiante {database[2][j][0]}")
            break
        else:
            pass
        for i in database[1]:
            if codigoVdocente == i:
                comprobante = True
                break
        if (comprobante):
            print(f"\nBienvenido de vuelva Docente {database[1][codigoVdocente]}")
        else:
            nombreDocente = str(input("\nSeñor docente por favor ingrese su nombre: "))
            if nombreDocente.isnumeric():
                print("Error")
                continue
            else:
                database[1][codigoVdocente] = nombreDocente 
        print('''
    +--------------------------------------+
    |           Menu de opciones           |
    +--------------------------------------+  
    | 1. crear quiz                        |
    | 2. mirar las respuestas del quiz     |
    | 3. mirar notas de los estudiantes    | 
    | 4. salir                             |
    +--------------------------------------+''')       
        cantidad = len(database[0])
        while True:
            try:
                opcion = int(input("\nEliga una opcion: "))
            except:
                print("Error")
                continue
            if opcion <= 0 or opcion > 4:
                print("Error")
            else:
                break
        if opcion == 1:
            creacionQuiz(database,comprobante,data)
        elif opcion == 2:
            if cantidad > 0:
                print(database[0][1][0])
                print("\nRespuestas del quiz:")
                for i, j in database[0].items():
                    print(f"\nPregunta {i}: ¿{database[0][i][0]}?")
                    print("Respuestas:")
                    for k, l in database[0][i][1].items():
                        print(f"{k}: {l}")
                    print(f"respuesta correcta: {database[0][i][2]}")
                sistema()
            else:
                print("No hay respuestas en la base de datos del quiz")
                continue
        elif opcion == 3: 
            cantidad1 = len(database[3])
            if cantidad1 > 0:
                print("\n--Notas de estudiantes--\n") 
                for i, j in database[2].items():
                    print(f"{database[2][i][0]}:  {database[3][i]}")
                Position1 = max(database[3].values())
                Position2 = min(database[3].values())     
                for k, p in database[3].items():
                    if Position1 == p:
                        Position1 = k
                    if Position2 == p:
                        Position2 = k
                print(f"\nLa nota mas alta fue del estudiante {database[2][Position1][0]} con {max(database[3].values())} ") 
                print(f"La nota mas baja fue del estudiante {database[2][Position2][0]} con {min(database[3].values())} ")
                sistema()
            else:
                print("No hay notas alguna al cual mirar")
                continue
        elif opcion == 4:
            for i in reversed(range(1,4)):
                print(f"__Cerrando sistema en {i}__")
                time.sleep(1)
            print("\nSistema cerrado")
            break
def estudiante(database,comprobante): 
    while True:
        while True:
            try:
                codigoVestudiante = int(input("\nSeñor estudiante por favor ingrese su codigo de identificacion: "))
            except:
                print("Error")
                continue
            if codigoVestudiante < 0: 
                print("Error")
            else:
                break
        for i in database[1].keys(): 
            if codigoVestudiante == i:
                comprobante = True
                break
        if (comprobante):
            print(f"\nLo lamentamos estudiante pero su codigo es identico al del docente {database[1][i]}")
            break
        else:
            pass
        for j in database[2]:
            if codigoVestudiante == j:
                comprobante = True
                break
        if (comprobante):
            print(f"\nBienvenido de vuelva {database[2][codigoVestudiante]}")
        else:
            while True:
                nombreEstudiante = str(input("\nSeñor estudiante por favor ingrese su nombre: "))
                if nombreEstudiante.isnumeric():
                    print("Error")
                else:
                    database[2][codigoVestudiante] = []
                    database[2][codigoVestudiante].append(nombreEstudiante)
                    database[2][codigoVestudiante].append([])
                    print(database[2])
                    break
        quiz(database,comprobante,codigoVestudiante,cont)
    
def creacionQuiz(database,comprobante,data): 
    while True:
        print('''
    +--------------------------------------+
    |           Menu de opciones           |
    +--------------------------------------+  
    | 1. crear un quiz                     |
    | 2. modificar un quiz                 |
    +--------------------------------------+   
            ''')
        while True:
            try:
                opciones = int(input("\nEliga una opcion: "))
            except:
                print("Error")
            if opciones <= 0 or opciones > 2:
                print("Error")
                continue
            else:
                break
        if opciones == 1:
            while True:
                try: 
                    cantPregunta = int(input("Digite la cantidad de preguntas que desea: "))
                except:
                    print("Error")
                    continue
                if cantPregunta <= 0:
                    print("Error")
                else:
                    break
            while True:
                try:
                    cantRespuestas = int(input("Digite la cantidad de respuestas que desea: "))
                except:
                    print("Error")
                    continue
                if cantRespuestas <= 0:
                    print("Error")
                    continue
                else:
                    break
            for i in range(cantPregunta):
                pregunta = input(f"Ingrese la pregunta {i+1}: ")
                database[0][i+1] = pregunta
                database[0][i+1] = []
                database[0][i+1].append(pregunta)
                database[0][i+1].append({})
                for j in range(cantRespuestas):
                    respuestas = input(f"Digite la respuesta {data[j]}: ")
                    database[0][i+1][1][data[j]] = respuestas
                    porcentaje = 5.0 / cantPregunta
                while True:
                    respuestaCorrecta = str(input("¿Cual es la respuesta correcta?: ")).upper()
                    if respuestaCorrecta.isnumeric():
                        print("No se aceptan numeros como respuesta correcta")
                        continue
                    else:
                        break
                database[0][i+1].append(respuestaCorrecta);database[0][i+1].append(porcentaje)
            sistema()
        elif opciones == 2:
            cantidad = len(database[0])
            if cantidad > 0:
                while True:
                    try:
                        pregunta_modificar = int(input("\nIngrese la pregunta que desea modificar: "))
                    except:
                        print("Error")
                        continue
                    if pregunta_modificar <= 0:
                        print("Error")
                    else:
                        break
                for i in database[0].keys():
                    if pregunta_modificar == i:
                        comprobante = True
                        break
                if (comprobante):
                    for l in database[0]:
                        print(f"\nPregunta {i}: {database[0][i][0]}\n")
                        for h,k in database[0][i][1].items():
                            print(f"{h}: {k}")
                        break
                    new_pregunta = input(f"Escriba la nueva pregunta: ")
                    cantidadRespuestas = int(input(f"Ingrese el numero de respuesta que tendra la pregunta: "))
                    for p in range(cantidadRespuestas):
                        new_respuesta = input(f"Ingrese la respuesta de la {data[p]}: ")
                        database[0][pregunta_modificar][0] = new_pregunta
                        database[0][i][1][data[p]] = new_respuesta
                    while True:
                        new_respuestaCorrecta = input("Cual es la respuesta correcta: ").upper()
                        if new_respuestaCorrecta.isnumeric():
                            print("Error")
                            continue
                        else:
                            break
                    database[0][1][2] = new_respuestaCorrecta
                    print("\nPregunta modificada con exito\n")
                    for w in database[0]:
                        print(f"Pregunta {i}: {database[0][i][0]}\n")
                        for x,y in database[0][i][1].items():
                            print(f"{x}: {y}")
                        break
                    sistema()
                else:
                    print("No se encontro la pregunta que deseaba modificar")
                    continue
            else:
                print("Lo lamentamos pero no hay ninguna pregunta en la base de datos del quiz al cual modificar")
                continue
def quiz(database,comprobante,codigoVestudiante,cont):
    cantidad = len(database[0])
    codigoEstudiante = codigoVestudiante
    if cantidad > 0:
        print("\n-------Quiz-------\n")
        notaFinal = 0
        for i in database[0]: 
            print(f"\nPregunta {i}: ¿{database[0][i][0]}?\n")
            for p, l in database[0][i][1].items():
                print(f"{p}: {l}") 
            respuesta = input(f"\n¿La respuesta de la pregunta {i} es?: ").upper()
            k = database[0][i][2]
            if respuesta == k:
                comprobante = True
                if (comprobante):
                    l = database[0][1][3]
                    notaFinal += l
                else:
                    pass
        database[2][codigoEstudiante][1].append(notaFinal)
        nota1 = database[2][codigoEstudiante][1][0]
        cont +=1
        if notaFinal < 3:
            if cont == 1:
                print(f"la nota del estudiante fue: {notaFinal}\n")
                print("\nPodra intentar el quiz de nuevo...solo 1 intento mas")
                for i in reversed(range(1,4)):
                    print(f"Podra hacer el quiz en {i}")
                    time.sleep(1)
                input("\nListo su quiz ya esta listo, dele enter para comenzar ")
                quiz(database,comprobante,codigoVestudiante,cont)
            elif cont == 2:  
                print("Sus intentos han finalizado :)")
                nota2 = database[2][codigoEstudiante][1][1] 
                if nota1 > nota2: 
                    database[3][codigoEstudiante] = nota1
                elif nota2 > nota1:
                    database[3][codigoEstudiante] = nota2
                print(f"\nLa nota final del estudiante es: {database[3][codigoEstudiante]}") 
                sistema()
        elif notaFinal > 3:
            print(f"La nota final del estudiante es: {notaFinal}")
            database[3][codigoEstudiante] = nota1
            sistema()
    else:
        print("Lo lamentamos no hay ninguna pregunta en la base de datos del quiz ")
        sistema()
if __name__ == "__main__":
    print('''
    +-------------------------+
    | Bienvenidos al sistema  |
    +-------------------------+''')
    sistema()
