from typing import List

from lotes.domain.repository.processes_repository import ProcessesRepository
from lotes.domain.datasource.processes_datasource import ProcessesDatasource
from lotes.domain.entities.process_entity import ProcessEntity

class ProcessRepositoryImpl(ProcessesRepository):

    def __init__(self, processesDatasource: ProcessesDatasource):
        super().__init__()
        self.processesDatasource: ProcessesDatasource = processesDatasource
    
        
    def get_all_processes(self) -> List[ProcessEntity]:
        return self.processesDatasource.get_all_processes()

        
    def get_process_by_id(self, id:int ) -> ProcessEntity:
        return self.processesDatasource.get_process_by_id(id)

    def save(self, process: ProcessEntity ) -> None:
        return self.processesDatasource.save(process)

    def get_finished_processes(self) -> List[ProcessEntity]:
        return self.processesDatasource.get_finished_processes()
    
    def get_processes_in_lotes(self, size_of_lotes:int ) -> List[List[ProcessEntity]]:
        return self.processesDatasource.get_processes_in_lotes(size_of_lotes)
        
