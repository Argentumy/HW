import pprint


def dictification(self):
    d1 = {}
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


with open('receipts.txt', encoding='utf8') as file:
    cook_book = {}
    ing = 'ingredient_name'
    qua = 'quantity'
    mea = 'measure'
    x1 = 0
    x2 = []
    count = 0
    count1 = 0
    count2 = 0

    for line in file:
        if '|' not in line and len(line) >= 3:
            cook_book.setdefault(line.strip())
            x1 = cook_book.keys()
            # print(x1)
        if len(line.strip()) == 1:
            count = int(line.strip())
            # print(count)
        if '|' in line:
            x2 += (dictification(line.strip().split(sep=' | ')), )

    diclisting(cook_book)
    cook_book.setdefault('Омлет').append(x2[0:3])
    cook_book.setdefault('Утка по-пекински').append(x2[3:7])
    cook_book.setdefault('Запеченный картофель').append(x2[7:10])
    cook_book.setdefault('Фахитос').append(x2[10:15])

    # pprint.pprint(cook_book, width=100)

# print(f'Статус файла {file.closed}')



# Task 2

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 8},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }


def get_shop_list_by_dishes(dishes, persons=1):
    dishes = dishes
    persons = persons
    ingredient = {}
    repeat = 1
    counter = []

    for dish in dishes:
        temp = cook_book.__getitem__(dish)
        # pprint.pprint(cook_book.__getitem__(dish))
        for list in temp:
            # pprint.pprint(list)
            for x in list:
                # pprint.pprint(x)
                ing_name = x['ingredient_name']
                counter.append(ing_name)
                # print(ing_name)
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

    pprint.pprint(ingredient)



get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
