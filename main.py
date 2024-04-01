class Category:
    total_categories = 0
    unique_products = set()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        Category.unique_products.add(product.name)

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

category1 = Category("Электроника", "Девайсы и гаджеты")
category2 = Category("Одежда", "Модный наряд")

product1 = Product("Ноутбук", "Высокопроизводительный ноутбук с SSD", 1200.50, 10)
product2 = Product("Смартфон", "Последняя модель с OLED-дисплеем", 800.99, 20)

category1.add_product(product1)
category1.add_product(product2)

print("Всего категорий:", Category.total_categories)
print("Уникальные продукты:", len(Category.unique_products))
