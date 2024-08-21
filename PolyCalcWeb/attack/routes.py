from flask import Blueprint, render_template, request, jsonify
from PolyCalcWeb.attack import unitClasses as uc
from PolyCalcWeb.attack.calcFunctions import attackOrder

attackBP = Blueprint('attack', __name__)



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

unit_names = [
    "Warrior", "Archer", "Defender", "Rider", "Cloak", "Dagger", "Mind Bender", 
    "Swordsman", "Catapult", "Knight", "Giant", "Bunny", "Raft", 
    "Scout", "Rammer", "Bomber", "Juggernaut", "Dinghy", "Pirate", 
    'Amphibian', 'Tridention', 'Crab', 'Mermaid', 'Mermaid Defender', 'Mermaid Archer',
    'Jelly', 'Shark', 'Swordsmaid', 'Scuba', 'Mermaid Dagger','Puffer',
    'Siren', "Polytaur", "Dragon Egg", "Baby Dragon", 
    "Fire Dragon", "Ice Archer", "Battle Sled", "Mooni", "Ice Fortress", 
    "Gaami", "Hexapod", "Kiton", "Phychi", "Shaaman", "Raychi", 
    "Exida", "Doomux", "Centipede", "Segment"
]

attack_image_filenames = [f'attacker{i}.png' for i in range(1, 51)]
attack_image_unit_mapping = dict(zip(attack_image_filenames, unit_names))

defence_image_filenames = [f'defender{i}.png' for i in range(1, 51)]
defence_image_unit_mapping = dict(zip(defence_image_filenames, unit_names))

@attackBP.route("/attack")
def unit_select():
    return render_template('unit_selection.html', attack_images=attack_image_unit_mapping,
                           defence_images=defence_image_unit_mapping)

@attackBP.route('/process', methods=['POST']) 
def process(): 
    data = request.get_json() 
    
    attackers = data['attackers']
    defenders = data['defenders']
    attackers_health = data['attackers_health']
    defenders_health = data['defenders_health']
    attackers_veteran = data['attackers_veteran']
    defenders_veteran = data['defenders_veteran']
    defenders_defense_bonus = data['defenders_defense_bonus']
    defenders_wall_bonus = data['defenders_wall_bonus']
    attackers_splash = data['attackers_splash']
    attackers_safe = data['attackers_safe']
    attackers_boost = data['attackers_boost']
    attackers_chain = data['attackers_chain']
    attackers_explode = data['attackers_explode']
    attackers_naval_max_health = data['attackers_naval_max_health']
    defenders_naval_max_health = data['defenders_naval_max_health']
    attackers_tentacles = data['attackers_tentacles']
    defenders_tentacles = data['defenders_tentacles']
    defenders_poison = data['defenders_poison']
    
    # print(f"Attackers: {attackers}\nDefenders: {defenders}\nAttackers health: {attackers_health}\nDefenders health: {defenders_health}\nAttackers veteran: {attackers_veteran}\nDefenders veteran: {defenders_veteran}\nDefenders defense bonus: {defenders_defense_bonus}\nDefenders wall bonus: {defenders_wall_bonus}\nAttackers splash: {attackers_splash}\nAttackers safe: {attackers_safe}\nAttackers boost: {attackers_boost}\nAttackers chain: {attackers_chain}\nAttackers explode: {attackers_explode}\nAttackers naval max health: {attackers_naval_max_health}\nDefenders naval max health: {defenders_naval_max_health}\nAttackers tentacles: {attackers_tentacles}\nDefenders tentacles: {defenders_tentacles}\nDefenders poison: {defenders_poison}")
    
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
            
    n = 1
    for unit in defenders:
        unit_name = defend_image_map[unit.split('.')[0].split('-')[0]]
        unit_class = unit_classes[unit_name]
        if unit_class != uc.Raft and unit_class != uc.Scout and unit_class != uc.Rammer and unit_class != uc.Bomber:
            defender_dict[f'defender{n}'] = unit_class(defenders_health[unit], defenders_veteran[unit], False, defenders_defense_bonus[unit], defenders_wall_bonus[unit], False, False, False, False,
                                                        False, defenders_tentacles[unit], defenders_poison[unit])
        else:
            defender_dict[f'defender{n}'] = unit_class(defenders_health[unit], defenders_veteran[unit], False, defenders_defense_bonus[unit], defenders_wall_bonus[unit], False, False, False, False,
                                                        False, defenders_tentacles[unit], defenders_poison[unit], defenders_naval_max_health[unit])
    
    attackOrder_list = attackOrder(attacker_dict, defender_dict)
    print(attackOrder_list[0].unit_class, attackOrder_list[0].health, attackOrder_list[0].afterAttackHealth)
    print(attackOrder_list[0].defenderHit.unit_class, attackOrder_list[0].defenderHit.health)
    
    n = 1
    javaList = []
    while n <= len(attackOrder_list):
        appendList = []
        attacker = attackOrder_list[n-1]
        defender = attacker.defenderHit
        attacker_class = attacker.unit_class
        defender_class = defender.unit_class
        attacker_start_health = attacker.health
        attacker_end_health = attacker.afterAttackHealth
        defender_end_health = defender.afterAttackHealth
        
        appendList.extend([attacker_class, defender_class, attacker_start_health, attacker_end_health, defender_end_health])
        javaList.append(appendList)
        
        n += 1
        
    print(javaList)
    
    return jsonify(result=javaList) 