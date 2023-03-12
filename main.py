import hashlib
import random


class IdCounter:
    def __init__(self):
        self._current_id = 0

    def _increment_id(self):
        self._current_id += 1

    @property
    def current_id(self):
        return self._current_id

    def get_new_id(self):
        self._increment_id()
        return self.current_id
    # @classmethod
    # def get_id(cls) -> int:
    #     cls.id_ += 1
    #     return cls.id_


class Password:
    """
    Класс Пароли
    """
    # def __init__(self, password: str) -> None:
    #     self.password = None
    #     self._init_password(password)

    @staticmethod
    def _init_password(password) -> None:
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть типа str")
        if len(password) < 8:
            raise ValueError("Длина пароля должна быть не менее 8 символов")
        if not password.isalnum():
            raise ValueError("Пароль должены состоять из букв и цифр")
        # self.password = password
        return True

    @classmethod
    def get(cls, password: str):
        if cls._init_password(password):
            hash_password = hashlib.sha256(password.encode()).hexdigest()
            return hash_password
        raise TypeError("Пароль должен быть строкой")

    # def check(self, password, ) -> bool:
    #     if hashlib.sha256(self.password.encode()).hexdigest() == self.get():
    #         return True
    #     return False


class Product:
    """
    Класс Продукты
    """
    _counter = IdCounter()

    def __init__(self, name, price, rating) -> None:
        self._id = self._counter.get_new_id()
        self._name = None
        self.price = price
        self.rating = rating
        self._init_name(name)

    # @property
    # def id(self) -> int:
    #     return self._id

    def _init_name(self, name) -> None:
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> (int, float):
        return self._price

    @price.setter
    def price(self, price) -> None:
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if price < 1:
            raise ValueError("Цена должны быть положительной")
        self._price = price

    @property
    def rating(self) -> (int, float):
        return self._rating

    @rating.setter
    def rating(self, rating) -> None:
        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг должен быть типа int или float")
        if rating < 0:
            raise ValueError("Рейтинг должен быть больше или равен 0")
        self._rating = rating

    def __str__(self) -> str:
        return f"{self._id}_{self._name}"

    def __repr__(self) -> str:
        return f"ID {self._id}: {self.__class__.__name__}({self.name}, {self.price}, {self.rating})"


class Cart:
    """
    Класс Корзина
    """
    def __init__(self):
        self.product_list = []

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError()
        self.product_list.append(product)

    def delete_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError()
        self.product_list.remove(product)

    def quantity_product(self):
        count = 0
        for _ in self.product_list:
            count += 1
        return count

    def change_product(self, product: Product, index) -> None:
        if not isinstance(product, Product):
            raise TypeError()
        self.product_list[index] = product

    def __repr__(self):
        return f"{self.product_list}"


class User:
    """
    Класс Юзер
    """
    _counter = IdCounter()

    def __init__(self, username: str, password: str) -> None:
        self._id = self._counter.get_new_id()
        self.__password = Password.get(password)
        self._username = None
        self._init_username(username)
        self.cart = Cart()

    def _init_username(self, username: str) -> None:
        if not isinstance(username, str):
            raise TypeError("Имя должно быть типа str")
        if len(username) < 3:
            raise ValueError("Имя должно содержать более 3 символов")
        self._username = username

    def get_cart(self):
        return self.cart

    def __str__(self) -> str:
        return f"ID Пользователя: {self._id}, Имя: {self._username}, Пароль: 'password1'"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._id}, username={self._username}, password='password1')"


def product_generator():
    product_name = ['Арбуз', 'Дыня', 'Вишня', 'Виноград', 'Апельсин', 'Яблоко', 'Груша', 'Персик', 'Банан', 'Мандарин']
    product_price = [150, 200, 183, 124, 211, 300, 99]
    product_rating = [1, 2, 3, 4, 5]
    name = random.choice(product_name)
    price = random.choice(product_price)
    rating = random.choice(product_rating)

    return Product(name, round(float(price), 2), round(float(rating), 2))


class Store:
    """
    Класс Магазин
    """
    def __init__(self):
        username = input("Введите имя: ")
        password = input("Введите пароль: ")
        self.user = User(username, Password.get(password))

    def add_to_cart(self):
        self.user.cart.add_product(product_generator())

    def check_cart(self):
        return self.user.get_cart()


if __name__ == '__main__':
    shop = Store()
    print(shop.user)
    print(shop.check_cart())
    shop.add_to_cart()
    print(shop.check_cart())
    shop2 = Store()
    print(shop2.user)
    print(shop2.check_cart())
    shop2.add_to_cart()
    print(shop2.check_cart())
    shop2.add_to_cart()
    print(shop2.check_cart())
