# implementation of card game - Memory

import simplegui
from random import shuffle

# global variable
n = 16
cards = [i for i in range(8)] * 2  # boolean, not string
exposed = [False for i in range(16)]
state = 0
counter = 0
exposed = [False for i in range(16)]
line_width = 800 / n
counter_skip = 0


# helper function to initialize globals
def new_game():
    global counter, cards, exposed, n, skip_counter
    shuffle(cards)
    exposed = [False for i in range(16)]
    counter = 0
    state = 0
    # print cards, exposed
    label.set_text("Turns = " + str(counter))
    counter_skip = 1


# define event handlers
def mouseclick(pos):
    # print("mouse clicked")
    mouse_pos = (pos[0], pos[1])
    global line_width, card_clicked, state, last_cardA, last_cardB, counter, counter_skip

    # mouse_pos[0] / line_width
    # print int(mouse_pos[0] / line_width)
    card_clicked = int(mouse_pos[0] / line_width)
    # print("card clicked", card_clicked)

    # ignore click if cards already face up
    if exposed[card_clicked] is True:
        return
    # print ("inside mouseclick " + str(counter))

    ###State 0 corresponds to the start of the game.
    ###In state 0, if you click on a card, that card is exposed, and you switch to state 1.

    ###State 1 corresponds to a single exposed unpaired card.
    ###In state 1, if you click on an unexposed card, that card is exposed and you switch to state 2.

    ###State 2 corresponds to the end of a turn.
    ###In state 2, if you click on an unexposed card, that card is exposed and you switch to state 1.

    # beginning / pick first card
    if state == 0:
        state = 1
        # print ("in state 0")
        last_cardA = card_clicked

        exposed[card_clicked] = True

        # update label
        counter += 1
        update_label = "Turns = " + str(counter)
        label.set_text(update_label)

        # print("in first card, set first card")

    # pick second card
    elif state == 1:
        state = 2
        # print ("in state 1")
        last_cardB = card_clicked
        exposed[card_clicked] = True


    elif state == 2:
        state = 1
        # print ("in state 2")

        # update label, skip first time in state 1
        counter += 1
        update_label = "Turns = " + str(counter)
        label.set_text(update_label)

        # ignore same card clicked, if not same, flip both
        # print ("in state 2, not same face")
        if cards[last_cardA] != cards[last_cardB]:
            exposed[last_cardA] = False

            exposed[last_cardB] = False
            # print (cards[last_cardA], cards[last_cardB])

        last_cardA = card_clicked

        exposed[card_clicked] = True
        # print cards[card_clicked]


# cards are logically 50x100 pixels in size
def draw(canvas):
    global cards, card_clicked, line_width, n

    # helper function
    def draw_card(n):
        canvas.draw_line((line_width * n, 0), (line_width * n, 100), 1, 'Black')

        if exposed[n] is False:
            canvas.draw_line((line_width * (n + 0.5), 0), (line_width * (n + 0.5), 100), line_width, 'Red')

        else:
            canvas.draw_line((line_width * (n + 0.5), 0), (line_width * (n + 0.5), 100), line_width, 'Green')
            canvas.draw_text(str(cards[n]), (line_width * (n + 0.5) - 10, 60), 30, "Black")

    # draw / redraw all cards
    for i in range(16):
        draw_card(i)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(counter))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
# print cards
# print len(exposed)=16


frame.start()

http: // www.codeskulptor.org /  # user47_1jaHEWTb4x_1.py (mine)
# http://www.codeskulptor.org/#user42_3sGOUh1Cll_2.py (reference)