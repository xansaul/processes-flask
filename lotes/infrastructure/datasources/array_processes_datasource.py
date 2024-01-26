
from lotes.domain.datasource.processes_datasource import ProcessesDatasource
from lotes.domain.entities.process_entity import ProcessEntity

from typing import List, Optional

class ArrayProcessesDatasource(ProcessesDatasource):

    def __init__(self):
        self.processes: List[ProcessEntity] = [
            ProcessEntity(1,"Saul","5+3", 5),
            ProcessEntity(2,"Jenny","5+3", 10),
            ProcessEntity(3,"si","5+3", 4),
        ]
        
    def get_all_processes(self) -> List[ProcessEntity]:
        return self.processes

    def get_process_by_id(self, id:int ) -> Optional[ProcessEntity]:

        for process in self.processes:
            if process.id == id:
                return process
            
        return None
        
    def save(self, process: ProcessEntity ) -> None:
        self.processes.append(process)
        
    def get_finished_processes(self) -> List[ProcessEntity]:
        finished_processes = [process for process in self.processes if process.TEM == 0]
        return finished_processes

    def get_processes_in_lotes(self, size_of_lotes: int) -> List[List[ProcessEntity]]:
        if size_of_lotes <= 0:
            raise ValueError("El tamaño de los lotes debe ser mayor que cero.")

        lotes = [self.processes[i:i+size_of_lotes] for i in range(0, len(self.processes), size_of_lotes)]
        return lotes