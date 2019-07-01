# Предметная область – магазин. Разработать класс Shop, описывающий работу магазина продуктов.
#
# Разработать класс Products, продукт описывается следующими параметрами:
# уникальный идентификатор, название продукта, стоимость, количество.
#
# Разработать класс Fruit_product на базе класс Product.
# Фрукт характеризуется параметрами: страна изготовителя, срок годности.


class Shop:
    pass


class Products:
    def __init__(self, id_num, name, price, amount):
        self.id_num = id_num
        self.name = name
        self.price = price
        self.amount = amount


class FruitProduct(Products):
    def __init__(self, id_num, name, price, amount, country, storage_life):
        super().__init__(id_num, name, price, amount)
        self.country = country
        self.storage_life = storage_life


# Расширить функционал:
# 1. Формировать id продукта при создании: хранить id в глобальном атрибуте Products и прибавлять и присваивать при init
# 2. Создать метод определения оставшегося срока годности: при init устанавливать дату создания. Текущ дат - дат созд
# 3. Реализовать количество. При соз экз - +кол-во. При продаже(метод) - -кол-во (реализ метод продажи (кол-во прод))
