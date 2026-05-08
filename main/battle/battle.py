import time

def battle(hero, enemy):
    print("-" * 30)
    print("MATCH START!")
    print("-" * 30)

    while hero.is_alive() and enemy.is_alive():
        print("-" * 30)
        print(f"{hero.name} | HP: {hero.hp}")
        print(f"{enemy.name} | HP: {enemy.hp}")
        print("-" * 30)

        hero.basic_attack(enemy)
        time.sleep(1)
        if enemy.is_alive():
            enemy.basic_attack(hero)
        time.sleep(1)

    if hero.is_alive():
        print(f"{hero.name} menang!")
    else:
        print(f"{enemy.name} menang!")