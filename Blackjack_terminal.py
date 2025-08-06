'''
Authors Github: JPab-Dev
version: 1.2
'''

#Blackjack program
import random
from time import sleep

#This function creates all the cards of the deck -----------------------------------------------------------------
def create_deck(deck = []):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'spades', 'hearts', 'diamonds']

    for s in suits:
        for v in values:
            deck.append(f'{v} of {s}')

    return deck

#This function returns the value of the whole hand of the player --------------------------------------------------
def get_hand_value(hand):
    score = 0
    Aces = 0
    for card in hand:
        if card[0] == '2':
            score += 2
        elif card[0] == '3':
            score += 3
        elif card[0] == '4':
            score += 4
        elif card[0] == '5':
            score += 5
        elif card[0] == '6':
            score += 6
        elif card[0] == '7':
            score += 7
        elif card[0] == '8':
            score += 8
        elif card[0] == '9':
            score += 9
        elif card[0] == '1' or card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
            score += 10
        elif card[0] == 'A' and Aces == 0:
            Aces += 1
            score += 11
            if score > 21:
                score -= 10
        elif card[0] == 'A' and Aces > 0:
            score += 1

    return score

#This function acts like the croupier when playing its turn -------------------------------------------------------
def croupier_turn(croupier, deck):

    while (get_hand_value(croupier) <= 16):
        sleep(3)
        croupier.append(deck.pop())
        print('---------------------------------------------------\n')
        print(f'croupier hits, he recieve a [{croupier[-1]}]\n')
        print('---------------------------------------------------')

        if get_hand_value(croupier) > 21:
            sleep(2)
            print(f'\nyou win, croupier was over 21 :D, croupier hand value: {get_hand_value(croupier)}')
            return croupier, deck
        
    sleep(3)
    if len(croupier) == 2:
        print('\n---------------------------------------------------\n')
    print(f'croupier stands, total croupier hand value: {get_hand_value(croupier)}\n') 
    
    return croupier, deck

#This function compare both hands and give a winner ---------------------------------------------------------------
def compare_player_croupier(player, croupier):
    
    if get_hand_value(player) == get_hand_value(croupier):
        print('Its a tie :l\n')

    elif get_hand_value(player) > get_hand_value(croupier):
        print(f'YOU WIN :D, by a diference of {(get_hand_value(player) - get_hand_value(croupier))}\n')

    elif get_hand_value(player) < get_hand_value(croupier):
        print(f'you lost :C, by a diference of {(get_hand_value(croupier) - get_hand_value(player))}\n')

    return player, croupier

#This function shows both hands, the player and the croupier hand -------------------------------------------------
def show_hands(player, croupier, reveal_croupier = False):

    if croupier != []:
        print('Croupier hand: ', end="")
        for c in croupier:
            if c != croupier[-1]:
                print(f'[{c}]', end="")
                print(", ", end="")

            else:
                if (not reveal_croupier):
                    print('[________]')
                else:
                    print(f'[{c}]')
                
        print(f'Croupier hand value: ', end="")

        if (not reveal_croupier):
            print(f'{get_hand_value(croupier[0])} + ? \n')
        else:
            print(f'{get_hand_value(croupier)} \n')
    
    if player != []:
        print(f'\nYour hand: ', end="")
        for p in player:
            print(f'[{p}]', end="")
            if p != player[-1]:
                print(", ", end="")

        print(f'\nvalue in your hand: {get_hand_value(player)}')

#Here starts main: -<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<

continue_game = True
round = 1

while continue_game:
    print('-------------------- BLACKJACK --------------------\n')

    player = []
    croupier = []

    if round == 1 or len(deck) < 16:

        print('---------------------------------------------------')
        if round == 1:
            print('Croupier shuffles the deck')
        else:
            print('Croupier shuffles the deck again')
        print('---------------------------------------------------\n')

        deck = []
        create_deck(deck)
        random.shuffle(deck)

    for i in range (2):
        player.append(deck.pop())
        croupier.append(deck.pop())

    show_hands(player, croupier)

    print('\n---------------------------------------------------')

    if get_hand_value(player) == 21:
        print('\nYou have a blackjack, you win :D')

    elif get_hand_value(croupier) == 21:
        print('\nBlackjack for the croupier, croupier wins >:c')
        show_hands([], croupier, True)

    else:

        stand = False
        while (not stand) and get_hand_value(player) <= 21:

            hit_or_stand = str(input('\nHit or Stand? '))

            if hit_or_stand[0] == 'H' or hit_or_stand[0] == 'h':
                player.append(deck.pop())

                print('\n---------------------------------------------------')
                print(f'you have added a [{player[-1]}] to your hand\n')
                sleep(2)
                show_hands(player, [])
                print('\n---------------------------------------------------')

            else:
                stand = True
                print('\n---------------------------------------------------\n')
        
        if get_hand_value(player) <= 21:
            print('Its the croupier turn', end="")
            for i in ['.', '.', '.']:
                sleep(1)
                print(i, end="")
            print('\n')

            show_hands([], croupier, True)

            croupier_turn(croupier, deck)

            if get_hand_value(croupier) <= 21:
                print('---------------------------------------------------\n')
                sleep(4)
                show_hands(player, croupier, True)
                print('\n---------------------------------------------------\n')

                compare_player_croupier(player, croupier)

        else:
            sleep(1)
            print(f'\nyou lost, you were over 21 :C, your hand value: {get_hand_value(player)}\n')

    print('---------------------------------------------------')
    ask_for_stop = str(input('\nPlay again? '))

    if ask_for_stop[0] == 'Y' or ask_for_stop[0] == 'y':
        round += 1
        print('\n---------------------------------------------------')
        print(f'Round {round}                           cards in deck: {len(deck)}\n')

    else:
        continue_game = False
