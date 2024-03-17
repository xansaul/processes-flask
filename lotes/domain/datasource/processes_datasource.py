from abc import ( ABC, abstractmethod, )
from typing import List, Optional

from ..entities.process_entity import ProcessEntity

class ProcessesDatasource(ABC):

    @abstractmethod
    def get_all_processes() -> List[ProcessEntity]:
        pass

    @abstractmethod
    def get_process_by_id( id:int ) -> Optional[ProcessEntity]:
        pass

    @abstractmethod
    def save(process: ProcessEntity):
        pass

    @abstractmethod
    def get_processes_in_lotes(self, size_of_lotes:int ) -> List[List[ProcessEntity]]:
        pass