
from lotes.domain import ProcessesRepository, ProcessEntity

class LotesService:
    
    def __init__(self, processesRepository:ProcessesRepository ):
        self.processesRepository = processesRepository

    def get_process_by_id(self, id: int):
        return self.processesRepository.get_process_by_id(id)

    def get_all_processes(self):
        return self.processesRepository.get_all_processes()
    
    def get_finished_processes(self):
        return self.processesRepository.get_finished_processes()
    
    def create_process(self, data:dict):

        process_data = {
            "id": int(data["id"]),
            # "name": data["name"],
            "operation": data["operation"],
            "TEM": int(data["TEM"]),
            "elapsdT": int(data["elapsdT"]),
            "is_finished": bool(data["is_finished"])
        }

        process = ProcessEntity.process_from_dict(process_data)
        self.processesRepository.save(process)

        return process

    def get_processes_in_lotes(self, size_of_lotes = 4):
        return self.processesRepository.get_processes_in_lotes(size_of_lotes)

        

