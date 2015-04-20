from hero import Hero
from enemy import Enemy


class NotAValidDirection(Exception):
    pass


class Dungeon:

    def __init__(self, filename):
        self.matrix = self.translate_map_to_matrix(filename)
        self.my_map = self.get_map_from_file(filename)

    def get_map_from_file(self, filename):
        my_file = open(filename, 'r')
        my_map = my_file.read()
        my_file.close()
        return my_map

    def write_map_to_file(self, filename):
        my_file = open(filename, 'w+')
        my_file.write(self.my_map)
        my_file.close()

    def matrix_to_map(self):
        my_map = ''
        for row in range(len(self.matrix)):
            current_row = ''.join(self.matrix[row])
            my_map += current_row
            matrixy_map += '\n'
        return my_map

    def print_map(self):
        print (self.my_map())

    def map_to_matrix(self):
        string = self.my_map
        string_to_list = list(string)
        my_matrix = []
        row = []
        for item in string_to_list:
            if item != '\n':
                row.append(item)
            else:
                my_matrix.append(row)
                row = []
        return my_matrix

    def spawn(self, hero):
        self.my_map = self.matrix_to_map()
        if "S" in self.my_map:
            self.my_map = self.my_map.replace("S", "H")
            self.matrix = self.map_to_matrix()
            return True
        elif "." in self.my_map:
            self.my_map = self.my_map.replace(".", "H", 1)
            self.matrix = self.map_to_matrix()
            return True
        else:
            return False

    def translate_map_to_matrix(self, filename):
        string = self.get_map_from_file(filename)
        string_to_list = list(string)
        my_map = []
        row = []
        for item in string_to_list:
            if item != '\n':
                row.append(item)
            else:
                my_map.append(row)
                row = []
        return my_map

    def get_hero_position(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                x = len(self.matrix) - 1 - i
                y = len(self.matrix[0]) - 1 - j
                if self.matrix[x][y] == 'H':
                    return (x, y)

    def move_hero_right(self):
        if self.can_move('right'):
            x = self.get_hero_position()[0]
            y = self.get_hero_position()[1]
            self.swap_hero_and_position(self.matrix[x][y + 1])
           # self.write_map_to_file("level1.txt")
            return True
        return False

    def move_hero_up(self):
        if self.can_move('up'):
            x = self.get_hero_position()[0]
            y = self.get_hero_position()[1]
            self.swap_hero_and_position(self.matrix[x - 1][y])
           # self.write_map_to_file("level1.txt")
            return True
        return False

    def move_hero_down(self):
        if self.can_move('down'):
            x = self.get_hero_position()[0]
            y = self.get_hero_position()[1]
            self.swap_hero_and_position(self.matrix[x + 1][y])
           # self.write_map_to_file("level1.txt")
            return True
        return False

    def move_hero_left(self):
        if self.can_move('left'):
            x = self.get_hero_position()[0]
            y = self.get_hero_position()[1]
            self.swap_hero_and_position(self.matrix[x][y - 1])
           # self.write_map_to_file("level1.txt")
            return True
        return False

    def move_hero(self, direction):
        if direction not in ['left', 'right', 'up', 'down']:
            raise NotAValidDirection

        if direction == 'left':
            self.move_hero_left('left')

        elif direction == 'right':
            self.move_hero_right('right')

        elif direction == 'up':
            self.move_hero_up('up')

        elif direction == 'down':
            self.move_hero_down('down')

        else:
            raise NotAValidDirection

    def can_move(self, direction):

        if direction == 'up':
            return hero_index_row - 1 in range(len(self.matrix)) \
            and self.my_map[hero_index_row - 1][hero_index_col] != '#'
        if direction == 'down':
            return hero_index_row + 1 in range(len(self.matrix)) \
            and self.matrix[hero_index_row + 1][hero_index_col] != '#'
        if direction == 'right':
            return hero_index_col + 1 in range(len(self.matrix[0])) \
            and self.matrix[hero_index_row][hero_index_col + 1] != '#'
        if direction == 'left':
            return hero_index_col - 1 in range(len(self.matrix[0])) \
            and self.matrix[hero_index_row][hero_index_col - 1] != '#'

    def swap_hero_and_position(self, to_position):
        x = self.get_hero_position()[0]
        y = self.get_hero_position()[1]
        self.matrix[x][y], to_position = to_position, self.matrix[x][y]
        self.map = self.matrix_to_map()

dungeon = Dungeon("level1.txt")
dungeon.print_map()
h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
#dungeon.spawn(h)
dungeon.write_map_to_file("level1.txt")
dungeon.print_map()
'''see = dungeon.get_hero_position()[0]
print (see + 1)'''
print (dungeon.get_hero_position())
#print (dungeon.get_hero_position()[0])
#print (dungeon.move_hero_right())
