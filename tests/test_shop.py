
"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from tests.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(100) == True
        assert product.check_quantity(1000) == True
        assert product.check_quantity(10000) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(500)
        assert product.quantity == 500

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1500)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        assert cart.products[product] == 5
        with pytest.raises(ValueError):
            cart.add_product(product, -5)

    def test_remove_product(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_cart(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        cart.clear()
        assert cart not in cart.products

    def test_get_total_price(self, product):
        cart = Cart()
        cart.add_product(product, 5)
        assert cart.get_total_price() == 500

    def test_buy_product(self, product):
            cart = Cart()
            cart.add_product(product, 5)
            original_quantity = product.quantity
            cart.buy(5)
            assert product.quantity == original_quantity - 5