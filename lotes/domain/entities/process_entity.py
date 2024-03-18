
class ProcessEntity:

    def __init__(
            self, id:int, 
            operation:str, 
            TEM:int, 
            elapsdT:int, 
            is_finished:bool=False , 
            time_finished:int = 0,
            is_blocked:bool = False, 
            remaining_time_blocked:int = 0,
            initial_time: int = 0,
            response_time: int = 0,
            ):
        self.id = id
        self.operation = operation
        self.TEM = TEM
        self.elapsdT = elapsdT
        self.is_finished = is_finished
        self.time_finished = time_finished
        self.is_blocked = is_blocked
        self.remaining_time_blocked = remaining_time_blocked
        self.initial_time = initial_time
        self.response_time = response_time
        
        

    @classmethod
    def process_from_dict(cls, data:dict):
        return cls(data["id"], data["operation"], data["TEM"], data["elapsdT"])

    def process_to_dict(self):
        return {
            "id":self.id,
            "operation":self.operation,
            "TEM": self.TEM,
            "elapsdT": self.elapsdT,
            "is_finished": self.is_finished,
            "time_finished": self.time_finished,
            "is_blocked": self.is_blocked,
            "remaining_time_blocked": self.remaining_time_blocked,
            "initial_time": self.initial_time,
            "response_time": self.response_time,
            "remaining_time_running": self.TEM
        }

    


    def __str__(self):
        return f"(id: {self.id} operation: {self.operation} TEM: {self.TEM})"
    
    def __repr__(self):
        return f"(id: {self.id} operation: {self.operation} TEM: {self.TEM})"