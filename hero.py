from weapon import Weapon
from spell import Spell


class Hero():

    def __init__(self, name="", title="", health=100, mana=100,
                 mana_regeneration_rate=0, weapon=None, spell=None):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = weapon
        self.spell = spell

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self):
        return self.get_mana() > 0

    def take_damage(self, damage_points):
        if damage_points > self.get_health():
            self.health = 0
            return self.get_health()
        else:
            self.health = self.health - damage_points
            return self.get_health()

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        elif healing_points + self.get_health() > 100:
            self.health = 100
            return True
        else:
            self.health = self.health + healing_points
            return True

    def take_mana(self, mana_points):
        if self.mana + mana_points > 100:
            self.mana = 100
        else:
            self.mana = self.mana + mana_points

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, by):
        if by == "weapon":
            if self.weapon is None:
                return 0
            else:
                return self.weapon.get_damage()
        if by == "magic" and self.can_cast():
            if self.spell is None:
                return 0
            if self.mana < self.spell.get_mana_cost():
                raise Exception
            else:
                self.mana -= self.spell.get_mana_cost()
                return self.spell.get_damage()
