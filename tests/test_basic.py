import unittest

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
            grant = game.list_grants(game.turn_player_num())[0]
            self.assertEqual(grant.name, 'end_turn')
            game.trigger(game.turn_player(), grant.id, {})
            game.process_queue()

    def test_deck(self):
        game = engine.RailroadEngine({'players': list(range(3))})
        game.register_plugin(engine.RailroadPlugin())
        game.initialize()
        game.call_immediate("begin")

        self.assertFalse(game.discard_pile.stack)
        self.assertTrue(game.draw_pile.stack)


if __name__ == '__main__':
    unittest.main()
