class Character:
    def __init__(self, name, hp, attack,):
        # atribut character
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0
        