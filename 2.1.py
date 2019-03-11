from pprint import pprint


def dictification(self):
    d1 = {}
    ing = 'ingredient_name'
    qua = 'quantity'
    mea = 'measure'
    self = self
    d1.setdefault(ing, self[0]), d1.setdefault(qua, self[1]), d1.setdefault(mea, self[2])
    return d1


def dict_keys(self):
    self = self
    for key in self:
        f'key: {key}'
        return key


def diclisting(self):
    self = self
    for key in self:
        self[key] = []


def cook(self):
    cook_book = {}
    xkeys = 0
    xvalues = []
    count = 0

    for line in self:
        if '|' not in line and len(line) >= 3:
            cook_book.setdefault(line.strip())
            xkeys = cook_book.keys()
        if len(line.strip()) == 1:
            count = int(line.strip())
        if '|' in line:
            xvalues += (dictification(line.strip().split(sep=' | ')), )

    diclisting(cook_book)
    cook_book.setdefault('Омлет').append(xvalues[0:3])
    cook_book.setdefault('Утка по-пекински').append(xvalues[3:7])
    cook_book.setdefault('Запеченный картофель').append(xvalues[7:10])
    cook_book.setdefault('Фахитос').append(xvalues[10:15])

    # pprint(cook_book, width=100)

    return cook_book


# Task 2


def get_shop_list_by_dishes(dishes, persons=1):
    with open('receipts.txt', encoding='utf8') as file:
        cook_book = cook(file)
    dishes = dishes
    persons = persons
    ingredient = {}
    repeat = 1
    counter = []

    for dish in dishes:
        temp = cook_book.__getitem__(dish)
        for list in temp:
            for x in list:
                ing_name = x['ingredient_name']
                counter.append(ing_name)
                if ing_name in ingredient.keys():
                    repeat += 1
                    ingredient[ing_name] = {'measure': x['measure'], 'quantity': int(x['quantity'])}
                else:
                    ingredient[ing_name] = {'measure': x['measure'], 'quantity': int(x['quantity'])}

    for x in set(counter):
        temp1 = "{0}\n{1}".format(x, counter.count(x))
        if counter.count(x) >= 2:
            temp2 = ingredient[x].get('quantity') * 2
            ingredient[x].update({'quantity': temp2})

    for x in ingredient:
        temp3 = persons
        temp4 = ingredient[x].get('quantity')
        ingredient[x].update({'quantity': temp3 * temp4})

    pprint(ingredient)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
