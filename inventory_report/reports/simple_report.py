from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, data):
        oldest_company = sorted(
            data, key=lambda company: company["data_de_fabricacao"]
        )[0]["data_de_fabricacao"]

        closest_date = str(
            min(
                [
                    datetime.strptime(company["data_de_validade"], "%Y-%m-%d")
                    for company in data
                    if datetime.strptime(
                        company["data_de_validade"], "%Y-%m-%d"
                    )
                    >= datetime.now()
                ]
            )
        ).replace(" 00:00:00", "")

        stock = {}

        for company in data:
            if company["nome_da_empresa"] not in stock:
                stock[company["nome_da_empresa"]] = 1
            else:
                stock[company["nome_da_empresa"]] += 1

        stock = sorted(stock.items(), key=lambda company: company[1])[-1][0]

        return (
            f"Data de fabricação mais antiga: {oldest_company}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {stock}\n"
        )


# print(SimpleReport(data).generate())
