monster_health = 150
player_damage = 25
attacks = 0

while monster_health > 0:
    monster_health -= player_damage
    attacks += 1
    print(f"Attack {attacks}: Monster's health is now {monster_health}")



print("extra opdracht")
player_damage = 25
monsters = ["100", "150", "300"]

for monster in monsters:
    monster_health = int(monster)
    attacks = 0
    while monster_health > 0:
        print(f"monsters current Health: {monster_health}")
        monster_health -= player_damage
        attacks += 1
        print(f"Attack {attacks}: Monster's health is now {monster_health}")