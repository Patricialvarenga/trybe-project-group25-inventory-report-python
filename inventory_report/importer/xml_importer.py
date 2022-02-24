from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith("xml"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            tree = ET.parse(file)
            root = tree.getroot()

            final_list = []

            for element in root:
                product = {}
                for subelement in element:
                    product[subelement.tag] = subelement.text
                final_list.append(product)

            return final_list
