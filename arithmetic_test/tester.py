"""Tester, класс для проведения тестов над мешками с мясом"""
import random
import math


class Tester:

    def __init__(self):
        self.operations_lvl1 = {"+": lambda a, b: a + b,
                                "-": lambda a, b: a - b,
                                "*": lambda a, b: a * b}
        self.operations_lvl2 = {"^2": lambda a, b: pow(a, max(min(b, 2), 2))}
        self.operations_lvl3 = {" разделить на себя же, потом в третей степени, но сначало умножить на ": lambda a, b: \
            pow(a / a * b, max(min(b, 3), 3))}

    @staticmethod
    def do_test(operations_list):
        """Description

            Will do test and return, correct or no

            Parameters:
            operations_list (list): rules for testing in special format ("label": "answer func")

            Returns:
            bool: True if correct, else - False
            """
        while True:
            operation, func = random.choice(operations_list)
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            if func(a, b) >= 0:
                break

        while True:
            answer = input(f"Сколько будет {a} {operation} {b}?\n")
            if not answer.isnumeric():
                print("Введите число, числами.")
                continue
            answer = int(answer)
            if not (answer == func(a, b)):
                print("НЕПРАВИЛЬНО!")
                return False
            else:
                return True

    @staticmethod
    def print_and_save_res(self, score: int):
        """Description

            Will print result, ask for saving, and save

            Parameters:
            score (int): Players score
            """
        print(f"Результат - {score}/5, {score / 5 * 100}%")
        save_res = input("Сохранить результат?(y/other)")
        if save_res == "y":
            with open("results.txt", "a", encoding="utf-8") as file:
                file.write(f"Результат - {score}/5, {score / 5 * 100}%")

    def start(self):
        """Description

            Main game cycle
            """
        while True:
            print(
                """Выберите уровень сложности:

                    1. Простые операции сложения вычитания и унижения,
                    цифры от 2 до 9.
                    2. Тот же что и первый, только может появиться еще и квадрат\n     
            """)
            level = input(">")
            try:
                level = int(level)
            except ValueError:
                print("Числом")
                continue
            if not (0 < level < 3):
                print("Существующий пункт")
                continue

            score = 0
            match level:
                case 1:
                    for a in range(0, 5):
                        if self.do_test(list(self.operations_lvl1.items())):
                            score += 1
                    self.print_and_save_res(score)
                case 2:
                    for a in range(0, 5):
                        if self.do_test(list(self.operations_lvl1.items()) +
                                        list(self.operations_lvl2.items())):
                            score += 1
                    self.print_and_save_res(score)
                case 3:
                    for a in range(0, 5):
                        if self.do_test(list(self.operations_lvl1.items()) +
                                        list(self.operations_lvl2.items()) +
                                        list(self.operations_lvl3.items())):
                            score += 1
                    self.print_and_save_res(score)