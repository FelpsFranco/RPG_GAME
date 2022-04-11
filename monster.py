class Esqueleto:
    def __init__(self, name='Esqueleto', vida=60, dano=10, arm=5, vivo=True, atacando=False, defendendo=False):
        self.vida = vida
        self.name = name
        self.dano = dano
        self.arm = arm
        self.vivo = vivo
        self.atacando = atacando
        self.defendendo = defendendo


class Afogado:
    def __init__(self, name='Afogado', vida=120, dano=35, arm=20, vivo=True, atacando=False, defendendo=False):
        self.vida = vida
        self.name = name
        self.dano = dano
        self.arm = arm
        self.vivo = vivo
        self.atacando = atacando
        self.defendendo = defendendo

class Zombie:
    def __init__(self, name='Zumbi', vida=70, dano=15, arm=5, vivo=True, atacando=False, defendendo=False):
        self.vida = vida
        self.name = name
        self.dano = dano
        self.arm = arm
        self.vivo = vivo
        self.atacando = atacando
        self.defendendo = defendendo
