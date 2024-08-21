
import unitClasses as uc
from calcFunctions import *

attackers =  ['attacker1.png-1', 'attacker9.png-1', 'attacker14.png-1', 'attacker44.png-1', 'attacker48.png-1']
defenders = ['defender1.png-1', 'defender10.png-1', 'defender11.png-1']
attackers_health = {'attacker1.png-1':10, 'attacker9.png-1':10, 'attacker14.png-1':10, 'attacker44.png-1':5, 'attacker48.png-1':10}
defenders_health = {'defender1.png-1': 10, 'defender10.png-1': 10, 'defender11.png-1': 40}
attackers_veteran =  {'attacker1.png-1': False, 'attacker9.png-1': False, 'attacker14.png-1': False, 'attacker44.png-1': False, 'attacker48.png-1': False}
defenders_veteran = {'defender1.png-1': False, 'defender10.png-1': False, 'defender11.png-1': False}
defenders_defense_bonus = {'defender1.png-1': False, 'defender10.png-1': False, 'defender11.png-1': False}
defenders_wall_bonus = {'defender1.png-1': False, 'defender10.png-1': False, 'defender11.png-1': False}
attackers_splash =  {'attacker1.png-1': False, 'attacker9.png-1': False, 'attacker14.png-1': False, 'attacker44.png-1': False, 'attacker48.png-1': False}
attackers_safe = {'attacker1.png-1': False, 'attacker9.png-1': True, 'attacker14.png-1': True, 'attacker44.png-1': False, 'attacker48.png-1': False}
attackers_boost = {'attacker1.png-1': False, 'attacker9.png-1': False, 'attacker14.png-1': False, 'attacker44.png-1': False, 'attacker48.png-1': False}
attackers_chain = {'attacker1.png-1': False, 'attacker9.png-1': False, 'attacker14.png-1': False, 'attacker44.png-1': False, 'attacker48.png-1': False}
attackers_explode = {'attacker1.png-1': False, 'attacker9.png-1': False, 'attacker14.png-1': False, 'attacker44.png-1': False, 'attacker48.png-1': True}
attackers_naval_max_health = {'attacker14.png-1': 15}
defenders_naval_max_health = {}
attackers_tentacles = {'attacker1.png-1': False, 'attacker9.png-1': False, 'attacker14.png-1': False, 'attacker44.png-1': False, 'attacker48.png-1': False}
defenders_tentacles = {'defender1.png-1': False, 'defender10.png-1': False, 'defender11.png-1': False}
defenders_poison = {'defender1.png-1': False, 'defender10.png-1': False, 'defender11.png-1': False}

unit_classes = {
    'Warrior': uc.Warrior, 'Archer': uc.Archer,'Defender': uc.Defender,'Rider': uc.Rider, 
    'Cloak': uc.Cloak, 'Dagger': uc.Dagger, 'Mind bender': uc.Mind_bender, 'Swordsman': uc.Swordsman,
    'Catapult': uc.Catapult, 'Knight': uc.Knight, 'Giant': uc.Giant,'Bunny': uc.Bunny, 
    'Raft': uc.Raft,'Scout': uc.Scout,'Rammer': uc.Rammer,'Bomber': uc.Bomber,'Juggernaut': uc.Juggernaut,
    'Dinghy': uc.Dinghy,'Pirate': uc.Pirate, 'Amphibian': uc.Amphibian,'Tridention': uc.Tridention,
    'Crab': uc.Crab, 'Mermaid': uc.Mermaid, 'Mermaid Defender': uc.MermaidDefender, 'Mermaid Archer': uc.MermaidArcher,
    'Jelly': uc.Jelly, 'Shark': uc.Shark, 'Swordsmaid': uc.Swordsmaid, 'Scuba': uc.Scuba, 'Mermaid Dagger': uc.MermaidDagger, 'Puffer': uc.Puffer,
    'Siren': uc.Siren, 'Polytaur': uc.Polytaur, 'Dragon Egg': uc.Dragon_egg,'Baby Dragon': uc.Baby_Dragon,
    'Fire Dragon': uc.Fire_Dragon,'Ice Archer': uc.Ice_Archer,'Battle Sled': uc.Battle_Sled,'Mooni': uc.Mooni,
    'Ice Fortress': uc.Ice_Fortress,'Gaami': uc.Gaami,'Hexapod': uc.Hexapod,'Kiton': uc.Kiton,'Phychi': uc.Phychi,
    'Shaaman': uc.Shaaman,'Raychi': uc.Raychi,'Exida': uc.Exida,'Doomux': uc.Doomux,'Centipede': uc.Centipede,
    'Segment': uc.Segment 
    }

attack_image_map = {
    'attacker1': 'Warrior', 'attacker2': 'Archer', 'attacker3': 'Defender', 'attacker4': 'Rider', 'attacker5': 'Cloak', 'attacker6': 'Dagger', 'attacker7': 'Mind bender', 'attacker8': 'Swordsman', 'attacker9': 'Catapult',
    'attacker10': 'Knight', 'attacker11': 'Giant', 'attacker12': 'Bunny', 'attacker13': 'Raft', 'attacker14': 'Scout', 'attacker15': 'Rammer', 'attacker16': 'Bomber', 'attacker17': 'Juggernaut', 'attacker18': 'Dinghy', 
    'attacker19': 'Pirate', 'attacker20': 'Mermaid', 'attacker21': 'Mermaid Archer', 'attacker22': 'Mermaid Defender', 'attacker23': 'Mermaid Dagger', 'attacker24': 'Swordsmaid', 'attacker25': 'Shark', 
    'attacker26': 'Jelly', 'attacker27': 'Puffer', 'attacker28': 'Siren', 'attacker29': 'Scuba', 'attacker30': 'Amphibian', 'attacker31': 'Tridention', 'attacker32': 'Crab', 'attacker33': 'Polytaur', 
    'attacker34': 'Dragon Egg', 'attacker35': 'Baby Dragon', 'attacker36': 'Fire Dragon', 'attacker37': 'Ice Archer', 'attacker38': 'Battle Sled', 'attacker39': 'Mooni', 'attacker40': 'Ice Fortress',
    'attacker41': 'Gaami', 'attacker42': 'Hexapod', 'attacker43': 'Kiton', 'attacker44': 'Phychi', 'attacker45': 'Shaaman', 'attacker46': 'Raychi', 'attacker47': 'Exida', 'attacker48': 'Doomux', 
    'attacker49': 'Centipede', 'attacker50': 'Segment'
}

defend_image_map = {
    'defender1': 'Warrior', 'defender2': 'Archer', 'defender3': 'Defender', 'defender4': 'Rider', 'defender5': 'Cloak', 'defender6': 'Dagger', 'defender7': 'Mind bender', 'defender8': 'Swordsman', 'defender9': 'Catapult',
    'defender10': 'Knight', 'defender11': 'Giant', 'defender12': 'Bunny', 'defender13': 'Raft', 'defender14': 'Scout', 'defender15': 'Rammer', 'defender16': 'Bomber', 'defender17': 'Juggernaut', 'defender18': 'Dinghy', 
    'defender19': 'Pirate', 'defender20': 'Mermaid', 'defender21': 'Mermaid Archer', 'defender22': 'Mermaid Defender', 'defender23': 'Mermaid Dagger', 'defender24': 'Swordsmaid', 'defender25': 'Shark', 
    'defender26': 'Jelly', 'defender27': 'Puffer', 'defender28': 'Siren', 'defender29': 'Scuba', 'defender30': 'Amphibian', 'defender31': 'Tridention', 'defender32': 'Crab', 'defender33': 'Polytaur', 
    'defender34': 'Dragon Egg', 'defender35': 'Baby Dragon', 'defender36': 'Fire Dragon', 'defender37': 'Ice Archer', 'defender38': 'Battle Sled', 'defender39': 'Mooni', 'defender40': 'Ice Fortress',
    'defender41': 'Gaami', 'defender42': 'Hexapod', 'defender43': 'Kiton', 'defender44': 'Phychi', 'defender45': 'Shaaman', 'defender46': 'Raychi', 'defender47': 'Exida', 'defender48': 'Doomux', 
    'defender49': 'Centipede', 'defender50': 'Segment'
}

attacker_dict = {}
defender_dict = {}

n = 1
for unit in attackers:
    unit_name = attack_image_map[unit.split('.')[0].split('-')[0]]
    unit_class = unit_classes[unit_name]
    if unit_class != uc.Raft and unit_class != uc.Scout and unit_class != uc.Rammer and unit_class != uc.Bomber:
        attacker_dict[f'attacker{n}'] = unit_class(attackers_health[unit], attackers_veteran[unit], True, None, None, attackers_splash[unit], attackers_safe[unit], attackers_boost[unit], 
                                                   attackers_chain[unit], attackers_explode[unit], attackers_tentacles[unit], False)
        n += 1
    else:
        attacker_dict[f'attacker{n}'] = unit_class(attackers_health[unit], attackers_veteran[unit], True, None, None, attackers_splash[unit], attackers_safe[unit], attackers_boost[unit], 
                                                   attackers_chain[unit], attackers_explode[unit], attackers_tentacles[unit], False, attackers_naval_max_health[unit])
        n += 1
        

for i, unit in enumerate(defenders):
    unit_name = defend_image_map[unit.split('.')[0].split('-')[0]]
    unit_class = unit_classes[unit_name]
    key = f'defender{i+1}' 
    if unit_class != uc.Raft and unit_class != uc.Scout and unit_class != uc.Rammer and unit_class != uc.Bomber:
        defender_dict[key] = unit_class(defenders_health[unit], defenders_veteran[unit], False, defenders_defense_bonus[unit], defenders_wall_bonus[unit], False, False, False, False,
                                        False, defenders_tentacles[unit], defenders_poison[unit])
    else:
        defender_dict[key] = unit_class(defenders_health[unit], defenders_veteran[unit], False, defenders_defense_bonus[unit], defenders_wall_bonus[unit], False, False, False, False,
                                        False, defenders_tentacles[unit], defenders_poison[unit], defenders_naval_max_health[unit])

    
list = attackOrder(attacker_dict, defender_dict)
print(list[0].defenderHit.unit_class)


n = 1
javaList = []
while n <= len(list):
    appendList = []
    attacker = list[n-1]
    defender = attacker.defenderHit
    attacker_class = attacker.unit_class
    defender_class = defender.unit_class
    attacker_start_health = attacker.health
    attacker_end_health = attacker.afterAttackHealth
    defender_end_health = defender.afterAttackHealth
    
    appendList.extend([attacker_class, defender_class, attacker_start_health, attacker_end_health, defender_end_health])
    javaList.append(appendList)
    n+=1

print(javaList)
