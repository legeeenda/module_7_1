class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        """Считывает и возвращает все продукты из файла."""
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ''  

    def add(self, *products):
        """Добавляет новые продукты в файл, если их еще нет."""
        existing_products = self.get_products().splitlines()

        for product in products:
            product_str = str(product)
            product_name = product.name

            if any(product_name in p for p in existing_products):
                print(f'Продукт {product_str} уже есть в магазине')
            else:

                with open(self.__file_name, 'a', encoding='utf-8') as file:
                    file.write(product_str + '\n')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  

s1.add(p1, p2, p3)

print(s1.get_products()) 
