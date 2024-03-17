
from lotes.domain.datasource.processes_datasource import ProcessesDatasource
from lotes.domain.entities.process_entity import ProcessEntity

from typing import List, Optional

class ArrayProcessesDatasource(ProcessesDatasource):

    def __init__(self):
        self.processes: List[ProcessEntity] = [
            # ProcessEntity(1,"Saul","5+1", 5),
            # ProcessEntity(2,"Jenny","5+2", 5),
            # ProcessEntity(3,"si","5+3", 4),
            # ProcessEntity(4,"si","5+4", 4),
            # ProcessEntity(5,"si","5+5", 3),
            # ProcessEntity(6,"si","5+6", 3),
            # ProcessEntity(7,"si","5+7", 2),
            # ProcessEntity(8,"si","5+8", 2),
            # ProcessEntity(9,"si","5+9", 1),
            # ProcessEntity(10,"si","5+10", 1),
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
        finished_processes = [process for process in self.processes if process.is_finished]
        return finished_processes

    def get_processes_in_lotes(self, size_of_lotes: int) -> List[List[ProcessEntity]]:
        if size_of_lotes <= 0:
            raise ValueError("El tamaño de los lotes debe ser mayor que cero.")

        lotes = [self.processes[i:i+size_of_lotes] for i in range(0, len(self.processes), size_of_lotes)]
        return lotes
    
    def clean_processes(self):
        self.processes = []