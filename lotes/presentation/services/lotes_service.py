import uuid
from flask.json import jsonify

from lotes.domain import ProcessesRepository, ProcessEntity
from lotes.presentation.helpers import generate_operation, validate_operation

import random


class LotesService:

    def __init__(self, processesRepository: ProcessesRepository):
        self.processesRepository = processesRepository

    def get_process_by_id(self, id: int):
        return self.processesRepository.get_process_by_id(id)

    def get_all_processes(self):
        return self.processesRepository.get_all_processes()

    def get_finished_processes(self):
        return self.processesRepository.get_finished_processes()

    def create_process(self, data: dict):

        process = ProcessEntity.process_from_dict({
            **data
        })

        self.processesRepository.save(process)

        return process

    def get_processes_in_lotes(self, size_of_lotes=4):
        return self.processesRepository.get_processes_in_lotes(size_of_lotes)

    def create_processes_with_id_auto_generated(self, number_of_process):
        for i in range(0, number_of_process):
            data = {
                "id": uuid.uuid4(),
                "name": "",
                "operation": "",
                "TEM": random.randint(5, 18),
                "elapsdT": 0,
                "is_finished": False
            }

            is_valid_operation = validate_operation(data["operation"])
            while not is_valid_operation:
                data["operation"] = generate_operation()
                is_valid_operation = validate_operation(data["operation"])

            self.create_process(data)

    def create_processes_with_array_ids(self, number_of_process, ids):
        for i in range(0, number_of_process):
            data = {
                "id": ids[i],
                "name": "",
                "operation": "",
                "TEM": random.randint(5, 18),
                "elapsdT": 0,
                "is_finished": False
            }

            is_valid_operation = validate_operation(data["operation"])
            while not is_valid_operation:
                data["operation"] = generate_operation()
                is_valid_operation = validate_operation(data["operation"])

            self.create_process(data)

    def get_processes_json_format(self):
        processes = self.get_all_processes()
        processes_response = [process.process_to_dict() for process in processes]

        for process in processes_response:
            process.update({
                "time_blocked": 0,
                "addedToReadyForFirstTime": False,
                "addedToRunningProcessForFirstTime": False,
                "remaining_time_running": process["TEM"],
                "state": "queue"
            })

        return jsonify(processes_response)
