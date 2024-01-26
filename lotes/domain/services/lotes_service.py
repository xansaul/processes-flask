from lotes.domain.repository.processes_repository import ProcessesRepository
from lotes.domain.entities.process_entity import ProcessEntity
from typing import List, Optional

class LotesService:
    
    def __init__(self, processesRepository:ProcessesRepository ):
        self.processesRepository = processesRepository


    def get_process_by_id(self, id: int) -> Optional[ProcessEntity]:
        return self.processesRepository.get_process_by_id(id)

    def get_all_processes(self) -> List[ProcessEntity]:
        return self.processesRepository.get_all_processes()
    
    def create_process(self, data:dict)  -> ProcessEntity:

        process_data = {
            "id": int(data["id"]),
            "name": data["name"],
            "operation": data["operation"],
            "TEM": int(data["TEM"])
        }

        process = ProcessEntity.process_from_dict(process_data)
        self.processesRepository.save(process)

        return process

    def get_processes_in_lotes(self, size_of_lotes = 4):
        return self.processesRepository.get_processes_in_lotes(size_of_lotes)

        

