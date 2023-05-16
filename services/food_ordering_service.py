from typing import List

from valuesobjects.customer_id import CustomerId
from valuesobjects.restaurant_id import RestaurantId
from valuesobjects.street_address import StreetAddress
from valuesobjects.order_id import OrderId

from entities.order import Order
from entities.order_item import OrderItem

class FoodOrderingService:
    def createOrder(self, customer_id: CustomerId, restaurant_id: RestaurantId, delibery_adress: StreetAddress, items: List[OrderItem], orderId: OrderId = OrderId()) -> Order:
        order = Order()
        order.initialize_order(customer_id, restaurant_id, delibery_adress, items, orderId)
        return order
    
    def payOrder(self, order: Order) -> None:
        order.pay()
        
    def validateOrder(self, order: Order) -> None:
        order.approve()
        
    def cancelOrder(self, order: Order) -> None:
        order.cancel()