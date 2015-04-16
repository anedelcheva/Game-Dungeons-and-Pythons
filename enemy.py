from spell import Spell
from weapon import Weapon


class EnemyHasMaxHealth(Exception):
    pass


class CannotHealWithNonPositivePoints(Exception):
    pass


class Enemy:

    def __init__(self, health=100, mana=100, damage=20, weapon=None, spell=None):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.weapon = weapon
        self.spell = spell
        self.max_health = 100

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def get_damage(self):
        return self.damage

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self):
        return self.get_mana() > 0

    def take_healing(self, healing_points):
        if healing_points <= 0:
            raise CannotHealWithNonPositivePoints
        if self.get_health() == 0:
            return False
        elif self.get_health() == self.max_health:
            raise EnemyHasMaxHealth
        elif self.get_health() + healing_points > 100:
            self.health = 100
        else:
            self.health += healing_points
        return True

    def take_mana(self):
        return False

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
        elif by == "spell" and self.can_cast():
            if self.spell is None:
                return 0
            elif self.mana < self.spell.get_mana_cost():
                raise Exception
            else:
                self.mana -= self.spell.get_mana_cost()
                return self.spell.get_damage()
        else:
            self.get_damage()
