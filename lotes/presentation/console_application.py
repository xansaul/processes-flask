import time
import os

from ..infrastructure.repositories.processes_repository_impl import ProcessRepositoryImpl
from ..infrastructure.datasources.array_processes_datasource import ArrayProcessesDatasource
from ..domain.entities.process_entity import ProcessEntity
from ..domain.services.lotes_service import LotesService


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
        ConsoleApplication.__get_processes_from_user()
        os.system("cls")
        ConsoleApplication.__init_magnetic_tape()
    
    @staticmethod
    def __init_magnetic_tape():

        print("\n")
        lotes = lotes_service.get_processes_in_lotes()


        print(lotes)
        for lote in lotes:
            for process in lote:
                print()
                print(process)


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
                "TEM": ""
            }
            while not data["id"].isnumeric() or process_exists:
                data["id"] = input("Id a capturar: ")
                
                if data["id"].isnumeric():
                    process_exists = lotes_service.get_process_by_id(int(data["id"]))
            
            data["name"] = input("Nombre del usuario: ")

            is_valid_operation = ConsoleApplication.__validate_operation(data["operation"])
            while not is_valid_operation:
                operation = input("Operacion a realizar: ")
                is_valid_operation = ConsoleApplication.__validate_operation(operation)

            
            while not data["TEM"].isnumeric() or int(data["TEM"]) < 0:
                data["TEM"] =  input("Tiempo estimado(TEM): ")

            

            lotes_service.create_process(data)
            
            print()



    @staticmethod
    def __validate_operation(operation):
        try:
            eval(operation)
            return True
        except:
            return False
            
    






