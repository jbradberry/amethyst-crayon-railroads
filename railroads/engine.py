
from amethyst.core  import Object, Attr
from amethyst.games import Engine, EnginePlugin, Filter
from amethyst.games.plugins import GrantManager, Turns, Grant


class RailroadEngine(Engine):
    map = Attr()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Most turn-based games will want the GrantManager and Turns plugin
        self.register_plugin(GrantManager())
        self.register_plugin(Turns())
