# Самостоятельно познакомиться с паттернами Factory (фабрика) и Factory method (фабричный метод)
# и решить следующую задачу:
# «Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>).
# От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение:
# Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(),
# а через фабричный метод или фабрику, например factory.create_tag (name).»

# *Дополнительно:
# Реализовать возможность опциональной передачи атрибутов для тегов, т. е атрибуты могут быть
# (src для image, href для a и. т. д.) , а могут и не быть.


class Tag:
    def __init__(self, attributes_dict=None):
        """
        Описывает объект, содержащий по умолчанию название тега "tag" и атрибуты тега в виде словаря
        :param attributes_dict: Словарь с атрибутами тега, где ключ - атрибут, значение - значение.
        """
        self.tag = 'tag'
        self.attributes_dict = attributes_dict

    def get_html(self):
        """
        Формирует на основе названия тега (self.tag) и словаря атрибутами тега(не класса!) html-представление тега.
        :return: строка с html-представлением.
        """
        html_str = '<{tag}'.format(tag=self.tag)  # Создаём строку с началом html
        for k, v in self.attributes_dict.items():  # Добавляем конкатенацией атрибуты тега и их значения из словаря...
            html_str += ' {}="{}"'.format(k, v)  # ...в строку html
        html_str += '></{}>'.format(self.tag)  # Добавляем завершающую часть тега
        return html_str


class Image(Tag):
    def __init__(self, attributes_dict=None):
        super().__init__(attributes_dict)
        self.tag = 'img'  # Переопределяем родительское название тега

    def get_html(self):
        """
        Вызывает одноимённый родительский метод, и из возвращаемой им строки убирает завершающую часть тега.
        Т.е. из возвращаемого родительским методом <img></img> убирает вторую часть тега, оставляя <img>
        """
        html_str = super().get_html().replace('</{}>'.format(self.tag), '')
        return html_str


class Input(Tag):
    def __init__(self, attributes_dict=None):
        super().__init__(attributes_dict)
        self.tag = 'input'  # Переопределяем родительское название тега


class Text(Tag):
    def __init__(self, attributes_dict=None):
        super().__init__(attributes_dict)
        self.tag = 'p'  # Переопределяем родительское название тега


class Link(Tag):
    def __init__(self, attributes_dict=None):
        super().__init__(attributes_dict)
        self.tag = 'a'  # Переопределяем родительское название тега


class TagFactory:
    @staticmethod
    def create_tag(tag_name, attrs_dict):
        """
        В зависимости от переданного в словаре имени тега вызывает конструктор объекта соответствующего класса
        :param tag_name: имя тега
        :param attrs_dict: словарь атрибутов тега и их значений
        :return: объект тега
        """
        if tag_name == 'image':
            return Image(attrs_dict)
        elif tag_name == 'input':
            return Input(attrs_dict)
        elif tag_name == 'p':
            return Text(attrs_dict)
        elif tag_name == 'a':
            return Link(attrs_dict)
        elif tag_name == '':
            return Tag(attrs_dict)
        else:  # Если класс с переданным именем тега отсутствует
            some_tag = Tag(attrs_dict)   # Создаём родительский класс тега с именем тега по умолчанию (tag)
            some_tag.tag = tag_name   # Переопределяем имя по умолчанию на переданное имя тега
            return some_tag  # Так же, как и в предыдущих условиях, возвращаем объект тега


factory = TagFactory()
elements = {'image': {'src': '/src/logo.jpeg'},  # Словарь, где ключ - имя тега, а значение - словарь с атрибутами тега
            'input': {'alt': 'Подтвердить'},
            'p': {'align': 'center'},
            'a': {'href': 'www.wikipedia.com'},
            '': {},
            'script': {'async': 'sync', 'type': 'text/JavaScript', 'src': 'http://somescrypt.com/scrypt.js'}}
for tag_name, attrs in elements.items():
    print(factory.create_tag(tag_name, attrs).get_html())
