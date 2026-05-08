from character.character import Character # import class Character

# class Hero turunan dari Character
class Hero(Character):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)

    def basic_attack(self, target):
        target.hp -= self.attack
        print(f"{self.name} menyerang {target.name} | DMG: {self.attack}")
        print("-" * 30)