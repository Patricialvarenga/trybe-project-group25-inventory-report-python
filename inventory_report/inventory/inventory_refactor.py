import csv
import json

# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Iterable

# ref https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class ReadJSON:
    def toList(path, type):
        if type == "simples":
            with open(path, "r") as file:
                return SimpleReport.generate(list(json.loads(file.read())))

        if type == "completo":
            with open(path, "r") as file:
                return CompleteReport.generate(list(json.loads(file.read())))


class ReadCSV:
    def toList(path, type):
        if type == "simples":
            with open(path, "r") as file:
                return SimpleReport.generate(list(csv.DictReader(file)))

        if type == "completo":
            with open(path, "r") as file:
                return CompleteReport.generate(list(csv.DictReader(file)))


class ReadXML:
    def toList(path, type):
        with open(path, "r") as file:
            tree = ET.parse(file)
            root = tree.getroot()

            products = []
            for element in root:
                product = {}
                for subelement in element:
                    product[subelement.tag] = subelement.text
                products.append(product)
            if type == "simples":
                return SimpleReport.generate(products)

            if type == "completo":
                return CompleteReport.generate(products)


class Inventory:
    def import_data(path, report_type):
        if path.endswith("json"):
            return ReadJSON.toList(path, report_type)

        if path.endswith("csv"):
            return ReadCSV.toList(path, report_type)

        if path.endswith("xml"):
            return ReadXML.toList(path, report_type)


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
