"""Online Pizza Shop."""
class Order:
    def __init__(self, customer_name, order_date, quantity, pizza_type, base_type, size):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.pizza_type = pizza_type
        self.base_type = base_type
        self.size = size