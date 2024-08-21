# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:32:35 2024

@author: joshm
"""
class Unit:
    
    unit_class = None
    maxHealth = 10
    movement = 1
    attack = 2
    defence = 2
    cost = 2
    atk_range = 1
    retaliate = True
    skills = ['Dash', 'Fortify']
    multiplier = 1
    boosted = False
    safe = False
    defenceBonus = 1
    defenderHit = None
    afterAttackHealth = None
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash=None, safe=None, boost=None, chain=None, explode=None, tentacles=None, poison=None):
        self.health = int(health)
        self.veteran = veteran
        self.attacker = attacker
        self.defenceBonusQs = defenceBonus
        self.wallBonus = wallBonus 
        self.splash = splash
        self.safe = safe
        self.boosted = boost
        self.chain = chain
        self.explode = explode
        self.tentacles = tentacles
        self.poison = poison
        
        if self.veteran:
            self.maxHealth += 5
        if self.splash:
            self.multiplier += 0.5
        if self.defenceBonusQs:
                self.defenceBonus = 1.5
        if self.wallBonus and 'Fortify' in self.skills:
            self.defenceBonus = 4.0
        if 'Convert' in self.skills:
            self.multiplier += 2
        if 'Poison' in self.skills:
            self.multiplier += 1
        if 'Freeze' in self.skills:
            self.multiplier += 1
        if self.boosted:
            self.attack += 0.5
            self.movement += 1
        if self.tentacles:
            self.multiplier += 0.5
        if self.poison:
            self.defenceBonus = 0.8
            self.defence *= 0.7

class Warrior(Unit):
    
    unit_class = 'Warrior'
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)
        
class Archer(Unit):
    
    unit_class = 'Archer'
    defence = 1
    cost = 3
    atk_range = 2
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

class Defender(Unit):
    
    unit_class = 'Defender'
    maxHealth = 15
    attack = 1
    defence = 3
    cost = 3
    skills = ['Fortify']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

class Rider(Unit):
    
    unit_class = 'Rider'
    movement = 2
    defence = 1
    cost = 3
    skills = ['Dash', 'Escape', 'Fortify']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)
        
class Cloak(Unit):
    
    unit_class = 'Cloak'
    maxHealth = 5
    movement = 2
    attack = 0
    defence = 0.5
    cost = 8
    retaliate = False
    skills = ['Hide', 'Sneak', 'Infiltrate', 'Dash']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)
        
class Dagger(Unit):
    
    unit_class = 'Dagger'
    cost = 1
    skills = ['Dash', 'Surprise', 'Independent']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)
        
class Mind_bender(Unit):
    
    unit_class = 'Mind Bender'
    attack = 0
    defence = 1
    cost = 5
    retaliate = False
    skills = ['Heal', 'Convert', 'Detect']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

class Swordsman(Unit):
    
    unit_class = 'Swordsman'
    maxHealth = 15
    attack = 3
    defence = 3
    cost = 5
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
            super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Catapult(Unit):
    
    unit_class = 'Catapult'
    attack = 4
    defence = 0
    cost = 8
    atk_range = 3
    retaliate = False
    skills = ['None']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Knight(Unit):
    
    unit_class = 'Knight'
    movement = 3
    attack = 3
    defence = 1
    cost = 8
    skills = ['Dash', 'Persist', 'Fortify']
    attack_chain = True
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)


class Giant(Unit):
    
    unit_class = 'Giant'
    maxHealth = 40
    attack = 5
    defence = 4
    cost = 20
    skills = ['Big']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

class Bunny(Unit):
    
    unit_class = 'Bunny'
    maxHealth = 20
    attack = 5
    cost = 0
    skills = ['Independent']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Raft(Unit):
    
    unit_class = 'Raft'
    cost = 3
    movement = 2
    attack = 0
    defence = 1
    retaliate = False
    skills = ['Carry', 'Float']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison, navalMaxHealth):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)
        
        self.maxHealth = navalMaxHealth

        
class Scout(Unit):
    
    unit_class = 'Scout'
    cost = 8
    movement = 3
    cost = 5
    atk_range = 2
    skills = ['Dash', 'Carry', 'Float', 'Scout']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison, navalMaxHealth):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        self.maxHealth = navalMaxHealth

class Rammer(Unit):
    
    unit_class = 'Rammer'
    cost = 8
    movement = 3
    attack = 3
    defence = 3
    skills = ['Dash', 'Carry', 'Float', 'Scout']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison, navalMaxHealth):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        self.maxHealth = navalMaxHealth

class Bomber(Unit):
    
    unit_class = 'Bomber'
    cost = 18
    movement = 2
    attack = 3
    defence = 2
    atk_range = 3
    retaliate = False
    skills = ['Carry', 'Float', 'Splash', 'Stiff']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison, navalMaxHealth):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        self.maxHealth = navalMaxHealth

class Juggernaut(Unit):
    
    unit_class = 'Juggernaut'
    movement = 2
    attack = 4
    defence = 4
    retaliate = False
    skills = ['Float', 'Splash', 'Stomp']
    unit_in_unit = 'Giant'
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)


class Dinghy(Unit):
    
    unit_class = 'Dinghy'
    maxHealth = 5
    movement = 2
    attack = 0
    defence = 0.5
    cost = 8
    retaliate = False
    skills = ['Hide', 'Sneak', 'Infiltrate', 'Dash']
    unit_in_unit = 'Cloak'
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)


class Pirate(Unit):
    
    unit_class = 'Pirate'
    cost = 1
    skills = ['Dash', 'Surprise', 'Independent']
    unit_in_unit = 'Dagger'
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)


class Amphibian(Rider):
    
    unit_class = 'Amphibian'
    skills = ['Dash', 'Escape', 'Amphibious']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Tridention(Knight):
    
    unit_class = 'Tridention'
    maxHealth = 10
    attack = 2.5
    movement = 2
    skills = ['Dash', 'Persist', 'Amphibious']

    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Crab(Giant):
    
    unit_class = 'Crab'
    attack = 4
    defence = 5
    skills = ['Escape', 'Float']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Jelly(Unit):
    
    unit_class = 'Jelly'
    maxHealth = 20
    attack = 0
    movement = 2
    cost = 8
    skills = 'Stiff, Tentacles, Static, Water'
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Mermaid(Warrior):
    
    unit_class = 'Mermaid'
    skills = ['Dash', 'Fortify', 'Amphibian']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class MermaidArcher(Archer):
    
    unit_class = 'Mermaid Archer'
    skills = ['Dash', 'Fortify', 'Amphibian']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

    
class MermaidDefender(Defender):
    
    unit_class = 'Mermaid Defender'
    skills = ['Fortify', 'Amphibious']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)


class Shark(Unit):
    
    unit_class = 'Shark'
    attack = 3
    movement = 3
    cost = 8
    skills = ['Dash', 'Surprise', 'Water']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Swordsmaid(Swordsman):
    
    unit_class = 'Swordsmaid'
    skills = ['Dash', 'Amphibious']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Scuba(Cloak):
    
    unit_class = 'Scuba'
    skills = ['Hide', 'Creep', 'Infiltrate', 'Dash', 'Scout', 'Amphibious']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class MermaidDagger(Dagger):
    
    unit_class = 'Mermaid Dagger'
    skills = ['Dash', 'Surprise', 'Amphibious']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)


class Puffer(Catapult):
    
    unit_class = 'Puffer'
    movement = 2
    skills = ['Drench', 'Water']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Siren(Mind_bender):
    
    unit_class = 'Siren'
    skills = ['Heal', 'Convert', 'Amphibious']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

    
class Polytaur(Unit):
    
    unit_class = 'Polytaur'
    maxHealth = 15
    attack = 3
    defence = 1
    skills = ['Dash', 'Fortify', 'Independent']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Dragon_egg(Unit):
    
    unit_class = 'Dragon Egg'
    attack = 0
    cost = 20
    retaliate = False
    skills = ['Grow', 'Fortify']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

    
class Baby_Dragon(Unit):
    
    unit_class = 'Baby Dragon'
    maxHealth = 15
    movement = 2
    attack = 3
    defence = 3
    cost = 20
    skills = ['Grow', 'Dash', 'Fly', 'Escape', 'Scout']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

    
class Fire_Dragon(Baby_Dragon):
    
    unit_class = 'Fire Dragon'
    maxHealth = 2
    movement = 3
    attack = 4
    atk_range = 2
    skills = ['Dash', 'Fly', 'Splash', 'Scout']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

    
class Ice_Archer(Archer):
    
    unit_class = 'Ice Archer'
    attack = 0.1
    skills = ['Dash', 'Fortify', 'Freeze']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

    
class Battle_Sled(Unit):
    
    unit_class = 'Battle Sled'
    maxHealth = 15
    movement = 2
    attack = 3
    cost = 5
    skills = ['Dash', 'Escape', 'Skate']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Mooni(Unit):
    
    unit_class = 'Mooni'
    attack = 0
    cost = 10
    retaliate = False
    skills = ['Skate', 'Freeze Area']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Ice_Fortress(Unit):
    
    unit_class  = 'Ice Fortress'
    maxHealth = 20
    attack = 4
    defence = 3
    cost = 15
    skills = ['Skate', 'Scout']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Gaami(Unit):
    
    unit_class = 'Gaami'
    maxHealth = 30
    attack = 4
    defence = 4
    cost = 20
    skills = ['Auto Freeze', 'Freeze Area']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Hexapod(Rider):
    
    unit_class = 'Hexapod'
    maxHealth = 5
    attack = 3
    skills = ['Dash', 'Escape', 'Creep', 'Sneak']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Kiton(Defender):
    
    unit_class = 'Kiton'
    unit_class = 'Kiton'
    skills = ['Poison']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Phychi(Archer):
    
    unit_class = 'Phychi'
    maxHealth = 5
    attack = 1
    movement = 2
    skills = ['Fly', 'Dash', 'Poison', 'Surprise']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

    
class Shaaman(Mind_bender):
    
    unit_class = 'Shaaman'
    attack = 1
    skills = ['Boost', 'Convert']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Raychi(Unit):
    
    unit_class = 'Raychi'
    maxHealth = 15
    movement = 3
    attack = 3
    skills = ['Dash', 'Float', 'Creep', 'Navigate', 'Explode']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Exida(Catapult):
    
    unit_class = 'Exida'
    attack = 3
    defence = 1
    skills = ['Poison', 'Splash']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Doomux(Knight):
    
    unit_class = 'Doomux'
    maxHealth = 20
    attack = 4
    defence = 2
    cost = 10
    skills = ['Dash', 'Creep', 'Explode']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

        
class Centipede(Giant):
    
    unit_class = 'Centipede'
    maxHealth = 20
    movement = 2
    attack = 4
    defence = 3
    skills = ['Dash', 'Eat', 'Creep']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)

    
class Segment(Unit):
    
    unit_class = 'Segment'
    cost = 10
    skills = ['Independent', 'Creep', 'Explode']
    
    def __init__(self, health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison):
        super().__init__(health, veteran, attacker, defenceBonus, wallBonus, splash, safe, boost, chain, explode,  tentacles, poison)
