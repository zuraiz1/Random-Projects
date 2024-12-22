class enemy():
    def __init__(self,name, Hp, MHp, atk):
        self.name = name
        self.Hp = Hp
        self.MHp = MHp
        self.atk = atk
        self.alive = True

    def attack(self, target):
        target.Hp -= self.atk
