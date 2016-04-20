# -*- coding: utf-8 -*-
'''
methods for a card game. A deck is any stack of cards. 
'''
import random

def create(decksize):
    '''Loads array with numbers from 1 to decksize'''
    # this is for simple tests for decks filled with "blank" cards
    aDeck=[]
    for x in range(decksize):
        aDeck.append(x+1)
    return aDeck
    
def shuffle(aDeck):
    ''' Uses the Fisher-Yates Shuffle'''
    
    '''
    Fisher-Yates Shuffle
    -- To shuffle an array a of n elements (indices 0..n-1):
    for i from n−1 downto 1 do
     j ← random integer such that 0 ≤ j ≤ i
     exchange a[j] and a[i]
     
     -- To shuffle an array a of n elements (indices 0..n-1):
    for i from 0 to n−2 do
     j ← random integer such that 0 ≤ j < n-i
     exchange a[i] and a[i+j]
'''
    n=len(aDeck)
    for i in range(n):
        j =random.randrange(0,n-i)
        temp=aDeck[i]
        aDeck[i]=aDeck[i+j]
        aDeck[j+i]=temp
    return None

def split(aDeck,location): 
    """Splits deck at 'location'. Returns the new deck"""
    newDeck=[]
    for x in range(location):
        newDeck.append(aDeck.pop())
    return (newDeck)
    
def combine(bottomDeck, topDeck):
    '''Adds the top deck to the bottom deck. Bottom deck is emptied'''
    for x in range(len(topDeck)):
        bottomDeck.append(topDeck.pop())
    return(None)

def countCards(aDeck):
    return len(aDeck)

def moveCard(card_Origen,card_destination):
    card_destination.append(card_Origen.pop())
    return(None)
    
def sumDeck(aDeck,cardType):
    """ Card type is either "Face" or "Number". """
    points =0
    
    for x in range(len(aDeck)):
        card=aDeck[x]
        if (card["Type"]==cardType):
            points+= card["Value"]
    return points

def revealAll(aDeck):
    """Returns a string of card names. Reveals all cards in deck. """
    cardNames=''
    for x in range(len(aDeck)):
        card= aDeck[x]
        if (card["Name"] == "Joker"):
            cardNames += card["Suite"] + " " + card["Name"]
        else:
            cardNames += card["Name"] + " of " +card["Suite"]
        cardNames += "\n" 
    return (cardNames)
    
def revealCard(card):
    """Returns a string. """
    cardName=''
    if (card["Name"] == "Joker"):
        cardName += card["Suite"] + " " + card["Name"]
    else:
        cardName += card["Name"] + " of " +card["Suite"] 
    return (cardName)
    
def populatePokerDeck():
    """ creates a array (deck) of pokercards in the form of dictionaries."""
    #At some point, I may want this function, or a function like it, to read from a txt/json or dat file, 
    #but for now this suffices.
    aDeck =	[
                {
                    "Suite": "Hearts",
                    "Name": "Ace",
                    "Type": "Face",
                    "Value": 1
                },
                {
                    "Suite": "Hearts",
                    "Name": "Two",
                    "Type": "Number",
                    "Value": 2
                },
                {
                    "Suite": "Hearts",
                    "Name": "Three",
                    "Type": "Number",
                    "Value": 3
                },
                {
                    "Suite": "Hearts",
                    "Name": "Four",
                    "Type": "Number",
                    "Value": 4
                },
                {
                    "Suite": "Hearts",
                    "Name": "Five",
                    "Type": "Number",
                    "Value": 5
                },
                {
                    "Suite": "Hearts",
                    "Name": "Six",
                    "Type": "Number",
                    "Value": 6
                },
                {
                    "Suite": "Hearts",
                    "Name": "Seven",
                    "Type": "Number",
                    "Value": 7
                },
                {
                    "Suite": "Hearts",
                    "Name": "Eight",
                    "Type": "Number",
                    "Value": 8
                },
                {
                    "Suite": "Hearts",
                    "Name": "Nine",
                    "Type": "Number",
                    "Value": 9
                },
                {
                    "Suite": "Hearts",
                    "Name": "Ten",
                    "Type": "Number",
                    "Value": 10
                },
                {
                    "Suite": "Hearts",
                    "Name": "Jack",
                    "Type": "Face",
                    "Value": 2
                },
                {
                    "Suite": "Hearts",
                    "Name": "Queen",
                    "Type": "Face",
                    "Value": 3
                },
                {
                    "Suite": "Hearts",
                    "Name": "King",
                    "Type": "Face",
                    "Value": 4
                },
                {
                    "Suite": "Clubs",
                    "Name": "Ace",
                    "Type": "Face",
                    "Value": 1
                },
                {
                    "Suite": "Clubs",
                    "Name": "Two",
                    "Type": "Number",
                    "Value": 2
                },
                {
                    "Suite": "Clubs",
                    "Name": "Three",
                    "Type": "Number",
                    "Value": 3
                },
                {
                    "Suite": "Clubs",
                    "Name": "Four",
                    "Type": "Number",
                    "Value": 4
                },
                {
                    "Suite": "Clubs",
                    "Name": "Five",
                    "Type": "Number",
                    "Value": 5
                },
                {
                    "Suite": "Clubs",
                    "Name": "Six",
                    "Type": "Number",
                    "Value": 6
                },
                {
                    "Suite": "Clubs",
                    "Name": "Seven",
                    "Type": "Number",
                    "Value": 7
                },
                {
                    "Suite": "Clubs",
                    "Name": "Eight",
                    "Type": "Number",
                    "Value": 8
                },
                {
                    "Suite": "Clubs",
                    "Name": "Nine",
                    "Type": "Number",
                    "Value": 9
                },
                {
                    "Suite": "Clubs",
                    "Name": "Ten",
                    "Type": "Number",
                    "Value": 10
                },
                {
                    "Suite": "Clubs",
                    "Name": "Jack",
                    "Type": "Face",
                    "Value": 2
                },
                {
                    "Suite": "Clubs",
                    "Name": "Queen",
                    "Type": "Face",
                    "Value": 3
                },
                {
                    "Suite": "Clubs",
                    "Name": "King",
                    "Type": "Face",
                    "Value": 4
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Ace",
                    "Type": "Face",
                    "Value": 1
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Two",
                    "Type": "Number",
                    "Value": 2
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Three",
                    "Type": "Number",
                    "Value": 3
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Four",
                    "Type": "Number",
                    "Value": 4
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Five",
                    "Type": "Number",
                    "Value": 5
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Six",
                    "Type": "Number",
                    "Value": 6
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Seven",
                    "Type": "Number",
                    "Value": 7
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Eight",
                    "Type": "Number",
                    "Value": 8
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Nine",
                    "Type": "Number",
                    "Value": 9
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Ten",
                    "Type": "Number",
                    "Value": 10
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Jack",
                    "Type": "Face",
                    "Value": 2
                },
                {
                    "Suite": "Diamonds",
                    "Name": "Queen",
                    "Type": "Face",
                    "Value": 3
                },
                {
                    "Suite": "Diamonds",
                    "Name": "King",
                    "Type": "Face",
                    "Value": 4
                },
                {
                    "Suite": "Spades",
                    "Name": "Ace",
                    "Type": "Face",
                    "Value": 1
                },
                {
                    "Suite": "Spades",
                    "Name": "Two",
                    "Type": "Number",
                    "Value": 2
                },
                {
                    "Suite": "Spades",
                    "Name": "Three",
                    "Type": "Number",
                    "Value": 3
                },
                {
                    "Suite": "Spades",
                    "Name": "Four",
                    "Type": "Number",
                    "Value": 4
                },
                {
                    "Suite": "Spades",
                    "Name": "Five",
                    "Type": "Number",
                    "Value": 5
                },
                {
                    "Suite": "Spades",
                    "Name": "Six",
                    "Type": "Number",
                    "Value": 6
                },
                {
                    "Suite": "Spades",
                    "Name": "Seven",
                    "Type": "Number",
                    "Value": 7
                },
                {
                    "Suite": "Spades",
                    "Name": "Eight",
                    "Type": "Number",
                    "Value": 8
                },
                {
                    "Suite": "Spades",
                    "Name": "Nine",
                    "Type": "Number",
                    "Value": 9
                },
                {
                    "Suite": "Spades",
                    "Name": "Ten",
                    "Type": "Number",
                    "Value": 10
                },
                {
                    "Suite": "Spades",
                    "Name": "Jack",
                    "Type": "Face",
                    "Value": 2
                },
                {
                    "Suite": "Spades",
                    "Name": "Queen",
                    "Type": "Face",
                    "Value": 3
                },
                {
                    "Suite": "Spades",
                    "Name": "King",
                    "Type": "Face",
                    "Value": 4
                },
                {
                    "Suite": "Red",
                    "Name": "Joker",
                    "Type": "Face",
                    "Value": None
                },
                {
                    "Suite": "Black",
                    "Name": "Joker",
                    "Type": "Face",
                    "Value": None
                }]
                
    return aDeck