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

    # Полностью сбрасывает параметры калькулятора. На случай, если используется не один раз
    def clear_data(self):
        self.months = None
        self.payment_per_month = None
        self.last_payment = None
        self.credit_summ = None
        self.yearlich_percent = None
        self.month_add_payment = None
        self.result_summ = None

    # Спрашивает кредита сумму
    def get_credit_summ(self):
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

    # Ввод месяца
    def get_month(self):
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

    # Ввод ежемесячной суммы
    def get_payment(self):
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

    # Ввод процентов
    def get_percent(self):
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

    # Считает простую выплату в месяц по сумме кредита и месяцам,
    # при условии необзодимости округления и сохранения суммы
    def calc_payment_by_summ_and_mont(self):
        self.payment_per_month = round(self.credit_summ / self.months, 0)
        self.last_payment = None
        if self.payment_per_month != self.credit_summ / self.months:
            self.last_payment = self.credit_summ - self.payment_per_month * self.months + self.payment_per_month

    # Считает просто месяца по сумме кредита и выплатам в месяц,
    # при условии необзодимости округления и сохранения суммы
    def calc_mont_by_summ_and_payment(self):
        self.months = round(self.credit_summ / self.payment_per_month, 0)
        self.last_payment = None
        if self.months != self.credit_summ / self.payment_per_month:
            self.last_payment = self.credit_summ - self.payment_per_month * self.months + self.payment_per_month

    # Считает ауетарный или как он там называется кредит, и выводит информацию.
    def calc_au_credit(self):
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

    # Считает дифференциальный кредит по особым формулам
    def calc_di_credit(self):
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

    # получить переплату, возращает переплату как инт
    def get_overpayment(self):
        return self.credit_summ * self.yearlich_percent

    # Сеттеры и геттеры
    def set_months(self, months: int):
        if months <= 0:
            raise ValueError("Too small")
        self.months = months

    def set_payment(self, payment: int):
        if payment <= 0:
            raise ValueError("Too small")
        self.payment_per_month = payment

    def set_percent(self, percent: float):
        if percent < 0:
            raise ValueError("Too small")
        self.yearlich_percent = percent

    def set_credit_summ(self, summ: int):
        if summ <= 0:
            raise ValueError("Too small")
        self.credit_summ = summ
