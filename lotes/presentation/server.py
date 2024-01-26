from flask import Flask
from flask.json import jsonify

from lotes.infrastructure.repositories.processes_repository_impl import ProcessRepositoryImpl
from lotes.infrastructure.datasources.array_processes_datasource import ArrayProcessesDatasource
from lotes.domain.services.lotes_service import LotesService

app = Flask(__name__)

process_repository = ProcessRepositoryImpl(
    ArrayProcessesDatasource()
)

lotes_service = LotesService(
    process_repository
)


@app.route("/")
def get_lotes():

    processes = lotes_service.get_all_processes()

    return jsonify([
        process.process_to_dict() for process in processes
    ])