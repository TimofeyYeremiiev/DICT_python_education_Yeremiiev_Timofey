"""Game - Main game class"""
import engine
import player


class DominoGame:
    """Game main class"""

    def __init__(self):
        self.engine = engine.Engine()

    def add_player(self, curr_player: player.Player):
        """Description:
            Adding player from outside
            Parameters:
                curr_player (player.Player) - Player for adding
            """
        self.engine.add_player(curr_player)

    def main_loop(self):
        """Description:
            Game main loop"""
        print("Starting...")
        two = ""
        while self.engine.step_player is None:
            self.engine.game_filed = []
            self.engine.re_give_players_figures()
            self.engine.step_player, first = self.engine.decide_who_is_first()
            self.engine.game_filed.append(first)
            two = first
        self.engine.players_figures[self.engine.step_player].remove(two)
        print(f"Start done, first is {self.engine.step_player.name}")
        while True:
            # Проверка на готовность
            for player_curr in list(self.engine.players_figures):
                if not player_curr == self.engine.step_player:
                    while not player_curr.is_ready():
                        pass
            # Игрок делает ход
            self.engine.step_player.make_step()
            # Проверка на победу
            if len(self.engine.players_figures[self.engine.step_player]) == 0 \
                    and len(self.engine.all_figures_list) == 0:
                # self.debug_print_game_stats()
                print(f"Игрок {self.engine.step_player.name} выиграл! Останавливаем игру...")
                break
            for player_curr in list(self.engine.players_figures):
                if len(self.engine.players_figures[player_curr]) == 0 \
                        and len(self.engine.all_figures_list) == 0:
                    # self.debug_print_game_stats()
                    print(f"Игрок {self.engine.step_player.name} выиграл! Останавливаем игру...")
                    break
            # Проверка на ничью
            counter = 0
            for figure in self.engine.all_figures_list:
                if self.engine.can_make_step_here(figure, True):
                    counter += 1
                if self.engine.can_make_step_here(figure, False):
                    counter += 1
            if counter == 0:
                for player_curr in list(self.engine.players_figures):
                    for figure in self.engine.players_figures[player_curr]:
                        if self.engine.can_make_step_here(figure, True):
                            counter += 1
                        if self.engine.can_make_step_here(figure, False):
                            counter += 1
                if counter == 0:
                    # self.debug_print_game_stats()
                    print("Ничья! Останавливаем игру...")
                    return

            self.engine.step_player = self.engine.next_player(self.engine.step_player)

    def debug_print_game_stats(self):
        """Description:
            Debug for me"""
        print("=========== Debug ===========")
        print("Figures at stock: ")
        print(self.engine.all_figures_list)
        print("Player 1 info:")
        print(self.engine.players_figures[list(self.engine.players_figures)[0]])
        print("Player 2 info:")
        print(self.engine.players_figures[list(self.engine.players_figures)[1]])
        print("Field:")
        print(self.engine.game_filed)
