import csv
import os
from csv import DictReader


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
        self.quntity = quantity
        # Item.all.append(self)

    @property
    def name(self):
        return self.__name

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
        return self.price * self.quntity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)

    # @classmethod
    # def instantiate_from_csv(cls):
    # with open("items.csv,newline=''") as csvfile:
    # reader = csv.Dictreader(csvfile)
    # for row in reader:
    # print(row["name"])

    @classmethod
    def instantiate_from_csv(cls, CSV_FILE=os.path.join('..', 'src', 'items.csv')):

        with open(CSV_FILE, encoding='cp1251',newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls.all.append(cls(row['name'], row['price'], row['quantity']))


    @staticmethod
    def string_to_number(number: str):
        return int(number.split('.')[0])


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)
