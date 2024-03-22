from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

import ast

from lotes import ProcessRepositoryImpl, LotesService, ArrayProcessesDatasource
from lotes.presentation.helpers import validate_array_ids

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

    if not no_processes or not no_processes.isdigit():
        return jsonify({"error": "noProcesses must be a positive integer"})

    no_processes = int(no_processes)

    processes_ids = request.args.get('ids')

    if processes_ids:
        try:
            ids_array = ast.literal_eval(processes_ids)
            validate_array_ids(ids_array, no_processes)

            lotes_service.create_processes_with_array_ids(no_processes, ids_array)
        except Exception as e:
            return jsonify({
                "error": str(e)
            })
    else:
        lotes_service.create_processes_with_id_auto_generated(no_processes)

    return lotes_service.get_processes_json_format()


