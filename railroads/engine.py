
from amethyst.core  import Object, Attr
from amethyst.games import action, Engine, EnginePlugin, Filter
from amethyst.games.plugins import GrantManager, Grant

from . import turns


class RailroadEngine(Engine):
    map = Attr()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Most turn-based games will want the GrantManager and Turns plugin
        self.register_plugin(GrantManager())
        self.register_plugin(turns.DoubleBackStart())


class RailroadPlugin(EnginePlugin):
    AMETHYST_PLUGIN_COMPAT = 1  # Plugin API version

    def next_turn(self, game):
        game.turn_start()
        game.grant(game.turn_player(), Grant(name="end_turn"))

    @action
    def begin(self, game, stash):
        self.next_turn(game)

    @action
    def end_turn(self, game, stash):
        game.commit()
        self.next_turn(game)
