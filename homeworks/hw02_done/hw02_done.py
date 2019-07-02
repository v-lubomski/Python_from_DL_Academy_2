# Предметная область – магазин. Разработать класс Shop, описывающий работу магазина продуктов.
#
# Разработать класс Products, продукт описывается следующими параметрами:
# уникальный идентификатор, название продукта, стоимость, количество.
#
# Разработать класс Fruit_product на базе класс Product.
# Фрукт характеризуется параметрами: страна изготовителя, срок годности.
from datetime import datetime


class Shop:
    def __init__(self, working_hours: list, types_of_products: list):
        """
        :param working_hours: часы работы магазина в виде списка [с, до]
        :param types_of_products: список продуктов, продающихся в магазине в виде списка списков [[фрукты], [овощи] ...]
        """
        self._working_hours = working_hours
        self._types_of_products = types_of_products

    @property
    def working_hours(self):
        return 'Магазин работает с {} до {}.'.format(*self._working_hours)

    def is_shop_open(self):
        """Проверяет открыт ли в данный момент магазин"""
        start_time = self._working_hours[0]
        end_time = self._working_hours[1]
        if start_time < datetime.now().hour < end_time:
            return 'Магазин открыт.'
        else:
            return 'Магазин закрыт'

    @property
    def _all_products(self):
        """Возвращает все продукты магазина единым списком ОБЪЕКТОВ, независимо от типа продукта"""
        return [product for product_type in self._types_of_products for product in product_type]

    # Проверка не заканчиваются ли какие-либо из товаров, и если да - выводим какие, и их остаток
    def check_amount(self):
        """Выводит название и кол-во товара, которого в магазине меньше 10 кг"""
        few_products = 0  # Устанавливаем счётчик, для того чтобы понимать - есть ли продукты, которых мало
        notice = 'Следующие товары заканчиваются в магазине: '
        for pr in self._all_products:   # Для каждого продукта в магазине...
            if pr.amount < 10:  # ...если его кол-во меньше 10...
                few_products += 1  # ...увеличиваем счётчик продуктов, которых не хватает.
                notice += '\n{} - {} кг'.format(pr.name, pr.amount)  # Добавляем название и кол-во в отчёт
        if few_products == 0:  # Счётчик пригодился: если товаров, которых мало нет - всех продуктов достаточно
            return 'Продуктов пока достаточно'
        else:
            return notice

    # Продажа товара
    def sell(self, product_name, sell_amount):
        """
        Имитирует продажу товара, увабляя количество продаваемого товара на указанное число единиц
        :param product_name: Название товара с маленькой буквы в ед.ч. Пример: "apple".
        :param sell_amount: Количество проданного товара
        """
        for product in self._all_products:   # Для каждого продукта в магазине...
            if product.name == product_name:  # ...ищем имя, соответствующее указанному.
                product.amount -= sell_amount  # Если имя совпало - уменьшаем кол-во товара в магазине


class Products:
    id_num = 0

    def __init__(self, name, price, amount):
        """
        :param name: Название продукта с маленькой буквы в ед.числе. Пример: "apple".
        :param price: Стоимость продукта в долларах.
        :param amount: Количество товара в кг.
        """
        Products.id_num += 1  # При создании объекта увеличивает id родительского класса на 1
        self.id_num = Products.id_num  # затем присваивает текущий id.
        # Таким образом, всем товарам автоматически присваивается уникальный id.
        self.name = name
        self.price = price
        self.amount = amount


class FruitProduct(Products):
    def __init__(self, name: str, price: float, amount: float, country: str, shelf_life: int):
        """
        :param name: Название продукта с маленькой буквы в ед.числе. Пример: "apple".
        :param price: Стоимость продукта в долларах.
        :param amount: Количество товара в кг.
        :param country: Страна происхождения
        :param shelf_life: Срок годности (суток)
        """
        super().__init__(name, price, amount)
        self.country = country
        self.storage_life = shelf_life


fruits = [FruitProduct(name='apple', price=3.0, amount=100.0, country='Jamaica', shelf_life=20),
          FruitProduct(name='banana', price=6.0, amount=7.0, country='Siberia', shelf_life=10),
          FruitProduct(name='kluckwa', price=15.0, amount=10.0, country='Brazil', shelf_life=100),
          FruitProduct(name='pineapple', price=9.0, amount=30.0, country='Norway', shelf_life=20),
          FruitProduct(name='lemon', price=7.0, amount=20.0, country='China', shelf_life=25)]

my_shop = Shop([8, 22], [fruits])

print(my_shop.check_amount())
print('\nПродадим 4 кг бананов и 25 кг ананасов и проверим, какие продукты заканчиваются теперь.\n')
my_shop.sell('banana', 4)
my_shop.sell('pineapple', 25)
print(my_shop.check_amount())
print('\nУзнаем график работы магазина:')
print(my_shop.working_hours)
print('\nУзнаем, работает ли магазин сейчас:')
print(my_shop.is_shop_open())
