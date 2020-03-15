# Mini-project #6 - Blackjack
# To Hung Sze - Jan, 2020

# The game logic for oversimplified version of Blackjack is as follows.
# The player and the dealer are each dealt two cards initially with one of the dealer's cards
# being dealt faced down (his hole card).
# The player may then ask for the dealer to repeatedly "hit" his hand by dealing him another card.
# If, at any point, the value of the player's hand exceeds 21,
# the player is "busted" and loses immediately.
# At any point prior to busting, the player may "stand" and the dealer will then hit his hand
# until the value of his hand is 17 or more.
# (For the dealer, aces count as 11 unless it causes the dealer's hand to bust).
# If the dealer busts, the player wins. Otherwise, the player and dealer then
# compare the values of their hands and the hand with the higher value wins.
# The dealer wins ties in our version

# Global variables


import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False  # False until player presses Hit
outcome = ""  # String indicating the status / result of game
msg = "Start"  # msg to be displayed to ask user to hit or stand
score = 0  # to keep track of player's total point
hide_dealer = True  # to hide dealer's first card until it is dealer's turn

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
# represent each card
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print
            "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
# each hand contains 2 cards initially
# add one every time player press Hit button
# dealer gets card automatically until busted or 17
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        info = "Hand contains "
        for card in self.cards:
            info += str(card.get_suit()) + str(card.get_rank()) + " "
        return info

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        has_ace = False

        # add up a face value for all cards
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_ace = True

        if not has_ace:
            return value
        else:
            if value + 10 <= 21:
                return value + 10
            else:
                return value

    # draw each card in hand one by one with 20 as offset between cards
    def draw(self, canvas, pos):
        i = 0
        for i in range(len(self.cards)):
            card = self.cards[i - 0]
            card.draw(canvas, [pos[0] + i * (CARD_SIZE[0] + 20), pos[1]])


# define deck class
#
class Deck:
    global SUIT, RANKS

    # new deck created when game starts or player presses Hit button
    def __init__(self):
        self.deck = []
        # self.deck += "a"
        # print self.deck
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

        # return self.deck

    # shuffle the deck each time a new deck is created
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)  # deal first card in deck

    def __str__(self):
        info = "Deck contains"
        holder_list = []
        for x, y in enumerate(self.deck):
            info += " " + str(y)
        return info


# define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer_hand, player_hand, msg, hide_dealer
    hide_dealer = False
    deck = Deck()

    deck.shuffle()

    dealer_hand = Hand()
    player_hand = Hand()

    # deal two cards each at beginning of hand
    for i in range(2):
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())

    in_play = True
    msg = "Hit or Stand?"
    outcome = ""


def hit():
    global in_play, outcome, dealer_hand, player_hand, score, msg

    # if hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())

        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            score -= 1  # player scores
            outcome = "You went bust and lose."
            in_play = False
            # print outcome
            msg = "New deal?"

        else:
            msg = "You have " + str(player_hand.get_value()) + ". Hit or Stand?"
    # not in_play, tell user to start new hand
    else:
        msg = "Please start new hand"
        # msg = ""


def stand():
    global outcome, in_play, dealer_hand, player_hand, score, msg

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(deck.deal_card())

        # assign a message to outcome, update in_play and score
        # determine who wins
        if 22 > dealer_hand.get_value() >= player_hand.get_value():
            outcome = "You lose."
            score -= 1  # dealer wins
            in_play = False
            msg = "New deal?"
        else:
            outcome = "You win!"
            score += 1  # player wins
            in_play = False
            msg = "New deal?"

    # hand is over
    else:
        msg = "Please start new hand."


# draw handler
def draw(canvas):
    global hide_dealer, CARD_SIZE, card_back

    # draw dealer card
    dealer_hand.draw(canvas, [80, 180])

    if in_play:  # hide dealer's first card
        # draw the hide image
        back_width = card_back.get_width()  # 144
        back_height = card_back.get_height()  # 196
        # print back_width, back_height

        canvas.draw_image(card_back, (back_width * 3 / 4, back_height / 2), (back_width / 2, back_height),
                          (80 + CARD_SIZE[0] / 2, 180 + CARD_SIZE[1] / 2), (back_width / 2, back_height))

    player_hand.draw(canvas, [80, 430])

    # draw text outcome
    # draw standard text
    # draw headline
    canvas.draw_text("Blackjack", (150, 100), 30, "Aqua")
    canvas.draw_text("Score: " + str(score), (400, 100), 25, "Black")

    # draw starting line
    canvas.draw_text("Dealer", (80, 150), 25, "Black")
    canvas.draw_text("Player", (80, 400), 25, "Black")

    # draw msgs
    canvas.draw_text(outcome, (200, 150), 25, "Black")
    canvas.draw_text(msg, (200, 400), 25, "Black")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()

frame.start()

http: // www.codeskulptor.org /  # user47_F07Sm08XkI_48.py
# remember to review the gradic rubric
# def __str__(self):
# return str([str(card) for card in self.deck_lst])