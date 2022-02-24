data = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-02-18",
        "data_de_validade": "2022-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
    {
        "id": "2",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2019-12-06",
        "data_de_validade": "2022-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2",
    },
    {
        "id": "3",
        "nome_do_produto": "NITROUS OXIDE",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2019-12-22",
        "data_de_validade": "2023-11-07",
        "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
        "instrucoes_de_armazenamento": "instrucao 3",
    },
    {
        "id": "4",
        "nome_do_produto": "Norepinephrine Bitartrate",
        "nome_da_empresa": "Cantrell Drug Company",
        "data_de_fabricacao": "2019-12-24",
        "data_de_validade": "2024-08-19",
        "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
        "instrucoes_de_armazenamento": "instrucao 4",
    },
    {
        "id": "5",
        "nome_do_produto": "ACETAMINOPHEN, PHENYLEPHRINE HYDROCHLORIDE",
        "nome_da_empresa": "Moore Medical LLC",
        "data_de_fabricacao": "2020-04-14",
        "data_de_validade": "2024-01-14",
        "numero_de_serie": "LV23 ELDS 2GD5 X19P VCSI K",
        "instrucoes_de_armazenamento": "instrucao 5",
    },
    {
        "id": "6",
        "nome_do_produto": "Silicea Belladonna",
        "nome_da_empresa": "Cantrell Drug Company",
        "data_de_fabricacao": "2020-07-18",
        "data_de_validade": "2023-10-05",
        "numero_de_serie": "FR57 7414 7254 046O IHVX AV6L H71",
        "instrucoes_de_armazenamento": "instrucao 6",
    },
    {
        "id": "7",
        "nome_do_produto": "Spironolactone",
        "nome_da_empresa": "REMEDYREPACK",
        "data_de_fabricacao": "2020-07-17",
        "data_de_validade": "2022-11-18",
        "numero_de_serie": "SM28 B981 5118 903W JY0C 5KVO 3QD",
        "instrucoes_de_armazenamento": "instrucao 7",
    },
    {
        "id": "8",
        "nome_do_produto": "Aspirin",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2020-02-22",
        "data_de_validade": "2023-03-14",
        "numero_de_serie": "KZ63 800H NM4B ZOWB YYUI",
        "instrucoes_de_armazenamento": "instrucao 8",
    },
    {
        "id": "9",
        "nome_do_produto": "eucalyptus globulus",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2019-09-06",
        "data_de_validade": "2023-05-21",
        "numero_de_serie": "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
        "instrucoes_de_armazenamento": "instrucao 9",
    },
    {
        "id": "10",
        "nome_do_produto": "Titanium Dioxide",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2019-12-08",
        "data_de_validade": "2022-12-08",
        "numero_de_serie": "FR29 5791 5333 58XR G4PR IG28 D08",
        "instrucoes_de_armazenamento": "instrucao 10",
    },
]

import datetime


class SimpleReport:
    def __init__(self, data_list):
        self.data = data_list

    def generate(self):
        oldest_company = sorted(
            self.data, key=lambda company: company["data_de_fabricacao"]
        )

        closest_date = sorted(
            self.data, key=lambda company: company["data_de_validade"]
        )

        valid_dates = filter(
            lambda closest: datetime.datetime.now()
            >= datetime.datetime.strptime(
                closest["data_de_validade"], "%Y-%m-%d"
            ),
            closest_date,
        )

        max_products_in_stock = {}

        for company in self.data:
            if company["nome_da_empresa"] not in max_products_in_stock:
                max_products_in_stock[company["nome_da_empresa"]] = 1
            else:
                max_products_in_stock[company["nome_da_empresa"]] += 1

        max_products_in_stock = sorted(
            max_products_in_stock.items(), key=lambda company: company[1]
        )

        return (
            f"Data de fabricação mais antiga: {oldest_company[0]['data_de_fabricacao']}\n"
            f"Data de validade mais próxima: YYYY-MM-DD\n"
            f"Empresa com maior quantidade de produtos estocados: {max_products_in_stock[-1][0]}"
        )


print(SimpleReport(data).generate())
