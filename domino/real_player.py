"""Real player class"""
import re
import player
import game


class RealPlayer(player.Player):
    """Real player class, have interface for humans"""

    def __init__(self, player_name: str, caller: game.DominoGame):
        super().__init__(player_name, caller)

    def print_interface(self):
        """Description:
            Will print nice interface for you"""
        print("======================================================================")
        print(f"В запасе {len(self.game.engine.all_figures_list)} доминошек")
        print(f"Количество доминошек у следующего игрока "
              f"{len(self.game.engine.players_figures[self.game.engine.next_player(self)])}\n")
        game_field_string = ""
        if len(self.game.engine.game_filed) > 10:
            first_3 = self.game.engine.game_filed[0:3]
            last_3 = self.game.engine.game_filed[-3::1]
            for figure in first_3:
                game_field_string += f"|{str(figure[0])},{str(figure[1])}| "
            game_field_string += "... "
            for figure in last_3:
                game_field_string += f"|{str(figure[0])},{str(figure[1])}| "
        else:
            for figure in self.game.engine.game_filed:
                game_field_string += f"|{str(figure[0])},{str(figure[1])}| "
        print(game_field_string + "\n")
        player_figures_string = ""
        counter = 1
        for figure in self.game.engine.players_figures[self]:
            player_figures_string += f"{counter}:{str(figure)} "
            counter += 1
        print(player_figures_string)
        print("======================================================================")

    def is_ready(self) -> bool:
        """Description
            For ready confirming"""
        _ = input("Нажмите Enter для головности к следующему ходу")
        return True

    def make_step(self):
        """Description:
            Will print interface, procces input, and call methods. All for players"""
        self.print_interface()
        while True:
            action = input("Ваш ход: ")
            if action == "0":
                if self.game.engine.grab_figure(self):
                    print("Взято из резерва, пропуск хода")
                else:
                    print("Резерв пуст, пропуск хода")
                break
            math = re.search("[+].", action)
            if math is not None:
                if not len(self.game.engine.players_figures[self]) >= int(action.lstrip("+")) >= 1:
                    print(len(self.game.engine.players_figures[self]))
                    print(int(action.lstrip("+")))
                    print("Не верный индекс")
                    continue
                if self.game.engine.put_figure(self, self.game.engine.players_figures[self]
                                               [int(action.lstrip("+")) - 1], True):
                    print("Поставлено справа")
                    break
                print("Нельзя поставить")
                continue
            math = re.search("-.", action)
            if math is not None:
                if not len(self.game.engine.players_figures[self]) >= int(action.lstrip("-")) >= 1:
                    print("Не верный индекс")
                    continue
                if self.game.engine.put_figure(self, self.game.engine.players_figures[self]
                                               [int(action.lstrip("-")) - 1], False):
                    print("Поставлено слево")
                    break
                print("Нельзя поставить")
                continue
            print("Команда не распознана")
