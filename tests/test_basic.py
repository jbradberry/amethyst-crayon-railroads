import unittest

from railroads import engine


class RailroadEngineTest(unittest.TestCase):

    def test_basic(self):
        game = engine.RailroadEngine()

    def test_doubleback(self):
        game = engine.RailroadEngine({'players': list(range(3))})
        game.initialize()
        game.call_immediate("begin")

        for turn, player in enumerate([0, 1, 2, 2, 1, 0]):
            self.assertEqual(game.turn_number(), turn)
            self.assertEqual(game.turn_player_num(), player)
            game.call_immediate("end_turn")

    def test_grants(self):
        game = engine.RailroadEngine({'players': list(range(3))})
        game.initialize()
        game.call_immediate("begin")

        for p in range(3):
            self.assertEqual(game.turn_number(), p)
            self.assertEqual(game.turn_player_num(), p)
            grant = game.list_grants(game.turn_player_num())[0]
            self.assertEqual(grant.name, 'end_turn')
            game.trigger(game.turn_player(), 'end_turn', {})
            game.process_queue()
