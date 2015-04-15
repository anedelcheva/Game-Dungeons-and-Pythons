class EnemyHasMaxHealth(Exception):
    pass


class CannotHealWithNonPositivePoints(Exception):
    pass


class Enemy:

    def __init__(self, health=100, mana=100, damage=20):
        self.health = health
        self.mana = mana
        self.damage = damage
        self.max_health = 100

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

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
