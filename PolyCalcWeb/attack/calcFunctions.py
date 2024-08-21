import math

def PolyDamageCalc(attacker, defender):
    
    attackForce = attacker.attack * (attacker.health / attacker.maxHealth)
    defenceForce = defender.defence * (defender.health / defender.maxHealth) * defender.defenceBonus 
    totalDamage = attackForce + defenceForce 
    if attackForce > 0:
        attackResult = math.ceil((attackForce / totalDamage) * attacker.attack * 4.5) 
        attackSplash = math.floor(attackResult / 2)
    else:
        attackResult = 0
        attackSplash = 0
    if defenceForce > 0:
        defenceResult = math.ceil((defenceForce / totalDamage) * defender.defence * 4.5)
    else:
        defenceResult = 0
    
    if 'Freeze' in attacker.skills or 'Surprise' in attacker.skills:
        defender.retaliate = False
    if not defender.retaliate or attacker.safe:
        defenceResult = 0
    elif attackResult >= defender.health:
        defenceResult = 0
        attackResult = defender.health
    elif 'Convert' in attacker.skills:
        defenceResult = 0
        attackResult = defender.health
    if attacker.explode:
        attackResult = attackSplash
        defenceResult = attacker.health
    
    end_defenderHealth = defender.health - attackResult
    end_attackerHealth = attacker.health - defenceResult

    return attackResult, defenceResult, end_attackerHealth, end_defenderHealth
    

def starValue(attacker, defender):
    attackResult, defenceResult, end_attackerHealth, end_defenderHealth = PolyDamageCalc(attacker, defender)
    if attacker == 'Juggernaut' and end_defenderHealth != 0:
        attacker.multiplier -= 0.5
    if attacker.chain and end_defenderHealth <= 0:
        attacker.multiplier += 1
    if 'Eat' in attacker.skills and end_defenderHealth <= 0:
        attacker.multiplier += 1
    if end_defenderHealth <= 0:
        attacker.multiplier += 1
    if attackResult == 0:
        attackValue = 1
    else:
        attackValue = 1 + (attackResult / defender.health) * defender.cost * attacker.multiplier
    if defenceResult == 0:
        retaliationCost = 1
    else:
        retaliationCost = 1 + (defenceResult / attacker.health) * attacker.cost * defender.multiplier
    starValue = attackValue / retaliationCost
    return starValue

def bestAttack(attacker_dict, defender_dict):
    bestStarValue = 0
    bestAttackerKey = None
    bestDefender = None
    bestDefenderKey = None
    for defender in defender_dict.values():
        for attacker in attacker_dict.values():
            starVal = starValue(attacker, defender)
            if starVal > bestStarValue:
                bestStarValue = starVal
                bestAttackerKey = list(attacker_dict.keys())[list(attacker_dict.values()).index(attacker)]
                bestDefender = defender
                bestDefenderKey = list(defender_dict.keys())[list(defender_dict.values()).index(defender)]
                
    bestAttackerInstance = attacker_dict[bestAttackerKey]
    bestAttackerInstance.defenderHit = bestDefender
    bestDefenderInstance = defender_dict.get(bestDefenderKey) 
    if bestDefenderInstance is None:
        raise ValueError("Defender instance not found in defender_dict")
    attacker_dict.pop(bestAttackerKey)
    return bestAttackerInstance, bestDefenderInstance


def attackOrder(attacker_dict, defender_dict):
    attackOrder = []
    while len(attacker_dict) > 0:
        if len(defender_dict) == 0:
            break
        
        bestAttacker, bestDefender = bestAttack(attacker_dict, defender_dict)
        attackOrder.append(bestAttacker)
        
        attackResult, defenceResult, end_attackerHealth, end_defenderHealth = PolyDamageCalc(bestAttacker, bestDefender)
        bestAttacker.afterAttackHealth = end_attackerHealth
        bestDefender.afterAttackHealth = end_defenderHealth
        
        if end_defenderHealth <= 0:
            for key, defender in defender_dict.items():
                if defender is bestDefender:
                    defender_dict.pop(key)
                    break
        bestDefender.health = end_defenderHealth
        if 'Poison' in bestAttacker.skills:
            bestDefender.defenceBonus = 0.8
        if 'Freeze' in bestAttacker.skills:
            bestDefender.retaliate = False
        
    return attackOrder

