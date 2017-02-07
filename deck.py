# deck.py
# Defines a class to represent a deck of playing cards
# Author Erica Austin

import random

class DeckOfCards:

	SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
	
	RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
	
	NUMBER_OF_CARDS = len(SUITS) * len(RANKS)
	
	PLAYING_CARDS = [None]*NUMBER_OF_CARDS
	
	#deck = [] #move the variable deck into the contructor to be cleaner and more consistent
	
	def __init__( self ) :
		for i in range( len(self.RANKS) ) : #initialize the playing cards
			for j in range( len(self.SUITS)) :
		    		self.PLAYING_CARDS[(len(self.SUITS)*i) + j] = Card(self.RANKS[i], self.SUITS[j])
		    			
		self.deck = [] 
		self.deck.extend(self.PLAYING_CARDS)
		   
	def dealOneCard(self): #used to deal one card from the top of the deck
		if( len(self.deck) > 0):
			return self.deck.pop(0)

	def newDeck(self): #used to create a brand new playing deck - useful if we've dealt all the cards and want a new deck
		del self.deck[:]
		self.deck.extend(self.PLAYING_CARDS)
		
	def shuffle(self): #used to shuffle the deck
		numberOfCards = len(self.deck) - 1
		for i in range( numberOfCards ) :
			j = i + random.randint(0, numberOfCards-i)
			randomCard = self.deck[j];
			self.deck[j] = self.deck[i]
			self.deck[i] = randomCard
			
	def cardsLeftInDeck(self): #used to return the number of cards in the deck
		return len(self.deck)
									
			
# card.py 
# Defines a class to represent a card from a deck of playing cards
# Author Erica Austin

class Card:

	def __init__( self, rank, suit ):
		self.rank = rank
		self.suit = suit
	
	def getRank(self):
		return self.rank
		
	def getSuit(self):
		return self.suit
		
	def toString(self): #Rank and suit together as a string i.e Ace of Spades
		return self.rank + str(" of ") + self.suit

			
				
			

	
		





