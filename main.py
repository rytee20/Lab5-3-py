import unittest

from Accessories import Accessories
from Clothes import Clothes
from Shoes import Shoes


def add_element():
    print("Ввод объекта с клавиатуры\n")
    products = []

    # ввод количества продуктов
    while True:
        try:
            amount_of_products = int(input("Ведите сколько вы хотите добавить товаров, число от 1 до 10: "))
            while amount_of_products < 0 or amount_of_products > 10:
                amount_of_products = int(input("Вы ввели неверно\nВедите число от 1 до 10: "))
            break
        except ValueError:
            print("Вы ввели неверно")

    for i in range(amount_of_products):
        # выбор какй именно товар надо добавить
        while True:
            try:
                choise = int(
                    input("Вы хотите добавить одежду (нажмите 1), обувь (нажмите 2) или аксессуар (нажмите 3)? "))
                while choise > 3 or choise < 1:
                    choise = int(input(
                        "Вы ввели неверно\nВы хотите добавить одежду (нажмите 1), обувь (нажмите 2) или аксессуар (нажмите 3)? "))
                break
            except ValueError:
                print("Вы ввели неверно")
        # ввод названия
        while True:
            try:
                name = str(input("Введите название товара: "))
                break
            except ValueError:
                print("Вы ввели неверно")
        # ввод ширины
        while True:
            try:
                width = float(input("Введите ширину товара: "))
                while width <= 0.0:
                    width = int(input("Вы ввели неверно\nВведите ширину товара: "))
                break
            except ValueError:
                print("Вы ввели неверно")
        # ввод длины
        while True:
            try:
                height = float(input("Введите высоту товара: "))
                while height <= 0.0:
                    height = int(input("Вы ввели неверно\nВведите высоту товара: "))
                break
            except ValueError:
                print("Вы ввели неверно")
        # ввод глубины
        while True:
            try:
                depth = float(input("Введите глубину товара: "))
                while depth <= 0.0:
                    depth = int(input("Вы ввели неверно\nВведите глубину товара: "))
                break
            except ValueError:
                print("Вы ввели неверно")
        # ввод цены
        while True:
            try:
                price = float(input("Введите цену товара: "))
                while price <= 0.01:
                    price = int(input("Вы ввели неверно\nВведите цену товара: "))
                break
            except ValueError:
                print("Вы ввели неверно")
        # ввод количества
        while True:
            try:
                amount = int(input("Введите количество товара: "))
                while amount <= 0:
                    amount = int(input("Вы ввели неверно\nВведите количество товара: "))
                break
            except ValueError:
                print("Вы ввели неверно")

        if choise == 1:  # если выбрана одежда
            # ввод типа
            while True:
                try:
                    type_of_clothes = str(
                        input("Введите тип одежды (shirt или dress или skirt ли pants или outerwear): "))
                    while type_of_clothes != "shirt" and type_of_clothes != "dress" and \
                            type_of_clothes != "skirt" and type_of_clothes != "pants" and \
                            type_of_clothes != "outerwear":
                        type_of_clothes = str(input("Вы ввели неверно\nВведите тип одежды "
                                                    "(shirt или dress или skirt ли pants или outerwear): "))
                    break
                except ValueError:
                    print("Вы ввели неверно")
            # ввод бренда
            while True:
                try:
                    brand = str(input("Введите бренд одежды: "))
                    break
                except ValueError:
                    print("Вы ввели неверно")
            # ввод пола
            while True:
                try:
                    sex = str(input("Введите пол одежды (man или woman или unisex): "))
                    while sex != "man" and sex != "woman" and sex != "unisex":
                        sex = str(input("Вы ввели неверно\nВведите пол одежды (man или woman или unisex): "))
                    break
                except ValueError:
                    print("Вы ввели неверно")
            # ввод размера
            while True:
                try:
                    size = int(input("Введите размер одежды: "))
                    while 40 > size or size > 58:
                        size = int(input("Вы ввели неверно\nВведите размер одежды: "))
                    break
                except ValueError:
                    print("Вы ввели неверно")

            # добавляем элемент
            products.append(Clothes(size, type_of_clothes, brand, sex, name, width, height, depth, price, amount))

        elif choise == 2:  # если выбрана обувь
            # ввод типа
            while True:
                try:
                    type_of_shoes = str(input("Введите тип обуви (high boots или high-heels или sneakers или other): "))
                    while type_of_shoes != "high boots" and type_of_shoes != "high-heels" and \
                            type_of_shoes != "sneakers" and type_of_shoes != "other":
                        type_of_shoes = str(input("Вы ввели неверно\nВведите тип обуви "
                                                  "(high boots или high-heels или sneakers или other): "))
                    break
                except ValueError:
                    print("Вы ввели неверно")
            # ввод бренда
            while True:
                try:
                    brand = str(input("Введите бренд обуви: "))
                    break
                except ValueError:
                    print("Вы ввели неверно")
            # ввод пола
            while True:
                try:
                    sex = str(input("Введите пол обуви (man или woman или unisex): "))
                    while sex != "man" and sex != "woman" and sex != "unisex":
                        sex = str(input("Вы ввели неверно\nВведите пол обуви (man или woman или unisex): "))
                    break
                except ValueError:
                    print("Вы ввели неверно")
            # ввод размера
            while True:
                try:
                    size = int(input("Введите размер обуви: "))
                    while 34 > size or size > 45:
                        size = int(input("Вы ввели неверно\nВведите размер обуви: "))
                    break
                except ValueError:
                    print("Вы ввели неверно")

            # возвращаем объект
            products.append(Shoes(size, type_of_shoes, brand, sex, name, width, height, depth, price, amount))

        else:  # если выбран аксессуар
            # ввод типа
            while True:
                try:
                    type_of_accessory = str(input("Введите тип аксессуара (hat или bag или belt или other): "))
                    while type_of_accessory != "hat" and type_of_accessory != "bag" and \
                            type_of_accessory != "belt" and type_of_accessory != "other":
                        type_of_accessory = str(input("Вы ввели неверно\nВведите тип "
                                                      "аксессуара (hat или bag или belt или other): "))
                    break
                except ValueError:
                    print("Вы ввели неверно")
                # ввод бренда
                while True:
                    try:
                        brand = str(input("Введите бренд аксессуара: "))
                        break
                    except ValueError:
                        print("Вы ввели неверно")
                # ввод пола
                while True:
                    try:
                        sex = str(input("Введите пол аксессуара (man или woman или unisex): "))
                        while sex != "man" and sex != "woman" and sex != "unisex":
                            sex = str(input("Вы ввели неверно\nВведите пол аксессуара (man или woman или unisex): "))
                        break
                    except ValueError:
                        print("Вы ввели неверно")

            # возвращаем объект
            products.append(Accessories(type_of_accessory, brand, sex, name, width, height, depth, price, amount))

    return products


def read_from_file(products_default):
    products = []
    read_products = []
    count_lines = 0

    end_of_file = 'no'
    try:
        file = open('products.txt', 'r', encoding='utf-8')  # открываем файл
    except IOError:
        print("Не удалось открыть файл")
        return add_element()
    else:
        with file:
            while end_of_file != '':
                end_of_file = file.readline()  # считываем айпи адрес
                if end_of_file == '':  # как только пустая строка
                    break  # выходим из цикла
                else:
                    count_lines += 1
                products.append(list(end_of_file.split(';')))  # записываем в список
            file.close()

    if count_lines == 0:
        print("В файле пусто")
        return add_element()

    for i in range(len(products)):
        # преобразование и проверка выбора категории товара
        while True:
            try:
                products[i][0] = int(products[i][0])
                if products[i][0] < 1 or products[i][0] > 3:
                    print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                    return products_default
                break
            except ValueError:
                print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                return products

        # общее
        # проверка ширины
        while True:
            try:
                products[i][1] = float(products[i][1])
                if products[i][1] <= 0.0:
                    print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                    return products_default
                break
            except ValueError:
                print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                return products_default
        # проверка высоты
        while True:
            try:
                products[i][2] = float(products[i][2])
                if products[i][2] <= 0.0:
                    print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                    return products_default
                break
            except ValueError:
                print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                return products_default
        # проверка глубины
        while True:
            try:
                products[i][3] = float(products[i][3])
                if products[i][3] <= 0.0:
                    print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                    return products_default
                break
            except ValueError:
                print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                return products_default
        # ввод цены
        while True:
            try:
                products[i][4] = float(products[i][4])
                if products[i][4] <= 0.01:
                    print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                    return products_default
                break
            except ValueError:
                print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                return products_default
        # ввод количества
        while True:
            try:
                products[i][5] = int(products[i][5])
                if products[i][5] <= 0:
                    print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                    return products_default
                break
            except ValueError:
                print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                return products_default
        #
        if products[i][6] != "woman" and products[i][6] != "man" and \
                products[i][6] != "unisex":
            print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
            return products_default

        if products[i][0] == 1:  # если это одежда
            # преобразовние и проверка размера
            while True:
                try:
                    products[i][7] = int(products[i][7])
                    if products[i][7] < 40 or products[i][7] > 58:
                        print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                        return products_default
                    break
                except ValueError:
                    print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                    return products_default
            # проверка типа одежды
            if products[i][8] != "shirt" and products[i][8] != "dress" and \
                    products[i][8] != "skirt" and products[i][8] != "pants" and \
                    products[i][8] != "outerwear":
                print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                return products_default
            products[i][10] = products[i][10][:-1]
            read_products.append(
                Clothes(products[i][7], products[i][8], products[i][9], products[i][6], products[i][10],
                        products[i][1], products[i][2], products[i][3], products[i][4], products[i][5]))


        elif products[i][0] == 2:  # если это обувь
            # преобразовние и проверка размера
            while True:
                try:
                    products[i][7] = int(products[i][7])
                    if products[i][7] < 34 or products[i][7] > 45:
                        print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                        return products_default
                    break
                except ValueError:
                    print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                    return products_default
            # проверка типа обуви
            if products[i][8] != "high boots" and products[i][8] != "high-heels" and \
                    products[i][8] != "sneakers" and products[i][8] != "other":
                print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                return products_default
            products[i][10] = products[i][10][:-1]
            read_products.append(Shoes(products[i][7], products[i][8], products[i][9], products[i][6], products[i][10],
                                       products[i][1], products[i][2], products[i][3], products[i][4], products[i][5]))


        elif products[i][0] == 3:
            # проверка типа аксессуаров
            if products[i][7] != "hat" and products[i][7] != "bag" and \
                    products[i][7] != "belt" and products[i][7] != "other":
                print("Ошибка в файле в строке ", i + 1, ", не удалось его корректно прочесть")
                return products_default
            products[i][9] = products[i][9][:-1]
            read_products.append(
                Accessories(products[i][7], products[i][8], products[i][6], products[i][9], products[i][1],
                            products[i][2], products[i][3], products[i][4], products[i][5]))

    return read_products


def save_to_file(products_to_write):
    f = open('products.txt', 'w', encoding='utf-8')
    for product in products_to_write:
        if isinstance(product, Clothes):
            f.write(
                str(1) + ';' + str(product.width) + ';' + str(product.height) + ';' + str(product.depth) + ';' + str(
                    product.price) + ';' + str(product.amount) + ';'
                + product.sex + ';' + str(
                    product.size) + ';' + product.type_of_clothes + ';' + product.brand + ';' + product.name + '\n')
        elif isinstance(product, Shoes):
            f.write(
                str(2) + ';' + str(product.width) + ';' + str(product.height) + ';' + str(product.depth) + ';' + str(
                    product.price) + ';' + str(product.amount) + ';'
                + product.sex + ';' + str(
                    product.size) + ';' + product.type_of_shoes + ';' + product.brand + ';' + product.name + '\n')
        else:
            f.write(
                str(3) + ';' + str(product.width) + ';' + str(product.height) + ';' + str(product.depth) + ';' + str(
                    product.price) + ';' + str(product.amount) + ';'
                + product.sex + ';' + product.type_of_accessory + ';' + product.brand + ';' + product.name + '\n')
    f.close()


if __name__ == '__main__':
    # для примера
    products_we_have = []
    products_we_have = read_from_file(products_we_have)
    for product in products_we_have:
        product.display_info()

    save_to_file(products_we_have)

    product_for_test_1 = Clothes(48, "shirt", "O'stin", "man", "White shirt", 20, 15, 0.7, 1999, 45)
    product_for_test_1.total_price()
    unittest.main()
