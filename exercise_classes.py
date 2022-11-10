class Robot: 
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print('My name is ' + self.name)

# r1 = Robot()
# r1.name = 'Tom'
# r1.color = 'Red'
# r1.weight = 30

# r1.introduce_self()

# r2 = Robot()
# r2.name = 'Jerry'
# r2.color = 'blue'
# r2.weight = 40

# r2.introduce_self()

r1 = Robot('Tom', 'Red', 30)
r2 = Robot('Jerry', 'Blue', 40)

# r1.introduce_self()
# r2.introduce_self()

class Person:
    def __init__(self, n, p, i, r):
        self.name = n
        self.personality = p
        self.is_sitting = i
        self.robot_owned = r

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False, r2)
p2 = Person('Becky', 'talkative', True, r1)



p1.robot_owned.introduce_self()
p2.robot_owned.introduce_self() 



