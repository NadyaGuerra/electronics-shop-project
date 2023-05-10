import csv
import os

from src.item import Item


class MixinLanguage:
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLanguage):
    pass
   # def __init__(self, name,price,quantity ):
        #super().__init__(name, price, quantity)
        #MixinLanguage.__init__(self)


