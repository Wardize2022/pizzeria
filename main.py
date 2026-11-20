from modul_cart import PIZZAS, add_to_cart
from modul_status import next_status, status_label
from modul_total import calculate_total


def main():
    cart = add_to_cart({}, 1, 2)
    print("Корзина:", cart)
    print("Статус заказа:", status_label(next_status("accepted", "delivery"), "delivery"))
    prices = {pizza_id: pizza["price"] for pizza_id, pizza in PIZZAS.items()}
    print("Стоимость:", calculate_total(cart, prices, "delivery"))


if __name__ == "__main__":
    main()
