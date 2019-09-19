import deck
import time

    

###### initializing ######
print("Innitializing Game")
print("Lets play a game of 20 Points")
print("I'll be your dealer today.")
print("I'm opening a pack of regular poker cards")
main_deck=deck.populatePokerDeck()
time.sleep(3) # delays for 5 seconds

print("Shuffling them now.")
deck.shuffle(main_deck)
time.sleep(5) # delays for 5 seconds
print("Laying out cards now")
inventory=deck.split(main_deck,10)
negative_pile=[]
positive_pile=[]
hand=[]
print("Hand is empty. 10 cards in inventory. Positive and Negative Piles are empty")
operation = "A"
while operation!= "Q":
    print("l to look at inventory")
    print("t to take card from main deck")
    print("Q to quit")
    operation = input("What action do you want to take?")
    print("You chose " + operation)
    if operation == "l":
        deck.revealAll(inventory)
     

    
    
    
########################
"""
Game continues while there are cards in the main_deck
    
    Player adds cards to hand until hand is won or lost
    If won, add the hand to the positive pile
    else, add the hand to the negative pile.
    
    on the last hand, if there are no more cards in the deck, the player can add cards from inventory 
    only if they can use them to win the hand.

    To win a hand: The number cards in the hand = 10
    To loose a hand: The number cards in the hand are above 10 OR there are more than 10 cards in a hand.

    

            
    At the end of all hands, 
        The sum of the number cards in the inventory are totaled, and that many cards/
        are taken from the positive pile and added to the negative pile.
        The number cards are also added to the negative pile
    
        The sum of the face cards in the inventory are totaled, and that many cards/
        are taken from the negative pile and added to the positive pile.
        The face cards are added to the positive pile.
        
    Player wins if there are more cards in the positive Pile than the Negative Pile
"""






