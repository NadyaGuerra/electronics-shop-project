import csv
import os
from csv import DictReader


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8

    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}"

    @property
    def name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @name.setter
    def name(self, new_name):
        if len(self.__name) <= 10:
            self.__name = new_name
        else:
            raise ValueError("Длина наименования товара больше 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)

    @classmethod
    def instantiate_from_csv(cls, CSV_FILE=os.path.join('..', 'src', 'items.csv')):
        try:
            with open(CSV_FILE, encoding='cp1251', newline='') as file:
                reader = csv.DictReader(file)
                count = ["name", "price", "quantity"]

                if len(list(csv.reader(file)) [0]) != count:
                    raise InstantiateCSVError(f'Файл {CSV_FILE} поврежден')

                for row in reader:
                    cls.all.append(cls(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {CSV_FILE}')

        except PermissionError:
            print(f'Невозможно создать файл {CSV_FILE}')


    @staticmethod
    def string_to_number(number: str):
        return int(number.split('.')[0])


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
