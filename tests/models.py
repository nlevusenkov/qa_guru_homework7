class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity
        # raise NotImplementedError

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError
        # raise NotImplementedError

    def __hash__(self):
        return hash(self.name + self.description)

class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product not in self.products:
            self.products[product] = buy_count
        else:
            self.products[product] += buy_count
        if buy_count <= 0:
            raise ValueError("Quantity must be positive")

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count
        # raise NotImplementedError

    def clear(self):
        self.products.clear()
        # raise NotImplementedError

    def get_total_price(self) -> float:
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price

        # raise NotImplementedError

    def buy(self, quantity):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, thing in self.products.items():  # перебор продуктов в корзине
            if product.quantity < thing:  # проверка наличия продукта на складе
                raise ValueError  # выброс исключения если продукта не хватает
            else:
                product.buy(thing)  # покупка продукта