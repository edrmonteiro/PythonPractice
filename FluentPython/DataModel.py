"""
coding: utf-8
Created on 02/11/2020

@author: github.com/eduardormonteiro

Lesson From: Fluent Python book

Table 1-1. Special method names (operators excluded).

string/bytes representation __repr__, __str__, __format__, __bytes__
conversion to number __abs__, __bool__, __complex__, __int__, __float__, __hash__, __index__
emulating collections __len__, __getitem__, __setitem__, __delitem__, __contains__, __iteration __iter__, __reversed__, __next__
emulating callables __call__
context management __enter__, __exit__
instance creation and destruction __new__, __init__, __del__
attribute management __getattr__, __getattribute__, __setattr__, __delattr__, __dir__
attribute descriptors __get__, __set__, __delete__
class services __prepare__, __instancecheck__, __subclasscheck__

Table 1-2. Special method names for operators.
unary numeric operators __neg__ -, __pos__ +, __abs__ abs()
rich compartison operators __lt__ >, __le__ <=, __eq__ ==, __ne__ !=, __gt__ >, __ge__ >=
arithmetic operators __add__ +, __sub__ -, __mul__ *, __truediv__ /, __floordiv__ //, __mod__%, __divmod__ divmod() , __pow__ ** or pow(), __round__ round()
reversed arithmetic operators __radd__, __rsub__, __rmul__, __rtruediv__, __rfloordiv__,__rmod__, __rdivmod__, __rpow__
augmented assignment arithmetic operators __iadd__, __isub__, __imul__, __itruediv__, __ifloordiv__, __imod__, __ipow__
bitwise operators __invert__ ~, __lshift__ <<, __rshift__ >>, __and__ &, __or__ |,__xor__ ^
reversed bitwise operators __rlshift__, __rrshift__, __rand__, __rxor__, __ror__
augmented assignment bitwise operators __ilshift__, __irshift__, __iand__, __ixor__, __ior__

"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def getall(self):
        return self._cards


beer_card = Card('7', 'diamonds')
beer_card

deck = FrenchDeck()
len(deck)

deck[0]

deck[-1]


from random import choice
choice(deck)

deck.getall()

deck[:3]

deck[12::13]    # starting on index 12 and skipping 13 cards at a time

for card in deck: # doctest: +ELLIPSIS
    print(card)

for card in reversed(deck): # doctest: +ELLIPSIS
    print(card)
    
Card('Q', 'hearts') in deck
Card('7', 'beasts') in deck

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high): # doctest: +ELLIPSIS
    print(card)




from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)

print(v1 + v2)

v = Vector(3, 4)
print(abs(v))

print(v * 3)
print(abs(v * 3))

stop = True

print(bool(v1))





























