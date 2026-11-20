from modul_cart import PIZZAS, add_to_cart


def main():
    cart = add_to_cart({}, 1, 2)
    print("Корзина:", cart)


if __name__ == "__main__":
    main()
