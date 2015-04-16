import unittest
from enemy import Enemy
from enemy import EnemyHasMaxHealth
from enemy import CannotHealWithNonPositivePoints
from weapon import Weapon
from spell import Spell


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy_alive = Enemy(100, 0, 20)
        self.enemy_1fourthalive = Enemy(25, 0, 20)
        self.enemy_dead = Enemy(0, 50, 20)
        self.enemy_halfalive = Enemy(50, 0, 20)
        self.enemy_3fourthsalive = Enemy(75, 5, 60)
        self.knife = Weapon("knife", 20)
        self.spell = Spell("Fireball", 30, 50, 2)

    def test_init(self):
        self.assertTrue(isinstance(self.enemy_alive, Enemy))
        self.assertTrue(isinstance(self.enemy_dead, Enemy))
        self.assertTrue(isinstance(self.enemy_halfalive, Enemy))

    def test_get_health(self):
        self.assertEqual(self.enemy_alive.get_health(), 100)
        self.assertEqual(self.enemy_dead.get_health(), 0)

    def test_get_mana(self):
        self.assertEqual(self.enemy_alive.get_mana(), 0)
        self.assertEqual(self.enemy_dead.get_mana(), 50)

    def test_is_alive(self):
        self.assertTrue(self.enemy_alive.is_alive())
        self.assertFalse(self.enemy_dead.is_alive())

    def test_can_cast(self):
        self.assertTrue(self.enemy_dead.can_cast())
        self.assertFalse(self.enemy_alive.can_cast())

    def test_take_healing(self):
        with self.assertRaises(CannotHealWithNonPositivePoints):
            self.enemy_1fourthalive.take_healing(-10)
        self.assertFalse(self.enemy_dead.take_healing(20))
        with self.assertRaises(EnemyHasMaxHealth):
            self.enemy_alive.take_healing(10)
        self.assertTrue(self.enemy_halfalive.take_healing(60))
        self.enemy_1fourthalive.take_healing(75)
        self.assertEqual(self.enemy_1fourthalive.get_health(), 100)
        self.enemy_3fourthsalive.take_healing(10)
        self.assertEqual(self.enemy_3fourthsalive.get_health(), 85)

    def test_take_mana(self):
        self.assertFalse(self.enemy_1fourthalive.take_mana())
        self.assertFalse(self.enemy_3fourthsalive.take_mana())
        self.assertFalse(self.enemy_alive.take_mana())
        self.assertFalse(self.enemy_dead.take_mana())
        self.assertFalse(self.enemy_halfalive.take_mana())

    def test_equip(self):
        self.enemy_alive.equip(self.knife)
        self.assertEqual(self.enemy_alive.weapon, self.knife)

    def test_learn(self):
        self.enemy_halfalive.learn(self.spell)
        self.assertEqual(self.enemy_halfalive.spell, self.spell)

    def test_attack(self):
        self.assertEqual(self.enemy_halfalive.attack(by="weapon"), 0)
        self.assertEqual(self.enemy_1fourthalive.attack(by="spell"), None)
        self.enemy_alive.equip(self.knife)
        self.assertEqual(self.enemy_alive.attack(by="weapon"), 20)
        self.enemy_3fourthsalive.learn(self.spell)
        with self.assertRaises(Exception):
            self.enemy_3fourthsalive.attack(by="spell")


if __name__ == '__main__':
    unittest.main()
