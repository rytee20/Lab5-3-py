from Product import Product


class Shoes(Product):
    # конструктор
    def __init__(self, size, type_of_shoes, brand, sex, name, width, height, depth, price, amount):
        Product.__init__(self, name, width, height, depth, price, amount)
        self.__size = size  # размер
        self.__typeOfShoes = type_of_shoes  # тип
        self.__brand = brand  # бренд
        self.__sex = sex  # пол

    #размер
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) and 34 <= size <= 45:  #проверка
            self.__size = size
        else:
            print("Неверный ввод")

    # тип
    @property
    def type_of_shoes(self):
        return self.__typeOfShoes

    @type_of_shoes.setter
    def type_of_shoes(self, type_of_shoes):
        if (isinstance(type_of_shoes, str) and (
                type_of_shoes == "high boots" or type_of_shoes == "high-heels" or
                type_of_shoes == "sneakers" or type_of_shoes == "other")):
            self.__typeOfShoes = type_of_shoes
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

    # переопределение вывода
    def display_info(self):
        Product.display_info(self)
        print(" Тип: ", self.type_of_shoes, "\n Размер: ", self.size, "\n Бренд: ", self.brand, "\n Пол: ", self.sex)
