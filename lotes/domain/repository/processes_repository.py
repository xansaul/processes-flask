from abc import ( ABC, abstractmethod, )
from typing import List, Optional

from ..entities.process_entity import ProcessEntity

class ProcessesRepository(ABC):
   

    @abstractmethod
    def get_all_processes(self) -> List[ProcessEntity]:
        pass

    @abstractmethod
    def get_process_by_id(self, id:int ) -> Optional[ProcessEntity]:
        pass

    @abstractmethod
    def save(self, process: ProcessEntity ) -> None:
        pass

    @abstractmethod
    def get_finished_processes(self,) -> List[ProcessEntity]:
        pass
    
    @abstractmethod
    def get_processes_in_lotes(self, size_of_lotes:int ) -> List[List[ProcessEntity]]:
        pass