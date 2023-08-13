from random import *

class CRM:
    def __init__(self):
        self.__abiturients = {}

    def add(self, abiturient):
        # получение СНИЛСа
        number = abiturient.get_number()
        # добавление абитуриента в словарь,
        # где информация хранится под СНИЛСами
        if self.__is_number(number):
            if number in self.__abiturients:
                print('Такой абитуриент уже введен в базу')
            self.__abiturients[number] = abiturient
        else:
            print('Снилс указан с ошибкой')

    def get_status(self, number):
        return self.__abiturients[number].get_status()

    @staticmethod
    def __is_number(number):
        return number[0:3].isdigit() and number[4:7].isdigit() and number[8:11].isdigit() and number[12:].isdigit() and number[3] == "-" and number[7] == "-" and number[11] == " "


class Abiturient:
    def __init__(self, surname, name, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age

        # СНИЛС
        self.__number = number

        # Russian National Exam (ЕГЭ), баллы
        self.__RNE = self.__fetch_RNE()

        # есть ли БВИ
        self.__bvi = bvi

    @property
    def name(self):
        return self.__name

    def name(self, name):
        self.__name = self.__check_name(name)

    @property
    def surname(self):
        return self.__surname

    def surname(self, surname):
        self.__surname = self.__check_name(surname)

    @property
    def patronymic(self):
        return self.__patronymic

    def patronymic(self, patronymic):
        self.__patronymic = self.__check_name(patronymic)

    @property
    def age(self):
        return self.__age

    def age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            return "Возраст введен неправильно"

    @property
    def bvi(self):
        return self.__bvi

    def bvi(self, bvi):
        if isinstance(bvi, bool):
            self.__bvi = bvi
        else:
            return "БВИ введено неправильно"

    @property
    def RNE(self):
        return self.__RNE

    # проверка, все ли результаты ЕГЭ корректны
    def RNE(self, RNE):
        if isinstance(RNE, tuple):
            if len(RNE) != 3 or any(x < 0 or x > 100 for x in RNE):
                return "Ошибка в введенных данных"
            if all(isinstance(x, int) for x in RNE):
                self.__RNE = RNE
            else:
                return "Ошибка в введенных данных"
        else:
            return "Ошибка в введенных данных"

    # функция получения результатов ЕГЭ
    def __fetch_RNE(self):
        return (randint(0, 100) for i in range(3))

    # функция ответа на вопрос, проходит ли абитуриент
    def __check(self):
        if self.__bvi or random() > 0.95:
            return "Да"
        return "Нет"

    # корректно ли введено имя?
    @staticmethod
    def __check_name(name):
        if isinstance(name, str) and name.isalpha():
                return "Ошибка в введенных данных"
                #сделает первую букву заглавной
                return name.capitalize()
        else:
            return "Ошибка в введенных данных"

    def get_status(self):
        return self.__check()

    def get_number(self):
        return self.__number

module = CRM()


module.add(Abiturient("Уэйн", "Брюс", "Иванович", 19, "179-513-431 49"))

module.add(Abiturient("Иванов", "Василий", "Вячеславович", 77, "189-677-431 66", True))

module.add(Abiturient("Иванов", "Петр", "Алексеевич", 18, "100-513-478 78", False))

print(module.get_status("179-513-431 49"))
print(module.get_status("189-677-431 66"))
print(module.get_status("100-513-478 78"))

from random import *


class InvalidAction(Exception):
    pass


class Emerald:
    __statuses = ["не учтён", "учтён", "отправлен под спуд"]

    def __init__(self):
        self.__status = 0
        self.__price = 0

    def account(self):
        if self.__status == 0:
            self.__status = 1
            self.price = randint(5, 15) * 10
        else:
            raise InvalidAction

    def store(self):
        if self.__status == 1:
            self.__status = 2
        else:
            raise InvalidAction

    @property
    def status(self):
        return Emerald.__statuses[self.__status]

    @property
    def price(self):
        return self.__price

    def price(self, price):
        if isinstance(price, int) and price >= 0:
            self.__price = price
        else:
            raise InvalidAction

    def __str__(self):
        return "Изумруд"


class Shell:
    __statuses = ["не учтена", "учтена", "отправлена в монетолитейное отделение", "переплавлена в монету"]

    def __init__(self):
        self.__status = 0
        self.__price = 0

    def account(self):
        if self.__status == 0:
            self.__status = 1
            self.price = randint(3, 10)
        else:
            raise InvalidAction

    def process(self):
        if self.__status == 1:
            self.__status = 2
        else:
            raise InvalidAction

    def smelt(self, archive):
        if self.__status == 2:
            self.__status = 3

            for i in range(self.__price // 5):
                archive.add(Entry(Coin(Coin.next_serial, "2023", 5)))
                Coin.next_serial += 1

            for j in range(self.price % 5):
                archive.add(Entry(Coin(Coin.next_serial, "2023", 1)))
                Coin.next_serial += 1
        else:
            raise InvalidAction

    @property
    def status(self):
        return Shell.__statuses[self.__status]

    @property
    def price(self):
        return self.__price

    def price(self, price):
        if isinstance(price, int) and price >= 0:
            self.__price = price
        else:
            raise InvalidAction

    def __str__(self):
        return "Золотая скорлупка"


class Coin:
    next_serial = 0

    def __init__(self, serial_number, year, value):
        self.__serial_number = serial_number
        self.__year = year
        self.__value = value

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def year(self):
        return self.__year

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return "Монета"


class Archive:
    def __init__(self):
        self.__storage = []

    def add(self, entry):
        if isinstance(entry, Entry):
            self.__storage.append(entry)
        else:
            raise InvalidAction

    def get(self, index):
        entry = self.__storage[index]

        if entry == None or entry.secret:
            return f"[Запись {index}] Информация удалена"

        item = entry.item
        result = f"[Запись {index}-{entry.ID}] "
        result += f"[{str(item)}] {entry.date} '{entry.info}' "

        if isinstance(item, Emerald) or isinstance(item, Shell):
            result += f"Статус: {item.status} Цена: {item.price} "

        elif isinstance(item, Coin):
            result += f"Серийный номер: {str(item.serial_number).zfill(6)} "
            result += f"Год выпуска: {item.year} "
            result += f"Номинал: {item.value}"
        return result

    def edit(self, index, info):
        self.__storage[index].info = info

    def classify(self, index):
        self.__storage[index].secret = True

    def declassify(self, index):
        self.__storage[index].secret = False

    def delete(self, index):
        self.__storage[index] = None

    def info(self):
        for i in range(len(self.__storage)):
            print(self.get(i))

    def item(self, index):
        return self.__storage[index].item


class Entry:
    def __init__(self, item, date="01.01.2023", info="", secret=False):

        self.__ID = self.__get_next_ID()

        self.__item = item

        self.__date = date

        self.__info = info

        self.__secret = secret

    def __get_next_ID(self):
        return hash(self)

    @property
    def ID(self):
        return self.__ID

    @property
    def item(self):
        return self.__item

    @property
    def date(self):
        return self.__date

    @property
    def info(self):
        return self.__info

    # установщик info
    def info(self, info):
        self.__info = info

    @property
    def secret(self):
        return self.__secret

    # установщик secret
    def secret(self, update):
        if isinstance(update, bool):
            self.__secret = update
        else:
            raise InvalidAction


archive = Archive()
for i in range(20):
    shell = Shell()
    shell.account()

    archive.add(Entry(shell))

archive.info()

for _ in range(10):
    emerald = Emerald()
    emerald.account()

    archive.add(Entry(emerald))

archive.info()

for i in range(20, 30):
    archive.item(i).store()

archive.info()

for i in range(20):
    archive.item(i).process()

archive.info()

for i in range(20):
    archive.item(i).smelt(archive)

archive.info()

for i in range(20, 30):
    archive.classify(i)

archive.info()

for i in range(20):
    archive.delete(i)

archive.info()

for i in range(25, 30):
    archive.declassify(i)

archive.info()

for i in range(25, 30):
    archive.edit(i, "Информация обновлена")

archive.info()