#!/usr/bin/env python

import random
import time
import sys
#class Debuff(self):
#    """Class to handle debuffs"""
#    def status_effect_add(self, effect):
#        self.status.append(effect)
#    def status_effect_remove(self):
#        if len(self.status) > 0:
#            removed = self.status.pop[0]
#        else:
#            removed = False

#slain = {'Peon':0,'Ogre':0,'Troll':0,'Dragon':0}

class Enemy(object):
    """Generic Enemy class"""
    def __init__(self):
        self.isalive = True
        self.ishostile = True
        self.status = []

    def cstat(self):
        if self.hp > 0:
            print 'Enemy hp is ' + str(self.hp)


    def is_attacked(self,dmg,special):
        if dmg <= 0:
            print self.generic + ' evaded your attack'
            return
        if special == False:
            full_dmg = dmg - (self.armor/2)
            if full_dmg <= 0:
                print (str(new_enemy.generic) + "'s armor absorbed your attack")
            else :
                self.hp -= full_dmg
                print('Damaged ' + self.generic + ' for ' +str(full_dmg) + ' damage')
        if special == True:
            self.hp -= dmg
    def heal(self, amount):
        self.hp += amount

class Peon(Enemy):
    """Peon enemy class"""
    def __init__(self):
        Enemy.__init__(self)
        self.generic = 'Peon'
        self.description = 'Orc Peon armed with a shovel'
        self.armor = 10
        self.hp = 30
        self.atk = 2

class Ogre(Enemy):
    """Ogre enemy class"""
    def __init__(self):
        Enemy.__init__(self)
        self.generic = 'Ogre'
        self.description = 'Ogre armed with a polearm'
        self.armor = 20
        self.hp = 40
        self.atk = 4

class Troll(Enemy):
    """Troll enemy class"""
    def __init__(self):
        Enemy.__init__(self)
        self.generic = 'Troll'
        self.description = 'Troll armed with a War-Axe'
        self.armor = 25
        self.hp = 55
        self.atk = 6

class Dragon(Enemy):
    """Dragon boss class"""
    def __init__(self):
        Enemy.__init__(self)
        self.generic = 'Dragon'
        self.description = 'Green Dragon with thick scales'
        self.armor = 50
        self.hp = 150
        self.atk = 12

class Player(object):
    def __init__(self):
        self.defending = False
        self.isalive = True
        self.hp = 100
        self.armor = 20
        self.evasion = 1
        self.inventory = {'Weapons':[],'Artefacts':[],'Scrolls':[]}
        self.weapon = ('Shortsword', 5)
        self.potions = 3
        self.AP = 10
    def cstat(self):
        print 'Player HP is ' + str(self.hp)
        print 'Player has ' + str(self.potions) + ' potions'
        print 'Player AP : ' + str(self.AP)

    def is_attacked(self,dmg,special):
        if self.defending:
            self.evasion += self.evasion
            self.armor += self.armor
        if dmg <= 0:
            print new_enemy.generic + ' swipes and misses you'
            return
        if special == False:
            full_dmg = dmg - ((self.evasion + self.armor)/2)
            if full_dmg <= 0:
                print (str(new_enemy.generic) + ' attack bounces off of your armor')
            else :
                self.hp -= full_dmg
                print (str(new_enemy.generic) + ' hits you for ' + str(full_dmg))
        if special == True:
            full_dmg = dmg - self.evasion
            if full_dmg <= 0:
                print "You dodge the inbound attack at the last moment"
            else:
                self.hp -= full_dmg
                print (str(new_enemy.generic) + ' hits you for ' + str(dmg))
        if self.defending:
            self.evasion -= self.evasion
            self.armor -= self.armor
            self.defending = False
    def heal(self, amount):
        self.hp += amount

def doomselector():
    doomroll = random.randint(0,100)
    if doomroll > 0 and doomroll < 40:
        return 1
    if doomroll > 40 and doomroll < 70:
        return 2
    if doomroll > 70:
        return 3


player1 = Player()
game_is_running = True
gamecount = 1
enemies = {'Peon':Peon,'Ogre':Ogre,'Troll':Troll,'Dragon':Dragon}
first_iter = True
while game_is_running:
    if gamecount % 10 != 0:
        current_enemy = doomselector()
        if current_enemy == 1:
            new_enemy = enemies['Peon']()
        if current_enemy == 2:
            new_enemy = enemies['Ogre']()
        if current_enemy == 3:
            new_enemy = enemies['Troll']()
    if gamecount % 10 == 0:
        new_enemy = enemies['Dragon']()

    if first_iter:
        sys.stdout.write("Welcome, Gladiator.  Prepare to engage in mortal combat, in a fight for your very life!")
        sys.stdout.flush()
        time.sleep(2)
        sys.stdout.write('\n')
        sys.stdout.flush()
        first_iter = False
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write('New enemy, The ' + new_enemy.generic + ' approaches!\n')

    while new_enemy.hp > 0 and player1.hp > 0:
        print (' What action to you take? : (A to Attack, H to heal, S for Special Attack, D to defend for '
                '1 round, Q to quit) Potions left :' + str(player1.potions))
        action = raw_input('--> ')
        if action == 'A':
            attack_num = random.randint(0,15)
            if attack_num > 3:
                new_enemy.is_attacked(attack_num,False)
            else:
                print "You wave your weapon at empty air"

        if action == 'H':
            if player1.potions == 0:
                print "No Potions Remaining"
            if player1.potions > 0:
                heal_num = random.randint(10,25)
                player1.heal(heal_num)
                player1.potions -= 1
                print "Player healed for " + str(heal_num)

        if action == 'S':
            if player1.AP > 9:
                if random.randint(0,4) == 0:
                    print "You launched a special attack but missed!"
                elif random.randint(0,4) != 0:
                    attack_num = random.randint(20,40)
                    if attack_num < 28:
                        print "Your special attack went wide of its mark"
                    elif attack_num >= 28:
                        print "You wind up to deliver a special attack"
                        time.sleep(1)
                        print "You hit the " + new_enemy.generic + " for " + str(attack_num) + " damage"
                        new_enemy.is_attacked(attack_num,True)
            elif player1.AP < 10:
                print "You do not have enough AP to perform a special attack!"
            player1.AP = 0
        if (action == 'Q') or (action == 'q'):
            game_is_running = False
            break
        if action == 'D':
            print "You crouch and assume a defensive stance for 1 round"
            player1.defending = True
        elif action != 'A' and action != 'H' and action != 'S' and action != 'D':
            print "incorrect entry! You leave yourself open to attack!"
            player1.is_attacked(random.randint(5,(new_enemy.atk*6)),False)
        if player1.AP < 10:
            player1.AP += 2


        time.sleep(1)
        enemy_success = random.randint(0,19)
        enemy_attackdmg = random.randint(0,(new_enemy.atk*4))
        if new_enemy.hp > 0:
            if enemy_success == 0:
                print new_enemy.generic + " throws its weight into the attack.  Hit ignores your armor!"
                player1.is_attacked(enemy_attackdmg, True)
                time.sleep(.5)
            if enemy_success > 0:
                #print new_enemy.generic + " hits you for " + str(enemy_attackdmg) + " damage"
                player1.is_attacked(enemy_attackdmg, False)
                time.sleep(.5)
            print "Current status:"
            player1.cstat()
            new_enemy.cstat()
        else :
            print (new_enemy.generic + ' falls down, defeated')
        if player1.hp <= 0:
            print "You fall down, defeated"
            game_is_running = False
            break
print "Thanks for playing"
print '\n'
