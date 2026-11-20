from modul_cart import PIZZAS, add_to_cart
from modul_status import next_status, status_label
from modul_total import calculate_total

MIN_DELIVERY_SUM = 500


def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Нужно ввести целое число.")


def show_pizzas():
    print("\nМеню пиццерии:")
    for pizza_id, pizza in PIZZAS.items():
        print(f"  {pizza_id}. {pizza['name']:<16} {pizza['price']} руб.")


def show_cart(cart):
    if not cart:
        print("\nКорзина пуста.")
        return
    print("\nВаш заказ:")
    for pizza_id, quantity in cart.items():
        pizza = PIZZAS[pizza_id]
        print(f"  {pizza['name']:<16} {quantity} шт. x {pizza['price']} руб. = {pizza['price'] * quantity} руб.")


def checkout(cart):
    if not cart:
        print("\nСначала добавьте пиццу в корзину.")
        return cart
    choice = ask_int("\nСпособ получения (1 - доставка, 2 - самовывоз): ")
    if choice not in (1, 2):
        print("Такого способа нет.")
        return cart
    fulfillment = "delivery" if choice == 1 else "pickup"
    prices = {pizza_id: pizza["price"] for pizza_id, pizza in PIZZAS.items()}
    total = calculate_total(cart, prices, fulfillment)
    if fulfillment == "delivery" and total["subtotal"] - total["discount"] < MIN_DELIVERY_SUM:
        print(f"Минимальная сумма для доставки - {MIN_DELIVERY_SUM} руб. Добавьте пиццу или выберите самовывоз.")
        return cart

    show_cart(cart)
    print(f"Стоимость пицц: {total['subtotal']} руб.")
    print(f"Скидка:         {total['discount']} руб.")
    print(f"Доставка:       {total['delivery_fee']} руб.")
    print(f"Итого к оплате: {total['total']} руб.")

    status = "accepted"
    chain = [status_label(status, fulfillment)]
    while next_status(status, fulfillment) != status:
        status = next_status(status, fulfillment)
        chain.append(status_label(status, fulfillment))
    print("Статусы заказа: " + " -> ".join(chain))
    print("Заказ оформлен. Спасибо!")
    return {}


def main():
    cart = {}
    while True:
        print("\n1 - меню, 2 - добавить пиццу, 3 - показать заказ, 4 - оформить заказ, 0 - выход")
        action = ask_int("Выберите действие: ")
        if action == 1:
            show_pizzas()
        elif action == 2:
            pizza_id = ask_int("Номер пиццы: ")
            quantity = ask_int("Количество: ")
            try:
                cart = add_to_cart(cart, pizza_id, quantity)
                print(f"Добавлено: {PIZZAS[pizza_id]['name']}, {quantity} шт.")
            except ValueError as error:
                print("Ошибка:", error)
        elif action == 3:
            show_cart(cart)
        elif action == 4:
            cart = checkout(cart)
        elif action == 0:
            print("До свидания!")
            break
        else:
            print("Такого действия нет.")


if __name__ == "__main__":
    main()
