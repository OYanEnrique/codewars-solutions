'''
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

Your function also receives a third argument, a string, with the name of the fighter that attacks first.

Example:
  declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"
  
  Lew attacks Harry; Harry now has 3 health.
  Harry attacks Lew; Lew now has 6 health.
  Lew attacks Harry; Harry now has 1 health.
  Harry attacks Lew; Lew now has 2 health.
  Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
  
'''
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__

def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        attacker = fighter1
        defender = fighter2
    else:
        attacker = fighter2
        defender = fighter1
    while True:
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0:
            return attacker.name
        attacker, defender = defender, attacker

# Test
if __name__ == "__main__":
    # Example Test: Lew starts
    lew = Fighter("Lew", 10, 2)
    harry = Fighter("Harry", 5, 4)
    winner = declare_winner(lew, harry, "Lew")
    print(f"Winner: {winner}")  # Expected: "Lew"
    
    # Test 2: Harry starts
    lew2 = Fighter("Lew", 10, 2)
    harry2 = Fighter("Harry", 5, 4)
    winner2 = declare_winner(lew2, harry2, "Harry")
    print(f"Winner: {winner2}")  # Who wins?
        