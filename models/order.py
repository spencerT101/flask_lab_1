"""Online Pizza Shop."""
class Order:
    def __init__(self, customer_name, order_date, quantity, pizza_type, base_type, size):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.pizza_type = pizza_type
        self.base_type = base_type
        self.size = size
        self.description = f"{self.quantity} x {self.size} {self.pizza_type} ({self.base_type}) ordered at ({self.order_date})"

        """Dave: 2 x extra large Meat Feast (deep pan) ordered at order_date"""