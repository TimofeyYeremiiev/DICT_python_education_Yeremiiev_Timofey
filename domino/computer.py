"""Computer mind player"""
import game
import player


class ComputerPlayer(player.Player):
    """Computer solution for afk-problems"""

    def __init__(self, player_name: str, caller: game.DominoGame):
        super().__init__(player_name, caller)
        self.figures_score = []
        self.figures_costing = {0: 5, 1: 2, 2: 4, 3: 1, 4: 3, 5:3, 6: 0}

    def is_ready(self) -> bool:
        """Description:
            Computer is always ready for beat you!"""
        return True

    def make_step(self):
        """Description:
            Computer will make step"""
        self.figures_score = {}
        for figure in self.game.engine.players_figures[self]:
            fig_score = 0
            for num in figure:
                fig_score += self.figures_costing[num]
            self.figures_score[fig_score] = figure
        figures_order = list(self.figures_score)
        figures_order.sort()
        for tag in figures_order:
            if self.game.engine.put_figure(self, self.figures_score[tag], True):
                return
            if self.game.engine.put_figure(self, self.figures_score[tag], False):
                return
        self.game.engine.grab_figure(self)
