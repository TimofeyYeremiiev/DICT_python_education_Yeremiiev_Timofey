"""Domino game  class - Engine"""
import random
import player


class Engine:
    """Contain methods and data for good game"""

    def __init__(self):
        self.players_figures = {}
        self.step_player = None
        self.game_filed = []

        self.all_figures_list = self.generate_figures()

    @staticmethod
    def generate_figures() -> list:
        """Description
            Will generate valid figures list
            Returns:
                list: - valid figures list"""
        all_figures_list = []
        for var_a in range(0, 7):
            for var_b in range(0, 7):
                if not ([var_a, var_b] in all_figures_list
                        or [var_b, var_a] in all_figures_list):
                    all_figures_list.append([var_a, var_b])
        return all_figures_list

    def re_give_players_figures(self):
        """Description:
            Will RE-give figures for all players, when figures are not enough - add more"""
        while len(self.players_figures.keys()) * 7 >= len(self.all_figures_list) - 10:
            self.all_figures_list.extend(self.generate_figures())
        for player_obj in self.players_figures:
            self.players_figures[player_obj] = []
            for iteration in range(0, 7):
                self.players_figures[player_obj].append(random.choice(self.all_figures_list))
                self.all_figures_list.remove(self.players_figures[player_obj][iteration])

    def decide_who_is_first(self):
        """Description
            Will decide, who are first will make step
            Returns:
                None, None: - if draw
                player, list: - if decided"""
        for player_obj, figure_list in self.players_figures.items():
            for player_figure in figure_list:
                if player_figure[0] == player_figure[1]:
                    return player_obj, player_figure
        return None, None

    def put_figure(self, curr_player: player.Player, figure: list, direction: bool) -> bool:
        """Description
            Will put figure from players inventory to the game field
            Parameters:
                curr_player (player.Player): player from
                figure (list): figure to
                direction (bool): True - right, False - left
            Returns:
                bool: - True of success, otherwise false"""
        if self.can_make_step_here(figure, direction):
            self.players_figures[curr_player].remove(figure)
            if direction:
                if not figure[0] == self.game_filed[len(self.game_filed) - 1][1]:
                    figure[0], figure[1] = figure[1], figure[0]
                self.game_filed.append(figure)
            else:
                if not figure[1] == self.game_filed[0][0]:
                    figure[0], figure[1] = figure[1], figure[0]
                self.game_filed.insert(0, figure)
            return True
        return False

    def can_make_step_here(self, figure: list, direction: bool) -> bool:
        """Description:
            Will decide, can or not put here figure
            Parameters:
                figure (list): figure
                direction (bool): True - right, False - left
            Returns:
                bool: True if can, otherwise - False"""
        if direction:
            figure_2 = self.game_filed[len(self.game_filed) - 1]
            if figure[0] == figure_2[1] or figure[1] == figure_2[1]:
                return True
            return False
        figure_2 = self.game_filed[0]
        if figure[0] == figure_2[0] or figure[1] == figure_2[0]:
            return True
        return False

    def add_player(self, new_player: player.Player):
        """Description:
            Will add player to game
            Parameters:
                new_player (player.Player): Player to add"""
        self.players_figures[new_player] = []

    def next_player(self, curr_player: player.Player):
        """Description:
            Will return next player
            Parameters:
                curr_player (player.Player): Player from
            Returns:
                player: - next player"""
        curr_index = list(self.players_figures).index(curr_player)
        if curr_index == len(self.players_figures)-1:
            return list(self.players_figures)[0]
        return list(self.players_figures)[curr_index + 1]

    def grab_figure(self, curr_player: player.Player) -> bool:
        """Description:
            Will give player random figure from stack
            Parameters:
                curr_player (player.Player): will grab for THIS player
            Returns:
                bool: True if success, False if its empty"""

        if len(self.all_figures_list) != 0:
            figure = random.choice(self.all_figures_list)
            self.all_figures_list.remove(figure)
            self.players_figures[curr_player].append(figure)
            return True
        return False
