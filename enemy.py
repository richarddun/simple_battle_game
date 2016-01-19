#!/usr/local/bin/python2.7

import random
import time

class Enemy_peon:
    """Class to build enemies and manipulate them """
    def __init__(self):
        self.race = 'Troll with a large War-Axe'
        self.armor = 'Plate'
        self.boots = 'Iron'
        self.helmet = 'Obsidian'
        self.hp = 60
        self.critical = False
    def attack(self,x):
        if x == 0:
            print 'You swung and missed!'
        if x > 0:
            if self.hp > 0:
                self.hp -= x
                print 'Your strike hits the Troll for ' + str(x) + ' damage'
            if self.hp < 15 and self.critical == False and random.randint(0,2) == 2:
                print 'The Troll uses a restorative potion and grins menacingly'
                self.hp += 20
                print 'Troll HP is ' + str(self.hp)
                self.critical = True
    def get_hp(self):
        if self.hp > 0:
            print 'Troll HP is ' + str(self.hp)
        if self.hp < 0 :
            print 'Troll has 0 HP'

class Player:
    """Class to represent the players variables"""
    def __init__(self):
        self.hp = 100
        self.potions = 2
        self.crit = False
        self.serious = False
        self.dangerous = False
    def attack(self,x):
        if x > 0:
            print 'Troll hits you for ' + str(x)+ ' damage'
            self.hp -= x
        elif x == 0:
            print 'You expertly dodge the Trolls heavy swing'
        if self.hp <= 40 and self.crit == False:
            print 'You are seriously Injured!'
            self.crit = True
        if self.hp <= 20 and self.serious == False:
            print 'You are critically Injured!'
            self.serious = True
        if self.hp <= 10 and self.dangerous == False and self.hp > 0:
           print 'You are near Death... consider using a healing potion'
           self.dangerous = True
    def heal(self,x):
        if self.potions > 0:
            print 'Healed for ' + str(x)
            self.hp += x
            self.potions -= 1
        else:
            print 'No healing potions left!'
    def status(self):
        if self.hp > 0:
            print 'Player HP is ' + str(self.hp)
        elif self.hp <= 0:
            print 'Player HP is 0'

enemy1 = Enemy_peon()
player1 = Player()

print 'A ' + enemy1.race + ' enters the arena'
print "Its armor is " + enemy1.armor
print "Its boots are " + enemy1.boots
print 'Its helmet is ' + enemy1.helmet

while enemy1.hp > 0 and player1.hp > 0:
    print 'What action to you take? : (A to Attack, H to heal) Potions left :' + str(player1.potions)
    action = raw_input('--> ')
    if action == 'A':
        enemy1.attack(random.randint(0,10))
    if action == 'H':
        player1.heal(random.randint(10,25))
    elif action != 'A' and action != 'H':
        print "incorrect entry! You leave yourself open to attack!"
        player1.attack(random.randint(0,40))
    time.sleep(1)
    player1.attack(random.randint(0,30))
    time.sleep(1)
    print "Current status:"
    player1.status()
    enemy1.get_hp()

if enemy1.hp <= 0 and player1.hp <= 0:
    print "War... war never changes...\nGame Over\n"
elif enemy1.hp <= 0:
    print "You are victorious!\nGame Over\n"
elif player1.hp <= 0:
    print "You have been vanquished\nGame Over\n"

