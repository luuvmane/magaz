class Category:
    total_categories = 0
    unique_products = set()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product):
        """Метод для добавления товара в категорию."""
        self.__products.append(product)
        Category.unique_products.add(product.name)

    def get_products(self):
        """Геттер для получения списка товаров в категории."""
        return self.__products

    def get_products_info(self):
        """Геттер для получения информации о товарах в категории."""
        products_info = []
        for product in self.__products:
            products_info.append(str(product))
        return products_info

    def __len__(self):
        """Магический метод для получения количества товаров в категории."""
        return len(self.__products)

    def __str__(self):
        """Магический метод для строкового представления категории."""
        return f"{self.name}, количество продуктов: {len(self)} шт."


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @staticmethod
    def create_product(name, description, price, quantity):
        """Статический метод для создания товара и возвращения объекта товара."""
        return Product(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для цены товара."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены товара."""
        if new_price >= 0:
            self.__price = new_price
        else:
            raise ValueError("Цена не может быть отрицательной")

    @price.deleter
    def price(self):
        """Делитер для цены товара."""
        del self.__price

    def __str__(self):
        """Магический метод для строкового представления товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            total_quantity = self.quantity + other.quantity
            total_price = (self.price * self.quantity + other.price * other.quantity)
            return Product("Сумма товаров", "Сумма товаров", total_price, total_quantity)
        else:
            raise TypeError("Неверный тип операнда")


category1 = Category("Электроника", "Девайсы и гаджеты")
product1 = Product("Ноутбук", "Высокопроизводительный ноутбук с SSD", 1200.50, 10)
product2 = Product("Смартфон", "Последняя модель с OLED-дисплеем", 800.99, 20)

category1.add_product(product1)
category1.add_product(product2)

products_info = category1.get_products_info()
for info in products_info:
    print(info)

result_product = product1 + product2
print( result_product)
