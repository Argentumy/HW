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
    ing = 'ingridient_name'
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

    pprint.pprint(cook_book, width=100)

print(f'Статус файла {file.closed}')
