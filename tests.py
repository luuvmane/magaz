from main import Category, Product
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

def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Product description"
    assert sample_product.price == 10.99
    assert sample_product.quantity == 5

def test_count_products(sample_product, sample_category):
    sample_category.add_product(sample_product)  # Добавляем продукт в категорию
    assert len(sample_category.get_products_info()) == 1  # Проверяем количество продуктов в категории

# Запустить тесты
if __name__ == "__main__":
    pytest.main()
