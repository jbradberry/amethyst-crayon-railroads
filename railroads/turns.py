
from amethyst.games.plugins import Turns


class DoubleBackStart(Turns):

    def _start(self, engine, player=None, round=None, step=1):
        N = len(engine.players)
        self.current_turn  += step
        self.current_round = self.current_turn // N if round is None else round

        current_player = self.current_turn % N if player is None else player
        self.current_player = current_player if self.current_round != 1 else N - current_player - 1
