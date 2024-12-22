class player():
    def __init__(self, Hp, MHp, atk):
        self.Hp = Hp
        self.MHp = MHp
        self.atk = atk


    def attack(self, target):
        target.Hp -= self.atk

    def heal(self):
        self.Hp += 10
