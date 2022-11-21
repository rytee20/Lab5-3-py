import datetime
from Product import Product, toFixed


class Clothes(Product):
    #  конструктор
    def __init__(self, size, type_of_clothes, brand, sex, name, width, height, depth, price, amount):
        Product.__init__(self, name, width, height, depth, price, amount)
        self.__size = size  # размер
        self.__typeOfClothes = type_of_clothes  # тип
        self.__brand = brand  # бренд
        self.__sex = sex  # пол

    # размер
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) and 40 <= size <= 58:
            self.__size = size
        else:
            print("Неверный ввод")

    # тип
    @property
    def type_of_clothes(self):
        return self.__typeOfClothes

    @type_of_clothes.setter
    def type_of_clothes(self, type_of_clothes):
        if (isinstance(type_of_clothes, str) and (
                type_of_clothes.lower == "shirt" or type_of_clothes == "dress" or
                type_of_clothes.lower == "skirt" or type_of_clothes == "pants" or
                type_of_clothes.lower == "outerwear")):
            self.__typeOfClothes = type_of_clothes
        else:
            print("Неверный ввод")

    # бренд
    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand
        else:
            print("Неверный ввод")

    # пол
    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if isinstance(sex, str) and (sex == "man" or sex == "woman" or sex == "unisex"):
            self.__sex = sex
        else:
            print("Неверный ввод")

    #  переопределение вывода
    def display_info(self):
        Product.display_info(self)
        print(" Тип: ", self.type_of_clothes, "\n Размер: ", self.size, "\n Бренд: ", self.brand, "\n Пол: ", self.sex)

    # переопределение метода вычислющего уену со скидкой
    def total_price(self, discount):
        if datetime.datetime.now().day == 8 and datetime.datetime.now().mounth == 3:  # если сегодня 8 марта
            # то на женские товары действут скидка 30%
            print("Сегодня международный женский день, "
                  "дествует скидка на все товары для женщин 30%, скидки не суммируются")
            return toFixed((self.price * (100-30)) / 100,2)
        elif datetime.datetime.now().month == 8:  # если сегодня август, то скидка не верхнюю одежду 15%
            print(
                "Сегодня август, действует скидка на верхнюю одежду 15%, скидки не суммируются")
            return toFixed((self.price * (100-15)) / 100,2)
        else:  # если ничего из этого то тогда дествуетобычная скидка покупателя
            return toFixed((self.price * (100-discount)) / 100,2)
