import csv
import json

# ref https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


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
        method = (
            path.endswith("json")
            and ReadJSON
            or path.endswith("csv")
            and ReadCSV
            or ReadXML
        )
        return method.toList(path, report_type)
