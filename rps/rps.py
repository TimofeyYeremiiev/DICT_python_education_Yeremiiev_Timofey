"""rpsgame, rps game class"""
import json
import random


class RpsGame:

    def __init__(self):
        self.game_rules = ["6", "7", "8", "9", "10", "Андрей", "Артем", "Рубель"]
        self.player_name = None
        self.delta_score = 0

    def change_player_name(self):
        """Description
            Change player name
            """
        if not self.delta_score == 0:
            self.save_player_rang()
            self.delta_score = 0
        self.player_name = input("Введите новое имя игрока."
                                 " Абсолютно любое, никаких ограничений!\n> ")

    def view_player_rang(self):
        """Description
                    Will read and write player rank
                    """
        with open("ranking.txt", "r", encoding="utf-8") as rankfile:
            stringer = rankfile.read()
            if stringer == "":
                print(f"{self.player_name} rank is {self.delta_score}")
                return
            players_data = json.loads(stringer)
            if self.player_name in players_data:
                print(f"{self.player_name} rank is "
                      f"{players_data[self.player_name] + self.delta_score}")
            else:
                print(f"{self.player_name} rank is {self.delta_score}")

    def save_player_rang(self):
        """Description
               Will save player rank
                    """
        players_data = {self.player_name: 0}
        with open("ranking.txt", "r", encoding="utf-8") as rang_file:
            stringer = rang_file.read()
            if not stringer == "":
                players_data = json.loads(stringer)
        with open("ranking.txt", "w", encoding="utf-8") as rang_file:
            if self.player_name in players_data:
                players_data[self.player_name] += self.delta_score
            else:
                players_data[self.player_name] = self.delta_score
            self.delta_score = 0
            rang_file.write(json.dumps(players_data))

    def change_rules(self):
        """Description
                    Will change game rules
                    """
        game_rules = input("Или ведите новыe знаки в виде "
                           "набора символов с разделением"
                           " в виде пробелов... Или оставьте всё как есть!\n> ")
        if game_rules == "":
            return
        self.game_rules = game_rules.split(sep=" ")

    def get_winner(self, sym1, sym2):
        """Description

            Will decide, who is winner

            Parameters:
            sym1 (str): Players 1 symbol
            sym2 (str): Players 2 symbol

            Returns:
            int: 0 - draw, -1 - player 1 win, 1 - player 2 win
            """
        if sym1 == sym2:
            return 0
        starker_sym = []
        index1 = self.game_rules.index(sym1) + 1
        index2 = int(self.game_rules.index(sym1) +
                     (len(self.game_rules) - int(len(self.game_rules) % 2 == 1)) / 2)
        if index2 > len(self.game_rules):
            for element in range(index1, len(self.game_rules)):
                starker_sym.append(self.game_rules[element])
            for element in range(0, index2 - len(self.game_rules) + 1):
                starker_sym.append(self.game_rules[element])
        else:
            for element in range(index1, index2 + 1):
                starker_sym.append(self.game_rules[element])
        print("Подсказочка: Тебя могут вольнуть вот эти парни - "
              + str(starker_sym) + " И нет, это не для отлова оши"
              + "бок... Я СКАЗАЛ НЕТ!")
        if sym2 in starker_sym:
            return 1
        return -1

    def game_step(self, command):
        """Description

            Game iteration func

            Parameters:
            command (Str): Valid symbol or something else
            """
        if command not in self.game_rules:
            print("unexpacted beliberda")
            return
        computers_answer = random.choice(self.game_rules)
        result = self.get_winner(command, computers_answer)
        if result == 0:
            print(f"Ничья! Ибо компухтер выбрал {computers_answer}")
            self.delta_score += 50
            return
        if result == -1:
            print(f"Слава великому рандому,"
                  f" ты выиграл! Ход компа - {computers_answer}")
            self.delta_score += 100
            return
        print(f"Тебя и тут переиграли - компьютер выдал {computers_answer}")

    def game_cycle(self):
        """Description
            Game main cycle
            """
        self.change_player_name()
        self.change_rules()
        print("Введите команду: ")
        while True:
            command = input("> ")
            match command:
                case "help":
                    print("""
                    =======================================================================

                    Добро пожаловать в подобие камень-ножницы-и прочие сатанинские знаки!

                    Доступные опции:
                        !exit - свалить да подальше!
                        help - вывести бесполезные буковки
                        !chname - сменить имя
                        !getrank - получить ранг текущего игрока (А заодно и имя)
                        !svgame - сохранить ранг
                        !chrules - сменить набор символов (по сути - правила)
                        !getsymbs - получить набор символов

                        *Любой существующий символ* - вызвать бота на дуэль невиданных
                        масштабов!

                        Прятной игры!

                    =======================================================================
                    """)
                case "!exit":
                    break
                case "!chname":
                    self.change_player_name()
                case "!svgame":
                    self.save_player_rang()
                case "!getrank":
                    self.view_player_rang()
                case "!chrules":
                    self.change_rules()
                case "!getsymbs":
                    print(self.game_rules)
                case _:
                    self.game_step(command)