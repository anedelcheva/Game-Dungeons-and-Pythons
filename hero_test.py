from hero import Hero
from weapon import Weapon
from spell import Spell
import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero1 = Hero("Arthur", "knight", 100, 100, 2)
        self.weapon1 = Weapon(name="The Axe of Destiny", damage=20)
        self.spell1 = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)

    def test_init(self):
        self.assertTrue(isinstance(self.hero1, Hero))

    def test_known_as(self):
        self.assertEqual(self.hero1.known_as(), "Arthur the knight")

    def test_is_alive_and_take_damage(self):
        self.assertTrue(self.hero1.is_alive())
        self.hero1.take_damage(70)
        self.assertTrue(self.hero1.is_alive())
        self.assertEqual(self.hero1.get_health(), 30)
        self.hero1.take_damage(40)
        self.assertFalse(self.hero1.is_alive())

    def test_take_healing(self):
        self.hero1.take_damage(50)
        self.hero1.take_healing(20)
        self.assertTrue(self.hero1.get_health() == 70)
        self.assertTrue(self.hero1.take_healing(10))
        self.hero1.take_damage(80)
        self.assertFalse(self.hero1.take_healing(20))

    def test_equip(self):
        self.hero1.equip(self.weapon1)
        self.assertIsInstance(self.hero1.weapon, Weapon)

    def test_learn(self):
        self.hero1.learn(self.spell1)
        self.assertIsInstance(self.hero1.spell, Spell)

if __name__ == '__main__':
    unittest.main()
