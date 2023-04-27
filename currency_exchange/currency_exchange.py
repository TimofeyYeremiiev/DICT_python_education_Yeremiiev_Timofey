"""Currency exchanger module - хорошо делает запросы и умножение. Ну и обмен валют"""
import requests


class CurrencyExchanger:
    """Description
        Умело меняет одно на другое
        """

    def __init__(self):
        self.cache = {}
        self.valute_1 = None
        self.valute_2 = None
        self.value = 0

    @staticmethod
    def get_valuta():
        """Description

            Will input caluta

            Returns:
            str: valuta name
            """
        while True:
            variable = input("Введите валюту\n")
            if not len(variable) > 3:
                return variable
            print("incorrect!")

    @staticmethod
    def get_money():
        """Description

            Will input money count

            Returns:
            float: money value
            """
        while True:
            variable = input("Введите количество валюты\n")
            try:
                return float(variable)
            except:
                print("Не число")

    def make_request(self, valute_name: str):
        """Description

            Will make request

            Parameters:
            valute_name (str): valute name
            """
        req = requests.get(f'http://www.floatrates.com/daily/{valute_name.lower()}.json')
        req = req.json()
        self.cache[valute_name] = req

    def main_loop(self):
        """Description
            Main loop
            """
        while True:
            self.valute_1 = self.get_valuta()
            self.valute_2 = self.get_valuta()
            self.value = self.get_money()

            try:
                if self.valute_1 not in self.cache:
                    self.make_request(self.valute_1)
            except:
                print("Ошибка получения курса. Или сайт недоступен,"
                      " или кто то ввел неправильно название!")
                continue
            response = self.cache[self.valute_1][self.valute_2]["rate"] * self.value
            print(f"From {self.valute_1} to {self.valute_2}: {response}")
