def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


class Product():
    #  конструктоор
    def __init__(self, name, width, height, depth, price, amount):
        self.__name = name  # название
        self.__width = width  # ширина
        self.__height = height  # высота
        self.__depth = depth  # глубина
        self.__price = price  # цена
        self.__amount = amount  # количество

    # название
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):  # проверка на тип
            self.__name = name
        else:
            print("Неверный ввод")

    # ширина
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if isinstance(width, float) and width > 0.0:  # проверка на тип и положительность
            self.__width = width
        else:
            print("Неверный ввод")

    # высота
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, float) and height > 0.0:  # проверка на тип и положительность
            self.__height = height
        else:
            print("Неверный ввод")

    # глубина
    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth):
        if isinstance(depth, float) and depth > 0.0:  # проверка на тип и положительность
            self.__depth = depth
        else:
            print("Неверный ввод")

    # цена за штуку
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, int) and price >= 0.01:  # проверка на тип и цена должна быть >0.01
            self.__price = price
        else:
            print("Неверный ввод")

    # количество
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int) and amount > 0:  # проверка на тип и положительность числа
            self.__amount = amount
        else:
            print("Неверный ввод")

    # вывод
    def display_info(self):
        print("\n Название товара: ", self.name, "\n Габариты: ", self.width, "x", self.height, "x", self.depth,
              "\n Цена за штуку: ", self.price, "\n Количество товара в наличии: ", self.amount)

    # метод вычисления итоговой цены со скидкой
    def total_price(self, discount):
        return toFixed((self.__price * (100-discount)) / 100, 2)

    # метод, определяющий количество данного товара, который пожет поместится в заданную коробку
    def fit_in_a_box(self, box_width, box_height, box_depth):
        if ((box_width < self.width and box_width < self.height and box_width < self.depth)
                or (box_height < self.width and box_height < self.height and box_height < self.depth)
                or (box_depth < self.width and box_depth < self.height and box_depth < self.depth)):
            return 0
        else:
            box_volume = box_width * box_height * box_depth
            return box_volume // (self.width * self.height * self.depth)

    # перегрузка оператора сложения
    def __add__(self, other):
        return self.__price + other.__price
