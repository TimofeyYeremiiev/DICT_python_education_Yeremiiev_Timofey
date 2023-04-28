"""credit_calculator - считает кредиты"""


class CreditCalculator:

    def __init__(self):
        self.months = None
        self.payment_per_month = None
        self.last_payment = None
        self.credit_summ = None
        self.yearlich_percent = None
        self.month_add_payment = None
        self.result_summ = None

    def clear_data(self):
        """Description

            Clear data for credit calculator

                """
        self.months = None
        self.payment_per_month = None
        self.last_payment = None
        self.credit_summ = None
        self.yearlich_percent = None
        self.month_add_payment = None
        self.result_summ = None

    def get_credit_summ(self):
        """Description
            Input credit summ
                """
        while True:
            credit_summ = input("Введите сумму кредита: \n")
            if not credit_summ.isnumeric():
                print("Не число")
                continue
            credit_summ = float(credit_summ)
            if credit_summ <= 0:
                print("Не может быть менее или равно нулю")
                continue
            self.credit_summ = credit_summ
            break

    def get_month(self):
        """Description
            Input month
                """
        while True:
            month = input("Ведите месяц: \n")
            if not month.isnumeric():
                print("Не число")
                continue
            month = int(month)
            if month <= 0:
                print("Не может быть менее или равно нулю")
                continue
            self.months = month
            break

    def get_payment(self):
        """Description
             Input payment
                """
        while True:
            payment = input("Ведите желаемые выплаты в месяц: \n")
            if not payment.isnumeric():
                print("Не число")
                continue
            payment = float(payment)
            if payment <= 0:
                print("Не может быть менее или равно нулю")
                continue
            self.payment_per_month = payment
            break

    def get_percent(self):
        """Description
            Input percent
                """
        while True:
            percent = input("Введите годвой процент\n")
            try:
                percent = float(percent)
                if percent < 0:
                    print("Не может быть отрицательным")
                    continue
                self.yearlich_percent = percent
                break
            except Exception:
                print("Не процент")

    def calc_payment_by_summ_and_mont(self):
        """Description
            Will calc payment by summ and month
                """
        self.payment_per_month = round(self.credit_summ / self.months, 0)
        self.last_payment = None
        if self.payment_per_month != self.credit_summ / self.months:
            self.last_payment = self.credit_summ - self.payment_per_month * self.months + self.payment_per_month

    def calc_mont_by_summ_and_payment(self):
        """Description
            Will calc month by summ and payment
                """
        self.months = round(self.credit_summ / self.payment_per_month, 0)
        self.last_payment = None
        if self.months != self.credit_summ / self.payment_per_month:
            self.last_payment = self.credit_summ - self.payment_per_month * self.months + self.payment_per_month

    def calc_au_credit(self):
        """Description
            Calc au credit
                """
        # Проверка ввода
        if self.credit_summ is None:
            self.get_credit_summ()
        if self.months is None:
            if self.payment_per_month is not None:
                self.calc_mont_by_summ_and_payment()
            else:
                self.get_month()
        if self.yearlich_percent is None:
            self.get_percent()
        if self.payment_per_month is None:
            if self.months is not None:
                self.calc_payment_by_summ_and_mont()
            else:
                self.get_payment()
        # Счет кредита по особым формулам
        for a in range(0, self.months):
            if self.last_payment is not None and a == self.months - 1:
                print(f"Month {a}: {self.last_payment + self.last_payment * self.yearlich_percent / 100}"
                      f" ({self.last_payment}"
                      f" + {self.last_payment * self.yearlich_percent / 100})")
            else:
                print(f"Month {a}: {self.payment_per_month + self.payment_per_month * self.yearlich_percent / 100}"
                      f" ({self.payment_per_month}"
                      f" + {self.payment_per_month * self.yearlich_percent / 100})")

    def calc_di_credit(self):
        """Description
            calc di credit
                """
        #Проверка ввода
        if self.credit_summ is None:
            self.get_credit_summ()
        if self.months is None:
            if self.payment_per_month is not None:
                self.calc_mont_by_summ_and_payment()
            else:
                self.get_month()
        if self.yearlich_percent is None:
            self.get_percent()
        if self.payment_per_month is None:
            if self.months is not None:
                self.calc_payment_by_summ_and_mont()
            else:
                self.get_payment()
        # Особаая магия формул
        las_summ = self.credit_summ

        for a in range(0, self.months):
            if self.last_payment is not None and a == self.months - 1:
                print(f"Month {a}: {self.last_payment + las_summ * self.yearlich_percent / 100 / 12} "
                      f"({self.last_payment}"
                      f" + {las_summ * self.yearlich_percent / 12 / 100})")
                las_summ -= self.last_payment
            else:
                print(f"Month {a}: {self.payment_per_month + las_summ * self.yearlich_percent / 100 / 12} "
                      f"({self.payment_per_month}"
                      f" + {las_summ * self.yearlich_percent / 12 / 100})")
                las_summ -= self.payment_per_month
        pass

    def get_overpayment(self):
        """Description
            Will give overpayment

            Returns:
                int: overpayment
                """
        return self.credit_summ * self.yearlich_percent

    # Сеттеры
    def set_months(self, months: int):
        """Description

                Setter for months

                Parameters:
                months (int): - months
                """
        if months <= 0:
            raise ValueError("Too small")
        self.months = months

    def set_payment(self, payment: int):
        """Description

                        Setter for payment

                        Parameters:
                        payment (int): - payment
                        """
        if payment <= 0:
            raise ValueError("Too small")
        self.payment_per_month = payment

    def set_percent(self, percent: float):
        """Description

                        Setter for percent

                        Parameters:
                        percent (float): - percent
                        """
        if percent < 0:
            raise ValueError("Too small")
        self.yearlich_percent = percent

    def set_credit_summ(self, summ: int):
        """Description

                        Setter for summ

                        Parameters:
                        summ (int): - summ
                        """
        if summ <= 0:
            raise ValueError("Too small")
        self.credit_summ = summ

