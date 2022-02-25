# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Iterable

# ref https://docs.python.org/3/library/xml.etree.elementtree.html
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator

from .inventory import ReadCSV, ReadJSON, ReadXML


class Inventory:
    def import_data(path, report_type):
        method = (
            path.endswith("json")
            and ReadJSON
            or path.endswith("csv")
            and ReadCSV
            or ReadXML
        )
        return method.toList(path, report_type)


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        self.data += self.importer.import_data(path)

        if report_type == "simples":
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
