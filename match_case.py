player_class = input("Choose your class (Warrior, Mage, Archer, Rogue): ")

match player_class:
    case "Warrior":
        health = 150
        damage = 20
    case "Mage":
        health = 80
        damage = 35
    case "Archer":
        health = 100
        damage = 25
    case "Rogue":
        health = 90
        damage = 30
    case _:
        print("Unknown class!")
        health = 100
        damage = 100

print("Class:", player_class)
print("Health:", health)
print("Damage:", damage)
