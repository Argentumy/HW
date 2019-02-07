class Animal:
    hunger = True

    def feed(self):
        print('чамк чамк чамк')
        self.hunger = False

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Birds(Animal):
    fly = True
    egg = 0

    def collect_egs(self, egg):
        self.egg += egg


class Mammal(Animal):
    walk = True


class Duck(Birds):
    voice = 'quack'


class Chicken(Birds):
    voice = 'squawk'


class Goose(Birds):
    voice = 'honk'


class Cow(Mammal):
    voice = 'Moo'
    milk = False

    def milk(self):
        self.milk = True


class Sheep(Mammal):
    voice = 'baa'
    shear = False

    def shear(self):
        self.shear = True


class Goat(Mammal):
    voice = 'bleat'
    milk = False

    def milk(self):
        self.milk = True


goose_0 = Goose('Seriy', 10)
goose_1 = Goose('Beliy', 15)
cow_0 = Cow('Manka', 150)
sheep_0 = Sheep('Barashek', 40)
sheep_1 = Sheep('Kudryaviy', 45)
chicken_0 = Chicken('Ko-Ko', 5)
chicken_1 = Chicken('Kukareku', 10)
goat_0 = Goat('Roga', 30)
goat_1 = Goat('Kopyta', 40)
duck_0 = Duck('Kryakva', 20)

field_weight = 'weight'
field_name = 'name'


def weight_calc(*args):
    total_weight = 0
    value_list = []
    max_value = 0
    for arg in args:
        total_weight += getattr(arg, field_weight)
        value_list.append(getattr(arg, field_weight))
    print("Общий вес фермы составляет:", total_weight)
    max_value = max(value_list)
    for arg1 in args:
        if max_value == getattr(arg1, field_weight):
            print('Самое тяжёлое животное:', getattr(arg1, field_name))


weight_calc(goose_0, goose_1, cow_0, sheep_0, sheep_1, chicken_0, chicken_1, goat_0, goat_1, duck_0)

print(Animal.hunger)
