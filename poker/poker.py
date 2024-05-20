#Poker Hand Ranking challenge. 

import collections
from statistics import mode


global hand
#hand = "10d Jd Qd Ad Kd"	#Royal Flush
#hand = "2s 3s 4s 5s 6s"	#Straight Flush
#hand = "10s 10s 10s 10s Ad"	#Four of a kind
#hand = "10s 10s 10s 9a 9a"	#Full house
#hand = "10s 2s 4s 6s As"	#Flush	
#hand = "2s 3a 4s 5d 6s"	#Straight
#hand = "10s 10s 10s 9a 8d"	#Three of a kind
#hand = "10s 10s 9s 9s 8d"	#Two pair
#hand = "10s 10a 9s 8a 7d"	#Pair
hand = "2a 4s 6d 8h 10s"	#High card


#Scenario variable result
global royalflush_result
global straightflush_result
global fourofakind_result
global fullhouse_result
global flush_result
global straight_result
global threeofakind_result
global twopair_result
global pair_result


global suit_occurrances
global repeated_cards
global sorted_cards
global cards
cards = []
global suits 
suits = []
global card_values
card_values = dict(zip('1 2 3 4 5 6 7 8 9 10 J Q K A'.split(), range(14)))	#Give values to cards in deck to compare to hand.
royalflush = [9, 10, 11, 12, 13]
global in_sequence

def get_hand_data():
    global suit_occurrances
    global repeated_cards
    global sorted_cards	
    global in_sequence
    #For loop to split cards in hand and get its face and suit.
    for card in hand.split():
        #print(card)
        cards_list = []

        #Obtaining the face and suit values by slicing each of the cards.
        #"face" is obtained by cutting away the last character of the string and use the reaiming.
        #"suit" is obtained by using the last character of the string.   
        face, suit = card[:-1], card[-1]
        #print(face)
        #print(suit,"\n") 
        cards.append(face)
        suits.append(suit)
    
    #suit_occurrances = max([suits.count(a) for a in suits])
    
    #Get number of occurances from the suite with the highest distribution.  
    suit_population = mode(suits)					#Get the highest population distribution
    #print(suit_population)						
    suit_occurrances = suits.count(suit_population)			#Count occurrances of the item of highest distribution
    #print(suit_occurrances, "\n")

    repeated_cards = sorted([cards.count(a) for a in set(cards)])
    #print(repeated_cards)
    sorted_cards = sorted([card_values[a] for a in cards])
    #print(sorted_cards)	
    
    #Define if cards are in sequence
    if sorted_cards == [1, 2 , 3, 4, 5] or sorted_cards == [2, 3, 4, 5, 6] or sorted_cards == [3, 4, 5, 6, 7] or sorted_cards == [4, 5, 6, 7, 8] or sorted_cards == [5, 6, 7, 8, 9] or sorted_cards == [6, 7, 8, 9, 10] or sorted_cards == [7, 8, 9, 10, 11] or sorted_cards == [8, 9, 10, 11, 12]:
        #print("is in sequence")
        in_sequence = 1
    else:
        #print("is not in sequence")
        in_sequence = 0
    #print("In sequence: ", in_sequence)


def is_it_royalflush():
    global royalflush_result
    if suit_occurrances == 5 and sorted_cards == royalflush:	#Checking if all suits are the same and sorted cards are equal to a royal flush
        print("\nYou have a Royal Flush")
        royalflush_result = 1	
    else:
        print("\nNo royal flush found")
        royalflush_result = 0

def is_it_straightflush():
    global straightflush_result
    if suit_occurrances== 5 and in_sequence == 1:			#Checking if all suits are the same and cards are in sequence 
        print("\nStraight flush found")
        straightflush_result = 1
    else:
        print("\nNo straight flush found")
        straightflush_result = 0

def is_it_4ofakind():
    global fourofakind_result
    for x in range(len(repeated_cards)):
        #print (repeated_cards[x])
        if repeated_cards[x] == 4:
            print("\nFour or a kind found")
            fourofakind_result = 1
            break
        else:
            #print("\nNot four of a kind")
            fourofakind_result = 0
    if fourofakind_result == 0:
        print("\nNo four of a kind hand found")
def is_it_fullhouse():
    global fullhouse_result
    for x in range(len(repeated_cards)):
        #print(repeated_cards[x])
        if repeated_cards[x] == 3:
            #print("Three of a kind found")
            threeofkind = 1
            break
        else:
            threeofkind = 0
    for x in range(len(repeated_cards)):
        if repeated_cards[x] == 2:
            #print("Pair found")
            pair = 1
            break
        else:
            pair = 0
    #print("\n")
    #print(threeofkind)
    #print(pair)
    if threeofkind == 1 and pair == 1:
        print("\nFull house found")
        fullhouse_result = 1
    else:
        print("\nNo full house found")
        fullhouse_result = 0			

def is_it_flush():
    global flush_result
    global suit_occurrances
    global in_sequence
    if suit_occurrances == 5 and in_sequence == 0:
        print("\nFlush found")
        flush_result = 1
    else:
        print("\nNo flush found")
        flush_result = 0

def is_it_straight():
    global straight_result
    global suit_occurrences
    global in_sequence
    if suit_occurrances <= 4 and in_sequence == 1:
        print("\nStraight hand found")
        straight_result = 1
    else:
        print("\nNo straight hand found")
        straight_result = 0

def is_it_threeofakind():
    global threeofakind_result
    for x in range(len(repeated_cards)):
        #print(repeated_cards[x])
        if repeated_cards[x] == 3:
            #print("Three of a kind found")
            threeofkind = 1
            break
        else:
            threeofkind = 0
    for x in range(len(repeated_cards)):
        if repeated_cards[x] == 2:
            #print("Pair found")
            pair = 1
            break
        else:
            pair = 0
    #print("\n")
    #print(threeofkind)
    #print(pair)
    if threeofkind == 1 and pair == 0:
        print("\nThree of a kind found")
        threeofakind_result = 1
    else:
        print("\nNo three of a kind found")
        threeofakind_result = 0

def is_it_twopair():
    global twopair_result
    #Count pairs, if it is 2 this is true.
    pair = 0
    for x in range(len(repeated_cards)):
        if repeated_cards[x] == 2:
            #print("Two pair found")
            pair += 1
    if pair == 2:
        print("\nTwo pair hand found")
        twopair_result = 1
    else:
        print("\nNo two pair hand found")
        twopair_result = 0

def is_it_pair():
    global pair_result
    #Count pairs if pairs is only 1 this is true
    pair = 0
    for x in range(len(repeated_cards)):
        if repeated_cards[x] == 2:
            #print("Two pair found")
            pair += 1
    if pair == 1:
        print("\nPair hand found")
        pair_result = 1
    else:
        print("\nNo pair hand found")
        pair_result = 0

def is_it_highcard():
    #Create variables to store results of all other functions and it all other functions are false this is true. 
    #print("Royal Flush result: ", royalflush_result)
    #print("Straight Flush result: ", straightflush_result)
    #print("Four of a kind result: ", fourofakind_result)
    #print("Full house result: ", fullhouse_result)
    #print("Flush result: ", flush_result)
    #print("Straight result: ", straight_result)
    #print("Three of a kind result: ", threeofakind_result)
    #print("Two pair result: ", twopair_result)
    #print("Pair result: ", pair_result)
    if 1 in (royalflush_result, straightflush_result, fourofakind_result, fullhouse_result, flush_result, straight_result, threeofakind_result, twopair_result, pair_result):
        print("\nNo high card hand found")
    else:
        print("\nHigh card hand found")
    
#Main
get_hand_data()
is_it_royalflush()
is_it_straightflush()
is_it_4ofakind()
is_it_fullhouse()
is_it_flush()
is_it_straight()
is_it_threeofakind()
is_it_twopair()
is_it_pair()
is_it_highcard()	
