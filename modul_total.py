DISCOUNT_PERCENT = 10
DISCOUNT_FROM_COUNT = 3
DELIVERY_FEE = 150
FREE_DELIVERY_FROM = 1000


def count_pizzas(cart):
    count = 0
    for quantity in cart.values():
        count += quantity
    return count


def calculate_subtotal(cart, prices):
    subtotal = 0
    for pizza_id, quantity in cart.items():
        subtotal += prices[pizza_id] * quantity
    return subtotal


def calculate_discount(subtotal, pizzas_count, fulfillment):
    if fulfillment == "pickup" or pizzas_count >= DISCOUNT_FROM_COUNT:
        return subtotal * DISCOUNT_PERCENT // 100
    return 0


def calculate_total(cart, prices, fulfillment):
    if fulfillment not in ("delivery", "pickup"):
        raise ValueError("Неизвестный способ получения заказа.")
    subtotal = calculate_subtotal(cart, prices)
    discount = calculate_discount(subtotal, count_pizzas(cart), fulfillment)
    net = subtotal - discount
    if fulfillment == "delivery" and net < FREE_DELIVERY_FROM:
        delivery_fee = DELIVERY_FEE
    else:
        delivery_fee = 0
    return {"subtotal": subtotal, "discount": discount, "delivery_fee": delivery_fee, "total": net + delivery_fee}


if __name__ == "__main__":
    test_prices = {1: 490, 2: 590, 3: 690}
    test_cart = {1: 2, 3: 1}
    delivery = calculate_total(test_cart, test_prices, "delivery")
    pickup = calculate_total({2: 1}, test_prices, "pickup")
    small = calculate_total({1: 1}, test_prices, "delivery")
    print("Доставка, три пиццы:", delivery)
    print("Самовывоз, одна пицца:", pickup)
    print("Доставка, одна пицца:", small)
