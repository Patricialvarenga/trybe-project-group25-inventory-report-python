from .importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):

        if not path.endswith("json"):
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            return json.load(file)
