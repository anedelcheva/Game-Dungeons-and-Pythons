from hero import Hero
from weapon import Weapon
from spell import Spell
from enemy import Enemy
from dungeons import Dungeon
import unittest


class TestDungeons(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon("level1.txt")
        self.hero = Hero("Arthur", "knight", 100, 100, 2)
        self.my_map = "S.##.....T\n#T##..###.\n#.###E###E\n#.E...###.\n###T#####G\n"
        self.my_matrix = [['S', '.', '#', '#', '.', '.', '.', '.', '.', 'T'], ['#', 'T', '#', '#', '.', '.', '#', '#', '#', '.'], ['#', '.', '#', '#', '#', 'E', '#', '#', '#', 'E'], ['#', '.', 'E', '.', '.', '.', '#', '#', '#', '.'], ['#', '#', '#', 'T', '#', '#', '#', '#', '#', 'G']]

    def test_init(self):
        self.assertTrue(isinstance(self.dungeon, Dungeon))
        self.assertEqual(self.dungeon.my_map, self.my_map)
        self.assertEqual(self.my_matrix, self.dungeon.matrix)

    def test_matrix_to_map(self):
        self.assertEqual(self.dungeon.matrix_to_map(), self.my_map)

    def test_map_to_matrix(self):
        self.assertEqual(self.dungeon.map_to_matrix(), self.my_matrix)

    def test_get_hero_position(self):
        self.dungeon.spawn(self.hero)
        self.assertEqual(self.dungeon.get_hero_position(), (0, 0))
        self.dungeon.spawn(self.hero)
        self.dungeon.spawn(self.hero)
        self.assertEqual(self.dungeon.get_hero_position(), (0, 4))

    def test_move_hero(self):
        self.dungeon.spawn(self.hero)
        self.assertFalse(self.dungeon.move_hero('left'))


if __name__ == '__main__':
    unittest.main()


