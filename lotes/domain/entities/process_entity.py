class ProcessEntity:

    def __init__(
            self, id: int,
            operation: str,
            TEM: int,
            elapsdT: int,
            is_finished: bool = False,
            time_finished: int = 0,
            elapsed_time_blocked: int = 0,
            initial_time: int = 0,
            response_time: int = 0,
            wait_time: int = 0,
            service_time: int = 0,
            return_time: int = 0,
    ):
        self.id = id
        self.operation = operation
        self.TEM = TEM
        self.elapsdT = elapsdT
        self.is_finished = is_finished
        self.time_finished = time_finished
        self.elapsed_time_blocked = elapsed_time_blocked
        self.initial_time = initial_time
        self.response_time = response_time
        self.wait_time = wait_time
        self.service_time = service_time
        self.return_time = return_time

    @classmethod
    def process_from_dict(cls, data: dict):
        return cls(data["id"], data["operation"], data["TEM"], data["elapsdT"])

    def process_to_dict(self):
        attributes = vars(self)
        return {key: value for key, value in attributes.items()}

    def __str__(self):
        return f"(id: {self.id} operation: {self.operation} TEM: {self.TEM})"

    def __repr__(self):
        return f"(id: {self.id} operation: {self.operation} TEM: {self.TEM})"
