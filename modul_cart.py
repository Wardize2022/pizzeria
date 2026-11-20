PIZZAS = {
    1: {"name": "Маргарита", "price": 490},
    2: {"name": "Пепперони", "price": 590},
    3: {"name": "Пять сыров", "price": 690},
    4: {"name": "Курица и грибы", "price": 620},
    5: {"name": "Овощная", "price": 550},
    6: {"name": "Барбекю", "price": 650},
}
MAX_QUANTITY = 20


def add_to_cart(cart, pizza_id, quantity):
    if pizza_id not in PIZZAS:
        raise ValueError("Пиццы с таким номером нет в меню.")
    if quantity < 1:
        raise ValueError("Количество должно быть не меньше 1.")
    new_quantity = cart.get(pizza_id, 0) + quantity
    if new_quantity > MAX_QUANTITY:
        raise ValueError(f"Можно заказать не больше {MAX_QUANTITY} пицц каждого вида.")
    new_cart = dict(cart)
    new_cart[pizza_id] = new_quantity
    return new_cart
