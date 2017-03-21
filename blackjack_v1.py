#! python3

#blackjack_v1.py - Is version 1 of a basic Blackjack game in python.

#Features to be added in future versions: split, surrender, insurance, betting system,
# GUI, decks (ie 1 deck, 2 delks, 3 deck delt, etc.)

import random, sys, time

cards = ['A',
         '2',
         '3',
         '4',
         '5',
         '6',
         '7',
         '8',
         '9',
         '10',
         'J',
         'Q',
         'K']

# list for score (twenty_one) and the player/dealer's hand		 
twenty_one = []
hand = []

twenty_one_dealer = []
dealers_hand =  []

def random_card():
    return cards[random.randint(0, 12)]

def play(card, list):
    if  card == 'A':
        return list.append(11)
    if card == '2':
        return list.append(2)
    if card == '3':
        return list.append(3)
    if card == '4':
        return list.append(4)
    if card == '5':
        return list.append(5)
    if card == '6':
        return list.append(6)
    if card == '7':
        return list.append(7)
    if card == '8':
        return list.append(8)
    if card == '9':
        return list.append(9)
    if card == '10':
        return list.append(10)
    if card == 'J':
        return list.append(10)
    if card == 'Q':
        return list.append(10)
    if card == 'K':
        return list.append(10)

# controls the speed of the text (OOP only here because I just learned about it)
class Text_Speed:
    def __init__(self):
        pass
    def sleep(self):
        time.sleep(.125)

text_speed = Text_Speed()
        
# DEALER
# generates two random cards, adds it to dealer's hand, and finds their score using play()
print('Dealer\'s hand:')

dealer_draw = random_card()
dealers_hand.append(dealer_draw)
text_speed.sleep()
print(dealer_draw)

play(dealer_draw, twenty_one_dealer)

d_draw_2 = random_card()
dealers_hand.append(d_draw_2)
text_speed.sleep()
print('?')
play(d_draw_2, twenty_one_dealer)

text_speed.sleep()
print('-' * 50)

# PLAYER
print('Your hand:') 

draw = random_card()
hand.append(draw)
text_speed.sleep()
print(draw)

play(draw, twenty_one)

draw_2 = random_card()
hand.append(draw_2)
text_speed.sleep()
print(draw_2)
play(draw_2, twenty_one)
print('')
print('Your score:')

if draw == 'A' and draw_2 == 'A': # if the player draws two aces.
    twenty_one[1] = 1
	
print(sum(twenty_one))

 # changes the value if either first two draw are an ace or if both are aces, 
 # so player/dealer does not bust             
def ace(card_1, card_2, score):
    if card_1 == 'A' and card_2 == 'A' and sum(score) > 21:
        score[0] = 1
        print(score)
    if card_1 == 'A' and not card_2 == 'A' and sum(score) > 21:
        score[0] = 1
        print(score)
    if not card_1 == 'A' and card_2 == 'A' and sum(score) > 21:
        score[1] = 1
        print(score)

# adjust for scoring of 'A' (ace) by changing the value in twenty_one(_dealer) to 1
def ace_adjustment(hand, score):
     if sum(score) > 21:
            for i in range(len(hand)):
                if hand[i] == 'A':
                    score[i] = 1
                if sum(score) <= 21:
                    break

# text for player's hand					
def print_hand(current_hand, score):
    print('-' * 50)
    text_speed.sleep()
    print('Your hand:')
    for x in current_hand:
        print(x)
        text_speed.sleep()
    print('')
    text_speed.sleep()
    print('Your score:')
    text_speed.sleep()
    print(sum(score))
    text_speed.sleep()
    print('-' * 50)

# text for dealers hand
def print_dealers_hand():
    print('Dealer\'s hand:')
    for i in range(0, len(dealers_hand)):
        text_speed.sleep()
        print(dealers_hand[i])
        text_speed.sleep()

# function deals with if player or dealer has blackjack on first two draws 
def first_play_blackjack():
    if  not sum(twenty_one) == 21 and sum(twenty_one_dealer) == 21:
        text_speed.sleep()
        print('Dealer\'s hand:')
        text_speed.sleep()
        print(dealer_draw)
        text_speed.sleep()
        print(d_draw_2, '\n')
        text_speed.sleep()
        print('Dealer has Blackjack', '\n')
        text_speed.sleep()
        print('Player loses')
        sys.exit()
    if sum(twenty_one) == 21 and sum(twenty_one_dealer) != 21:
        text_speed.sleep()
        print('Blackjack!', '\n')
        text_speed.sleep()
        print('You WIN!')
        sys.exit()
    if sum(twenty_one) == 21 and sum(twenty_one_dealer) == 21:
        print_dealers_hand()
        print('Dealer\'s Total: ' + str(sum(twenty_one_dealer)), '\n')
        text_speed.sleep()
        print('Push')
        sys.exit()

# if players score is over 21, they bust
def bust():
    if sum(twenty_one) > 21:
        print('Bust')
        sys.exit()

# dealer starts play when player stands		
def move_dealer_stand():
    if sum(twenty_one_dealer) > 16 and sum(twenty_one_dealer) <= 21:
        if sum(twenty_one) > sum(twenty_one_dealer): 
            print('Dealer\'s Final Total: ' + str(sum(twenty_one_dealer)), '\n')
            text_speed.sleep()
            print('Player Wins!')
            sys.exit()
        elif sum(twenty_one) < sum(twenty_one_dealer):
            print('Dealer\'s Final Total: ' + str(sum(twenty_one_dealer)), '\n')
            text_speed.sleep()
            print('Dealer Wins!')
            sys.exit()
        else:
            print('Dealer\'s Final Total: ' + str(sum(twenty_one_dealer)), '\n')
            text_speed.sleep()
            print('Push')
            sys.exit()
    elif sum(twenty_one_dealer) <= 16:
        print_dealers_hand()
        draw_3_to_21 = random_card()   
        dealers_hand.append(draw_3_to_21)
        print(draw_3_to_21)
        play(draw_3_to_21, twenty_one_dealer)
        ace(dealer_draw, d_draw_2, twenty_one_dealer)
        ace_adjustment(dealers_hand, twenty_one_dealer)
        print('Dealer\'s Total: ' + str(sum(twenty_one_dealer)))
        text_speed.sleep()
        print('-' * 50)
        text_speed.sleep()
        move_dealer_stand() # loops
    else:
        print('Dealer\'s Final Total: ' + str(sum(twenty_one_dealer)), '\n')
        text_speed.sleep()
        print('Dealer bust', '\n')
        text_speed.sleep()
        print('Player Wins!')
        sys.exit()

def next_moves():
    for x in range(4, 22):       
        print('Hit or stand?')
        move = input()
        if move.lower() == 'hit':
          draw_4_to_21 = random_card()
          hand.append(draw_4_to_21)
          play(draw_4_to_21, twenty_one)
          ace(draw, draw_2, twenty_one)
          ace_adjustment(hand, twenty_one)
          print_hand(hand, twenty_one)
          bust()
        elif move.lower() == 'stand':
           print('-' * 50)
           print_dealers_hand()
           print('Dealer\'s Total: ' + str(sum(twenty_one_dealer)))
           print('-' * 50)
           move_dealer_stand() 
        else:
            print('Please retype your answer: ', '\n')
            next_moves()

# input for first move by player. Hit goes to next_move() and stay goes to move_dealer_stand()			
def first_move():
    first_play_blackjack()
    text_speed.sleep()
    print('Hit or stand?')
    next_play = input()
    if dealer_draw == 'A' and d_draw_2 == 'A': # if the dealer draws two aces in first two draws
        twenty_one_dealer[1] = 1
    if next_play.lower() == 'hit':
        draw_3 = random_card()
        hand.append(draw_3)
        play(draw_3, twenty_one)
        ace(draw, draw_2, twenty_one)
        ace_adjustment(hand, twenty_one)
        print_hand(hand, twenty_one)
        bust()
        next_moves()
    elif next_play.lower() == 'stand':
        print('-' * 50)
        print_dealers_hand()
        text_speed.sleep()
        print('Dealer\'s Total: ' + str(sum(twenty_one_dealer)))
        text_speed.sleep()
        print('-' * 50)
        text_speed.sleep()
        move_dealer_stand()
    else:
        print('Please retype your answer: ', '\n') 
        first_move()

text_speed.sleep()
print('-' * 50)
first_move()

