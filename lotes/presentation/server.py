from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

import random
import re

from lotes import ProcessRepositoryImpl, LotesService, ArrayProcessesDatasource


process_repository = ProcessRepositoryImpl(
    ArrayProcessesDatasource()
)

lotes_service = LotesService(
    process_repository
)


app = Flask(__name__)
CORS(app)

@app.route("/")
def get_processes():


    process_repository.clean_processes()

    no_processes = request.args.get('noProcesses')

    if not no_processes:
        return jsonify({
            "error": "missing parameter 'noProcesses'"
        })

    if not no_processes.isdigit():
        return jsonify({
            "error": "noProcesses must be a number"
        })
    
    __create_processes(int(no_processes))

    processes = lotes_service.get_all_processes()

    return jsonify([
        process.process_to_dict() for process in processes
    ])


def __create_processes(number_of_process: int):

    for i in range(1,number_of_process+1):
        data = {
            "id": i,
            "name": "",
            "operation": "",
            "TEM": random.randint(5, 18),
            "elapsdT": 0,
            "is_finished": False
        }
        
        is_valid_operation = __validate_operation(data["operation"])
        while not is_valid_operation:
            data["operation"] = __generate_operation()
            is_valid_operation = __validate_operation(data["operation"])

        lotes_service.create_process(data)


def __validate_operation(operation):
    try:
        if re.match('^-?\d+[+*/%-]-?\d+$', operation) and '/0' not in operation and '%0' not in operation:
            return True
    except:
        return False



def __generate_operation():
    symbols = ['+', '-', '/', '*', '%']
    operation = str(random.randint(0, 100))+random.choice(symbols)+str(random.randint(0, 100))

    return operation


