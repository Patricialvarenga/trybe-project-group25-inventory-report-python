import csv
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    def import_data(path, type):
        if type == "simples":
            with open(path, "r") as file:
                return SimpleReport.generate(list(csv.DictReader(file)))

        if type == "completo":
            with open(path, "r") as file:
                return CompleteReport.generate(list(csv.DictReader(file)))


print(Inventory.import_data("inventory_report/data/inventory.csv", "simples"))
