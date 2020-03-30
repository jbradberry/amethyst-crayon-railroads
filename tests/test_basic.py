import unittest

from amethyst.games import Filter

from railroads import engine


class RailroadEngineTest(unittest.TestCase):

    def test_basic(self):
        game = engine.RailroadEngine()
        game.register_plugin(engine.RailroadPlugin())

    def test_doubleback(self):
        game = engine.RailroadEngine({'players': list(range(3))})
        game.register_plugin(engine.RailroadPlugin())
        game.initialize()
        game.call_immediate("begin")

        for turn, (round, player) in enumerate(zip([0, 0, 0, 1, 1, 1], [0, 1, 2, 2, 1, 0])):
            self.assertEqual(game.turn_round(), 'setup-{}'.format(round))
            self.assertEqual(game.turn_number(), turn)
            self.assertEqual(game.turn_player_num(), player)
            game.call_immediate("end_turn")

    def test_grants(self):
        game = engine.RailroadEngine({'players': list(range(3))})
        game.register_plugin(engine.RailroadPlugin())
        game.initialize()
        game.call_immediate("begin")

        for p in range(3):
            self.assertEqual(game.turn_number(), p)
            self.assertEqual(game.turn_player_num(), p)
            self.assertListEqual([g.name for g in game.list_grants(game.turn_player_num())],
                                 ['draw', 'end_turn'])
            grant = game.list_grants(game.turn_player_num(), Filter(name='end_turn'))[0]
            game.trigger(game.turn_player(), grant.id, {})
            game.process_queue()

    def test_deck(self):
        game = engine.RailroadEngine({'players': list(range(3))})
        game.register_plugin(engine.RailroadPlugin())
        game.initialize()
        game.call_immediate("begin")

        self.assertEqual(game.discard_pile.count(), 0)
        self.assertEqual(game.draw_pile.count(), 156)

    def test_draw(self):
        game = engine.RailroadEngine({'players': list(range(3))})
        game.register_plugin(engine.RailroadPlugin())
        game.initialize()
        game.call_immediate("begin")

        for p in range(3):
            draw = game.list_grants(game.turn_player_num(), Filter(name='draw'))[0]
            game.trigger(game.turn_player(), draw.id, {})
            end_turn = game.list_grants(game.turn_player_num(), Filter(name='end_turn'))[0]
            game.trigger(game.turn_player(), end_turn.id, {})
            game.process_queue()
            self.assertEqual(game.discard_pile.count(), p + 1)
            self.assertEqual(game.draw_pile.count(), 156 - p - 1)


if __name__ == '__main__':
    unittest.main()
