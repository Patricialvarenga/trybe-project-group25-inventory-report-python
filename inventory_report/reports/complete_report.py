from .simple_report import SimpleReport


class CompleteReport:
    def generate(data):
        simple_report = SimpleReport.generate(data)

        stock = {}

        products_in_stock = "Produtos estocados por empresa: \n"

        for company in data:
            stock[company["nome_da_empresa"]] = (
                stock.get(company["nome_da_empresa"], 0) + 1
            )

        products_in_stock += (
            "\n".join(
                f"- {company}: {quantity}"
                for company, quantity in stock.items()
            )
            + "\n"
        )

        return "\n".join([simple_report, products_in_stock])
