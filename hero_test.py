from hero import Hero
import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero1 = Hero("Arthur", "knight", "100", "100", "2")

    def test_init(self):
        self.assertTrue(isinstance(self.hero1, Hero))

    def test_known_as(self):
        self.assertEqual(self.hero1.known_as(), "Arthur the knight")

    def test_is_alive(self):
        self.assertTrue(self.hero1)
        self.hero1.take_damage("70")
        self.assertTrue(self.hero1)
        self.assertEqual(self.hero1.get_health(), "30")
        #self.hero1.take_damage("40")
        #print(self.hero1.get_health())
        # self.assertFalse(self.hero1)

if __name__ == '__main__':
    unittest.main()
