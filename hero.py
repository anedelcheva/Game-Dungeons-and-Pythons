class Hero():

    def __init__(self, name="", title="", health="100", mana="100", mana_regeneration_rate=""):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate

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
            return 0
        else:
            self.health = self.health - damage_points
            return self.get_health()

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        elif healing_points + self.get_health > 100:
            self.health = 100
            return True
        else:
            self.health = self.health + healing_points
            return True

