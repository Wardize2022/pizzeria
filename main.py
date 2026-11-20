from modul_cart import PIZZAS, add_to_cart
from modul_status import next_status, status_label


def main():
    cart = add_to_cart({}, 1, 2)
    print("Корзина:", cart)
    print("Статус заказа:", status_label(next_status("accepted", "delivery"), "delivery"))


if __name__ == "__main__":
    main()
