from valuesobjects.order_item_id import OrderItemId
from valuesobjects.order_id import OrderId
from valuesobjects.money import Money
from entities.product import Product

class OrderItem:
    def __init__(self, orderItemId: OrderItemId, orderId: OrderId, product: Product, quantity: int) -> None:
        self.orderItemId = orderItemId
        self.orderId = orderId
        self.product = product
        self.quantity = quantity
        self.price = product.price
        self.subtotal = self.price * self.quantity
        pass