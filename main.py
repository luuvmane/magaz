from abc import ABC, abstractmethod
class LogMixin:
    def __repr__(self):
        attributes = ', '.join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__}: {self.__repr__()}")

class AbstractProduct(ABC, LogMixin):
    @abstractmethod
    def __str__(self):
        """Абстрактный метод для строкового представления продукта."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод для сложения продуктов."""
        pass

    @staticmethod
    @abstractmethod
    def create_product(name, description, price, quantity):
        """Абстрактный метод для создания продукта."""
        pass

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
        if not isinstance(product, AbstractProduct):
            raise TypeError("Можно добавлять только объекты типа AbstractProduct и его наследников")
        if product.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

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

    def average_price(self):
        """Метод для подсчета среднего ценника всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

class Product(AbstractProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    def __str__(self):
        """Метод для строкового представления товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):  # Проверяем типы объектов
            raise TypeError("Невозможно сложить товары разных классов")

        total_quantity = self.quantity + other.quantity
        total_price = (self.price * self.quantity + other.price * other.quantity)
        return Product.create_product("Сумма прайса техники", "Колличество товаров", total_price, total_quantity)

    @staticmethod
    def create_product(name, description, price, quantity):
        """Метод для создания продукта."""
        return Product(name, description, price, quantity)

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, storage_capacity, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.model}, {self.color}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):  # Проверяем типы объектов
            raise TypeError("Невозможно сложить товары разных классов")

        total_quantity = self.quantity + other.quantity
        total_price = (self.price * self.quantity + other.price * other.quantity)
        return Smartphone.create_product("Сумма товара", "Сумма товаров", total_price, total_quantity, "", "", "", "")

    @staticmethod
    def create_product(name, description, price, quantity, performance, model, storage_capacity, color):
        """Метод для создания продукта."""
        return Smartphone(name, description, price, quantity, performance, model, storage_capacity, color)

class Grass(Product):
    def __init__(self, name, description, price, quantity, country_of_origin, sprouting_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.sprouting_period = sprouting_period
        self.color = color

    def __str__(self):
        return f"{self.name}, {self.country_of_origin}, {self.color}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):  # Проверяем типы объектов
            raise TypeError("Невозможно сложить товары разных классов")

        total_quantity = self.quantity + other.quantity
        total_price = (self.price * self.quantity + other.price * other.quantity)
        return Grass.create_product("Сумма товара", "Сумма товаров", total_price, total_quantity, "", "", "")

    @staticmethod
    def create_product(name, description, price, quantity, country_of_origin, sprouting_period, color):
        """Метод для создания продукта."""
        return Grass(name, description, price, quantity, country_of_origin, sprouting_period, color)

category1 = Category("Электроника", "Девайсы и гаджеты")
product1 = Product.create_product("Ноутбук", "Высокопроизводительный ноутбук с SSD", 1200.50, 10)
product2 = Product.create_product("Смартфон", "Последняя модель с OLED-дисплеем", 800.99, 20)
grass_product = Grass.create_product("Трава газонная", "Зеленая трава для газона", 15.99, 50, "Россия", "Май-июнь", "Зеленый")
category1.add_product(product1)
category1.add_product(product2)
print(grass_product)
products_info = category1.get_products_info()
for info in products_info:
    print(info)

result_product = product1 + product2
print(result_product)
