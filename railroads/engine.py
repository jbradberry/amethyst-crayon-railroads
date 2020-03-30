
from amethyst.core  import Object, Attr
from amethyst.games import action, Engine, EnginePlugin, Filter
from amethyst.games.objects import Pile
from amethyst.games.plugins import GrantManager, Grant, Turns


class RailroadEngine(Engine):
    map = Attr()
    draw_pile = Attr(default=Pile)
    discard_pile = Attr(default=Pile)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Most turn-based games will want the GrantManager and Turns plugin
        self.register_plugin(GrantManager())
        self.register_plugin(Turns(setup_rounds=(1, -1)))


class RailroadPlugin(EnginePlugin):
    AMETHYST_PLUGIN_COMPAT = 1  # Plugin API version

    def next_turn(self, game):
        game.turn_start()
        game.grant(game.turn_player(), Grant(name="draw"))
        game.grant(game.turn_player(), Grant(name="end_turn"))

    @action
    def begin(self, game, stash):
        self.load_deck(game)
        self.shuffle(game)
        self.next_turn(game)

    @action
    def draw(self, game, stash):
        card = game.draw_pile.pop()
        game.discard_pile.append(card)

    @action
    def end_turn(self, game, stash):
        game.commit()
        self.next_turn(game)

    def load_deck(self, game):
        game.discard_pile.extend(range(156))

    def shuffle(self, game):
        game.discard_pile.shuffle()
        deck = game.discard_pile.remove()
        game.draw_pile.extend(deck)
