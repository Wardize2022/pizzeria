STATUSES = {
    "accepted": "Принят",
    "cooking": "Готовится",
    "ready": "Передан в доставку",
    "on_way": "Курьер в пути",
    "delivered": "Доставлен",
}
PICKUP_LABELS = {"ready": "Готов к выдаче", "delivered": "Выдан"}


def next_status(status, fulfillment):
    steps = ["accepted", "cooking", "ready", "on_way", "delivered"]
    if fulfillment == "pickup":
        steps.remove("on_way")
    if status not in steps:
        raise ValueError("Неизвестный статус заказа.")
    if status == "delivered":
        return status
    return steps[steps.index(status) + 1]


def status_label(status, fulfillment):
    if fulfillment == "pickup" and status in PICKUP_LABELS:
        return PICKUP_LABELS[status]
    return STATUSES[status]
