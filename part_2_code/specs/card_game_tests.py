import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("Hearts", 5)
        self.card2 = Card("Spades", 10)
        self.cards = [self.card1, self.card2]


    def test_card_has_suit(self):
        self.assertEqual("Hearts", self.card1.suit)

    def test_card_has_value(self):
        self.assertEqual(5, self.card1.value)


    def test_can_check_for_ace(self):
        self.card_game.check_for_ace(self.card1)
        expected = False
        actual = self.card_game.check_for_ace(self.card1)
        self.assertEqual(actual, expected)

    def test_highest_card(self):
        self.card_game.highest_card(self.card1, self.card2)
        expected = self.card2
        actual = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(expected, actual)

    def test_card_total(self):
        self.card_game.cards_total(self.cards)
        expected = "You have a total of 15"
        actual = self.card_game.cards_total(self.cards)
        self.assertEqual(expected, actual)