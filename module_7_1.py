class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self._read_existing_products()

        for new_p in products:
            found = False
            for i in range(len(existing_products)):
                existing = existing_products[i]
                if existing.name == new_p.name and existing.category == new_p.category:
                    existing.weight += new_p.weight
                    print(f'Продукт {new_p.name} уже был в магазине, его общий вес теперь равен {existing.weight}')
                    found = True
                    break
            if not found:
                existing_products.append(new_p)
                print(new_p)

        self._write_products(existing_products)

    def _read_existing_products(self):
        try:
            with open(self.__file_name, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            return []
        existing_products = []
        for line in content.split('\n'):
            line = line.strip()
            if not line:
                continue
            parts = line.split(', ')
            if len(parts) != 3:
                continue
            name, weight_str, category = parts
            try:
                weight = float(weight_str)
            except ValueError:
                continue
            existing_products.append(Product(name, weight, category))
        return existing_products

    def _write_products(self, products):
        with open(self.__file_name, 'w') as f:
            for p in products:
                f.write(f"{p}\n")


#Пример из задания
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())

''' В примере в задании в пукте "Вывод на консоль:" явно ошибка. Примере работы программы должен вывести в консоль список продуктов из файла, а в выводе на консоль указан список добавляемых товаров и строка "Продукт Potato уже был в магазине, его общий вес теперь равен 56.0" т.к. этот продукт уже есть, поэтому я вывел и то и другое:
Potato, 50.5, Vegetables
Spaghetti, 3.4, Groceries
Продукт Potato уже был в магазине, его общий вес теперь равен 56.0
Potato, 56.0, Vegetables
Spaghetti, 3.4, Groceries'''