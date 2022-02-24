from .importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        if not path.endswith("csv"):
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            return list(csv.DictReader(file))
