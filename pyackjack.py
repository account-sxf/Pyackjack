"""
Pyackjack!

A simplified blackjack game in idiotic python.

by Joel Taylor and Rory Samson
"""

import random
import time
from player_cards import Card, get_shuffled_deck


class Blackjack:
    def __init__(self, deck):
        self.deck = deck
        self.player_hand = []
        self.dealer_hand = []

    @staticmethod
    def get_score(cards: list[Card]):
        vals = [c.value for c in cards]
        if 11 in vals and sum(vals) > 21:
            idx = vals.index(11)
            vals[idx] = 1
        return sum(vals)

    @property
    def player_score(self):
        return self.get_score(self.player_hand)

    @property
    def dealer_score(self):
        return self.get_score(self.dealer_hand)

    @property
    def player_hud(self):
        return (
            f"\nYour cards: {self.player_hand}\n"
            f"Your score: {self.player_score}\n"
            f"Dealers first card was: {self.dealer_hand[0]}\n"
        )

    @property
    def resolved(self):
        return self.dealer_score >= 17

    def deal(self):
        self.dealer_hand = [self.deck.pop() for _ in range(2)]
        print(
            f'The dealer deals card "{self.dealer_hand[0]}" face up, and a card face down.'
        )
        self.player_hand = [self.deck.pop() for _ in range(2)]
        print("You are dealt 2 cards.\n", self.player_hud)
        if self.player_score == 21:
            return ("blackjack", "You scored 21 and won the game!")

    def player_turn(self):
        while True:
            if input("Receive another card [y] or stand [n]?: ") == "y":
                self.player_hand.append(self.deck.pop())
                print("You were dealt another card.")
                if self.is_bust(self.player_hand):
                    return (
                        "you lose",
                        f"You bust with a score of {self.player_score}!",
                    )
                print(self.player_hud)
                if not self.player_score == 21:
                    continue
            print("You chose to stand.")
            if self.resolved:
                print("The dealer's hand is resolved.")
                return self.get_result()
            break

    def is_bust(self, hand):
        if self.get_score(hand) > 21:
            return True

    def dealer_turn(self):
        while True:
            if self.resolved:
                print("The dealer's hand is resolved.")
                break
            self.dealer_hand.append(random.choice(self.deck))
            time.sleep(0.5)
            print("The dealer added a card to their hand.")
            time.sleep(0.5)
            if self.is_bust(self.dealer_hand):
                return (
                    "you win",
                    f"I bust with a score of {self.dealer_score}!",
                )
        return self.get_result()

    def get_result(self):
        if self.player_score == self.dealer_score:
            return (
                "it's a draw",
                f"Our scores were both {self.player_score}!",
            )
        elif self.dealer_score < self.player_score <= 21:
            return (
                "you win",
                f"Your score of {self.player_score} beats my score of {self.dealer_score}!",
            )
        elif self.player_score < self.dealer_score <= 21:
            return (
                "you lose",
                f"I beat your score of {self.player_score} with my score of {self.dealer_score}!",
            )
        else:
            assert False

    def display_result(self, status, reason):
        print(
            f"Dealer hand: {self.dealer_hand}\n"
            f'Dealer: "{reason}\n"'
            f"*** {status.upper()}! ***"
        )

    def play(self):
        result = self.deal()
        if not result:
            result = self.player_turn()
        if not result:
            result = self.dealer_turn()
        self.display_result(*result)


def main():
    while True:
        if input("New Blackjack game? ['y' or 'n']: ") == "y":
            blackjack = Blackjack(get_shuffled_deck())
            blackjack.play()
            print("-------------------\n")
        else:
            break


if __name__ == "__main__":
    main()
