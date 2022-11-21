import datetime
from Product import Product, toFixed


class Accessories(Product):
    #  конструктор
    def __init__(self, type_of_accessory, brand, sex, name, width, height, depth, price, amount):
        Product.__init__(self, name, width, height, depth, price, amount)
        self.__typeOfAccessory = type_of_accessory
        self.__brand = brand
        self.__sex = sex

    # тип
    @property
    def type_of_accessory(self):
        return self.__typeOfAccessory

    @type_of_accessory.setter
    def type_of_accessory(self, type_of_accessory):
        if (isinstance(type_of_accessory, str) and (
                type_of_accessory == "hat" or type_of_accessory == "bag" or
                type_of_accessory == "belt" or type_of_accessory == "other")):
            self.__typeOfAccessory = type_of_accessory
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
        print(" Тип: ", self.type_of_accessory, "\n Бренд: ", self.brand, "\n Пол: ", self.sex)

    # переопределение метода вычислющего уену со скидкой
    def total_price(self, discount):
        if datetime.datetime.now().day == 8:  # если сегодня 8 число любого месяца
            # то на все аксессуары действует скидка 10%, которая не суммируется со скидкой покупателя
            print("Сегодня дествует скидка на все аксессуары 10%, скидки не суммируются")
            return toFixed((self.price * (100-30)) / 100,2)
        else:  # если ничего из этого то тогда дествует обычная скидка покупателя
            return toFixed((self.price * (100-discount)) / 100,2)
