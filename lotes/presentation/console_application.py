import time
import os
import sys
import random
import re
import msvcrt

from lotes import ProcessRepositoryImpl, LotesService, ArrayProcessesDatasource

processes_repository = ProcessRepositoryImpl(
    ArrayProcessesDatasource()
)

lotes_service = LotesService(
    processes_repository
)


class ConsoleApplication:


    @staticmethod
    def run():
        ConsoleApplication.__appliaction()
        
    @staticmethod
    def __appliaction():
        # ConsoleApplication.__get_processes_from_user()
        os.system("cls")
        ConsoleApplication.__create_processes()
        ConsoleApplication.__init_magnetic_tape()
     
        
    @staticmethod
    def __init_magnetic_tape():
        print("\n")
        lotes = lotes_service.get_processes_in_lotes()
        global_timer = 0
        
        nro_lotes = len(lotes)
        for lote in lotes:
            nro_lotes -= 1
            while(len(lote)>0): 
                process_in_execution = lote.pop(0)
                tme=int(process_in_execution.TEM)
                if(lote==lotes[-1] and len(lote) == 0):
                    tme += 1
                for i in range(tme):
                    if(process_in_execution.is_finished):
                        break

                    if msvcrt.kbhit():
                        try:
                            key = msvcrt.getch().decode('utf-8')
                            while msvcrt.kbhit():
                                msvcrt.getch()
                            if key == 'e':
                                lote.append(process_in_execution)
                                break
                            if key == 'w':
                                process_in_execution.operation += " !"
                                process_in_execution.is_finished = True
                                break
                            if key == 'p':
                                ConsoleApplication.__pause()
                        except:
                                pass

                    os.system("cls")
                    print(f"Contador global: {global_timer}")
                    print(f"-Número de lotes pendientes: {nro_lotes}")
                    print("\n-Lote en Ejecución:")
                    for process in lote:
                        print(f"------------------\nID: {process.id} \nTEM: {process.TEM} | T trascurrido: {process.elapsdT}")

                    print("\n-Proceso en Ejecución:")
                    if process_in_execution.TEM > process_in_execution.elapsdT and not process_in_execution.is_finished:
                        print(process_in_execution)
                        global_timer += 1
                        print(f"Tiempo transcurrido: {process_in_execution.elapsdT} | Tiempo restante: {process_in_execution.TEM-process_in_execution.elapsdT}")
                        process_in_execution.elapsdT += 1
                    else:
                        process_in_execution.is_finished = True

                    print("\n-Procesos Terminados:")
                    finished_processes = lotes_service.get_finished_processes()
                    for nlote, process_finished in enumerate(finished_processes, start = 0):
                        if nlote % 4 == 0:
                            print(f"\n----Lote {(nlote // 4) + 1}----")
                        print(f"ID {process_finished.id} | Tiempo tomado: {process_finished.elapsdT} ~ Operacion: {process_finished.operation} | Resultado: {ConsoleApplication.__eval_operation(process_finished.operation)}")
                    sys.stdout.flush()
                    time.sleep(0.7)
                
                if process_in_execution.TEM==process_in_execution.elapsdT:
                    process_in_execution.is_finished = True

                
        os.system ("pause")
        
    @staticmethod
    def __create_processes():
        
        print("Porfavor escribe los datos correspondientes: ")

        number_of_process = ""

        while not number_of_process.isnumeric():
            number_of_process = input("Cuantos procesos vas a requerir: ")

        number_of_process = int(number_of_process)

        for i in range(1,number_of_process+1):
            data = {
                "id": i,
                "name": "",
                "operation": "",
                "TEM": random.randint(5, 18),
                "elapsdT": 0,
                "is_finished": False
            }
            
            is_valid_operation = ConsoleApplication.__validate_operation(data["operation"])
            while not is_valid_operation:
                data["operation"] = ConsoleApplication.__generate_operation()
                is_valid_operation = ConsoleApplication.__validate_operation(data["operation"])

            lotes_service.create_process(data)
            

    @staticmethod
    def __eval_operation(operation):
            try:
                return eval(operation)
            except:
                return "Error"


    @staticmethod
    def __pause():
            print("Programa en pausa, pulse C para continuar...")
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch().decode('utf-8')
                    if key == 'c':
                        break


    @staticmethod
    def __validate_operation(operation):
            try:
                if re.match('^-?\d+[+*/%-]-?\d+$', operation) and '/0' not in operation and '%0' not in operation:
                    return True
            except:
                return False
    

    @staticmethod
    def __generate_operation():
        symbols = ['+', '-', '/', '*', '%']
        operation = str(random.randint(0, 100))+random.choice(symbols)+str(random.randint(0, 100))
        return(operation)


    @staticmethod
    def __get_processes_from_user():
        
        print("Porfavor escribe los datos correspondientes: ")

        number_of_process = ""

        while not number_of_process.isnumeric():
            number_of_process = input("Cuantos procesos vas a requerir: ")

        number_of_process = int(number_of_process)

        print()
        for i in range(1,number_of_process+1):
            print(f"--------Proceso numero {i}--------")
            data = {
                "id": "",
                "name": "",
                "operation": "",
                "TEM": "",
                "is_finished": False
            }
            while not data["id"].isnumeric() or process_exists:
                data["id"] = input("Id a capturar: ")
                
                if data["id"].isnumeric():
                    process_exists = lotes_service.get_process_by_id(int(data["id"]))
            
            alpanumeric_regex = "^[A-Za-z0-9 ]*$"
            while data["name"] == "" or not bool(re.match(alpanumeric_regex, data["name"])):
                data["name"] = input("Nombre del usuario: ").strip()

            is_valid_operation = ConsoleApplication.__validate_operation(data["operation"])
            while not is_valid_operation:
                data["operation"] = input("Operacion a realizar: ")
                is_valid_operation = ConsoleApplication.__validate_operation(data["operation"])

            
            while not data["TEM"].isnumeric() or int(data["TEM"]) <= 0:
                data["TEM"] =  input("Tiempo estimado(TEM): ")


            lotes_service.create_process(data)
            
            print()
