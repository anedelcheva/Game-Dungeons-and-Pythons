import sys


class Dungeons():
    def print_map(self):
        file = open("level1.txt", "r")
        my_map = file.read()
        print (my_map)

    def spawn(self):
        file = open("level1.txt", "r")
        my_map = file.read()
        file.close()
        if "S" in my_map:
            my_map = my_map.replace("S", "H")
            file = open("level1.txt", "w+")
            file.write(my_map)
            file.close()
            return True
        elif "." in my_map:
            my_map = my_map.replace(".", "H", 1)
            file = open("level1.txt", "w+")
            file.write(my_map)
            file.close()
            return True
        else:
            return False

"""
a = Dungeons()
a.print_map()
a.spawn()
a.print_map()
"""
