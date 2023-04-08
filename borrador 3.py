from os import system 
system("cls")
import time
database = [
    {1: "2 + 2",2: "3 * 4"}, #0 dataQuiz
    {1: "4", 2: "12"}, #1 respuestaQuiz
    {1: 2.5, 2:2.5}, #2 PorcentajeQuiz
    {3456:5.0,6543: 2.5}, # 3 notas finales de los estudiantes
    {1234: "didier",4321:"oscar"}, #4 nombresDocentes
    {3456: "nicolas",6543:"juan"}] #5 nombresEstudiantes

comprobante = False
def sistema():
    while True:
        print('''
    __________________________
    |    Menu del sistema    | 
    |________________________|
    | 1. Docente             |
    | 2. Estudiante          |
    |________________________|''')
        while True:
            try:
                rol_usuario = int(input("\n¿Señor usuario que rol es usted?: "))
            except:
                print("Error")
                continue
            if rol_usuario <= 0 or rol_usuario > 2:
                print("Error")
            else:
                break
        if rol_usuario == 1:
            docente(database,comprobante)
        elif rol_usuario == 2:
            estudiante(database,comprobante,)
            
def docente(database,comprobante):
    while True:
        while True:
            try:
                codigoVdocente = int(input("\nSeñor docente por favor ingrese su codigo de identificacion: "))
            except: 
                print("Error")
                continue
            if codigoVdocente < 0:
                print("Error")
            else:
                break
            
        for j in database[5].keys():
            if codigoVdocente == j:
                comprobante = True
                break
        if (comprobante):
            print(f"\nLo lamentamos docente pero su codigo es identico al del estudiante {database[5][j]}")
            break
        
        for i in database[4]:
            if codigoVdocente == i:
                comprobante = True
                break
        if (comprobante):
            print(f"\nBienvenido de vuelva Docente {database[4][codigoVdocente]}")
            
        else:
            nombreDocente = str(input("\nSeñor docente por favor ingrese su nombre: "))
            if nombreDocente.isnumeric():
                print("Error")
            else:
                database[4][codigoVdocente] = nombreDocente 
        print('''
    ________________________________________
    |           Menu de opciones           |
    |______________________________________|  
    | 1. crear quiz                        |
    | 2. mirar las respuestas del quiz     |
    | 3. mirar notas de los estudiantes    | 
    | 4. salir                             |
    |______________________________________|''')       
        
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
            creacionQuiz(database,comprobante)
        elif opcion == 2:
            cantidad2 = len(database[1])
            if cantidad2 > 0:
                print("\nRespuestas del quiz:\n")
                for i, j in database[1].items():
                    print(f"Pregunta {i}: ¿{database[0][i]}?\tRespuesta: {j}")
                sistema()
            else:
                print("No hay respuestas en la base de datos del quiz")
        elif opcion == 3:
            cantidad3 = len(database[3])
            if cantidad3 > 0:
                print("\n--Notas de estudiantes--\n")
                for k, s in database[3].items():
                    print(f"{database[5][k]}: {s}")
                Position1 = min(database[3]);Position2 = max(database[3])  
                print(f"\nLa nota mas alta fue del estudiante {database[5][Position1]} con {max(database[3].values())} ")
                print(f"La nota mas baja fue del estudiante {database[5][Position2]} con {min(database[3].values())} ")
            else:
                print("No hay notas alguna al cual mirar")
        elif opcion == 4:
            for i in reversed(range(1,6)):
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
        
        for i in database[4].keys(): #docente
            if codigoVestudiante == i:
                comprobante = True
                break
        if (comprobante):
            print(f"\nLo lamentamos estudiante pero su codigo es identico al del docente {database[4][i]}")
            break
        
        for j in database[5]:
            if codigoVestudiante == j:
                comprobante = True
                break
        if (comprobante):
            print(f"\nBienvenido de vuelva {database[5][codigoVestudiante]}")
        else:
            nombreEstudiante = str(input("\nSeñor estudiante por favor ingrese su nombre: "))
            if nombreEstudiante.isnumeric():
                print("Error")
            else:
                database[5][codigoVestudiante] = nombreEstudiante    
        quiz(database,comprobante,codigoVestudiante)
    
def creacionQuiz(database,comprobante): 
    while True:
        print('''
    ________________________________________
    |           Menu de opciones           |
    |______________________________________|  
    | 1. agregar preguntas y respuestas    |
    | 2. modificar preguntas y respuestas  |
    |______________________________________|   
            ''')
        opciones = int(input("\nEliga una opcion: "))
        
        if opciones == 1:
            while True:
                try: 
                    preguntas = int(input("\n¿Cuantas preguntas tendra el quiz?: "))
                except:
                    print("Error")
                    continue
                if preguntas <= 0:
                    print("Error")
                else:
                    break
                
            for i in range(preguntas):
                pregunta = input(f"\nEscriba la pregunta {i+1}: ")    
                respuesta = input(f"\nIngrese la respuesta de la pregunta {i+1}: ")
                database[0][i+1] = pregunta
                porcentaje = 5.0 / preguntas
                database[2][i+1] = porcentaje
                database[1][i+1] = respuesta
                print(database)
            sistema() 

        elif opciones == 2:
            cantidad = len(database[0])
            if cantidad > 0:
                while True:
                    try:
                        pregunta_modficiar = int(input("\nIngrese la pregunta que desea modificar: "))
                    except:
                        print("Error")
                        continue
                    if pregunta_modficiar <= 0:
                        print("Error")
                    else:
                        break
                    
                for i in database[0].keys():
                    if pregunta_modficiar == i:
                        comprobante = True
                        break
                if (comprobante):
                    new_respuesta = input("Ingrese la nueva respuesta: ")
                    database[1][pregunta_modficiar] = new_respuesta
                    sistema()
                else:
                    print("No se encontro la pregunta que deseaba modificar")
            else:
                print("Lo lamentamos pero no hay ninguna pregunta en la base de datos del quiz al cual modificar")
            
def quiz(database,comprobante,codigoVestudiante):
    cantidad = len(database)
    if cantidad > 0:
        print("\n-------Quiz-------\n")
        notaFinal = 0
        for i, j in database[0].items():
            print(f"\n{i}. ¿{j}?")
            respuesta = input(f"\n¿La respuesta de la pregunta {i} es?: ")
            for k in database[1].values():
                if respuesta == k:
                    comprobante = True
                    if (comprobante):
                        for l in database[2].values():
                            notaFinal += l
                            break
                        else:
                            pass
                    break
        codigoEstudiante = codigoVestudiante
        database[3][codigoEstudiante] = notaFinal 
        print(f"La nota final del estudiante es: {notaFinal}")
        
        '''
        pregunta = str(input("¿Desea volver a intentar el examen si/no?: ")).lower()
        if pregunta == "si":
            for i in reversed(range(1,11)):
                print(f"Podra hacer el quiz en {i}")
            input("Listo su quiz ya esta listo, dele enter para comenzar")
            quiz()
        else:
            break
        '''
        sistema()            
    else:
        print("Lo lamentamos no hay ninguna pregunta en la base de datos del quiz ")
        
if __name__ == "__main__":
    print("     Bienvenidos al sistema")
    sistema()
