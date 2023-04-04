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
        
        rol_usuario = int(input("\n¿Señor usuario que rol es usted?: "))
        if rol_usuario == 1:
            docente(database,comprobante)
        elif rol_usuario == 2:
            estudiante(database,comprobante)
            
def docente(database,comprobante): 
    while True:
        while True:
            try:
                codigoV = int(input("\nSeñor docente por favor ingrese su codigo de identificacion: "))
            except: 
                print("Error")
                continue
            if codigoV < 0:
                print("Error, no se aceptan numeros negativos")
            else:
                break
        for i in database[4]:
            if codigoV == i:
                comprobante = True
                break
        if (comprobante):
            print(f"\nBienvenido de vuelva Docente {database[4][codigoV]}")
        else:
            nombreDocente = str(input("\nSeñor docente por favor ingrese su nombre: "))
            database[4][codigoV] = nombreDocente 
            print(database) # quitar cuando se termine por completo el codigo
        print('''
    ________________________________________
    |           Menu de opciones           |
    |______________________________________|  
    | 1. crear quiz                        |
    | 2. mirar las respuestas del quiz     |
    | 3. mirar notas de los estudiantes    | 
    | 4. salir                             |
    |______________________________________|''')       
        
        opcion = int(input("\nEliga una opcion: "))
        if opcion == 1:
            creacionQuiz(database,comprobante)
        elif opcion == 2: 
            cantidad2 = len(database[1])
            if cantidad2 > 0:
                for i, j in database[1].items():
                    print(f"Pregunta {i}: Respuesta: {j}")
            else:
                print("No hay respuestas en la base de datos del quiz")
        elif opcion == 3: 
            cantidad3 = len(database[3])
            if cantidad3 > 0:
                print("--Notas de estudiantes--")
                for k, s in database[3].items():
                    print(f"\n{database[5][k]} Nota final: {s}")
                    
                print(f"La nota mas alta fue del estudiante {database[5][k]} con su nota de {max(database[3].values())} ")
                print(f"La nota mas baja fue del estudiante {database[5][k]} con su nota de {min(database[3].values())} ")
                # hacer que muestre el nombre del estudiante y su nota, ademas
                # si es posible hacer promedio cual es el mayor puntaje y el menor
            else:
                print("No hay notas alguna al cual mirar")
        elif opcion == 4: # terminado
            for i in reversed(range(1,6)):
                print(f"__Cerrando sistema en {i}__")
                time.sleep(1)
            print("\nSistema cerrado")
            break
            
def estudiante(database,comprobante): # terminado pero mirar si se puede pulir
    while True:
        codigoV = int(input("\nSeñor estudiante por favor ingrese su codigo de identificacion: "))
        for i in database[5]:
            if codigoV == i:
                comprobante = True
                break
        if (comprobante):
            print(f"\nBienvenido de vuelva {database[5][codigoV]}")
        else:
            nombreEstudiante = str(input("\nSeñor estudiante por favor ingrese su nombre: "))
            database[5][codigoV] = nombreEstudiante    
            print(database) # quitar cuando se termine por completo el codigo
        quiz(database,comprobante,codigoV)
            
def creacionQuiz(database,comprobante): # creacion con quiz hay fallo
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
        # opcion 1 de agregar
        if opciones == 1: 
            preguntas = int(input("\n¿Cuantas preguntas tendra el quiz?: "))
            for i in range(preguntas):
                pregunta = input(f"\nEscriba la pregunta {i+1}: ")
                database[0][i+1] = pregunta
                respuesta = input(f"\nIngrese la respuesta de la pregunta {i+1}: ")
                porcentaje = 5.0 / preguntas;database[2][i+1] = porcentaje
                database[1][i+1] = respuesta
                database[2][i+1] = porcentaje
                print(database)
            sistema() 
            # opcion 2 de modificar    
        elif opciones == 2:
            cantidad = len(database[0])
            if cantidad > 0:
                pregunta_modficiar = int(input("\nIngrese la pregunta que desea modificar: "))
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
                print("Lo lamentamos no hay ninguna pregunta en la base de datos del quiz al cual modificar")
            
def quiz(database,comprobante,codigoV):
    cantidad = len(database)
    if cantidad > 0:
        print("\nQuiz\n")
        notaFinal = 0
        for i, j in database[0].items():
            print(f"\n{i}. {j}")
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
        codigoEstudiante = codigoV
        database[3][codigoEstudiante] = notaFinal 
        print(f"La nota final del estudiante es: {notaFinal}")
        sistema()            
    else:
        print("Lo lamentamos no hay ninguna pregunta en la base de datos del quiz ")
        
if __name__ == "__main__":
    print("Bienvenidos al sistema\n")
    sistema()
