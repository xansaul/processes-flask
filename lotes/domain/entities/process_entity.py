
class ProcessEntity:

    def __init__(self, id, name, operation, TEM):
        self.id = id
        self.name = name
        self.operation = operation
        self.TEM = TEM

    @classmethod
    def process_from_dict(cls, data:dict):
        return cls(data["id"], data["name"], data["operation"], data["TEM"])

    def process_to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "operation":self.operation,
            "TEM": self.TEM
        }


    def __str__(self):
        return f"({self.name} -> id: {self.id} operation: {self.operation} TEM: {self.TEM})"
    
    def __repr__(self):
        return f"({self.name} -> id: {self.id} operation: {self.operation} TEM: {self.TEM})"