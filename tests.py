from main import Category, Product,Smartphone, Grass
import pytest

# Тесты для класса Category
@pytest.fixture
def sample_category():
    Category.total_categories = 0  # Сброс счетчика перед каждым тестом
    Category.unique_products.clear()  # Очистка множества перед каждым тестом
    return Category("Test Category", "Test description")

def test_category_initialization(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test description"
    assert len(sample_category.get_products()) == 0

def test_count_categories(sample_category):
    assert Category.total_categories == 1

# Тесты для класса Product
@pytest.fixture
def sample_product():
    return Product("Test Product", "Product description", 10.99, 5)

# Тесты для класса Smartphone
def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Product description"
    assert sample_product.price == 10.99
    assert sample_product.quantity == 5

def test_count_products(sample_product, sample_category):
    smartphone = Smartphone("iPhone 13", "Latest iPhone model", 999.99, 50, "High", "13", "256GB", "Blue")
    sample_category.add_product(smartphone)  # Использование объекта Smartphone
    assert len(sample_category.get_products_info()) == 1
def test_smartphone_initialization():
    smartphone = Smartphone("iPhone 13", "Latest iPhone model", 999.99, 50, "High", "13", "256GB", "Blue")
    assert smartphone.name == "iPhone 13"
    assert smartphone.description == "Latest iPhone model"
    assert smartphone.price == 999.99
    assert smartphone.quantity == 50
    assert smartphone.performance == "High"
    assert smartphone.model == "13"
    assert smartphone.storage_capacity == "256GB"
    assert smartphone.color == "Blue"

# Тесты для класса Grass
def test_grass_initialization():
    grass = Grass("Kentucky Bluegrass", "Premium lawn grass seeds", 5.99, 100, "USA", "2 weeks", "Green")
    assert grass.name == "Kentucky Bluegrass"
    assert grass.description == "Premium lawn grass seeds"
    assert grass.price == 5.99
    assert grass.quantity == 100
    assert grass.country_of_origin == "USA"
    assert grass.sprouting_period == "2 weeks"
    assert grass.color == "Green"

# Запустить тесты
if __name__ == "__main__":
    pytest.main()
