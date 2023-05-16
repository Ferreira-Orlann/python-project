from typing import List

from valuesobjects.customer_id import CustomerId
from valuesobjects.restaurant_id import RestaurantId
from valuesobjects.street_address import StreetAddress
from valuesobjects.money import Money
from valuesobjects.order_id import OrderId
from valuesobjects.tracking_id import TrackingId
from valuesobjects.order_status import OrderStatus

from entities.order_item import OrderItem

class Order():
    def initialize_order(self, customer_id: CustomerId, restaurant_id: RestaurantId, delibery_adress: StreetAddress, items: List[OrderItem], orderId : OrderId = OrderId()) -> None:
        self.order_id = orderId
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.delibery_adress = delibery_adress
        self.items = items
        self.price = Money()
        for i in self.items:
            self.price += i.subtotal
        self.trackingId = TrackingId()
        self.order_status = OrderStatus()
        self.failure_messages = ["Failure"]
    
    def validate_order(self):
        if self.order_id is None:
            raise ValueError()
        if self.customer_id is None:
            raise ValueError()
        if self.restaurant_id is None:
            raise ValueError()
        if self.delibery_adress is None:
            raise ValueError()
        if self.items is None:
            raise ValueError()
        if self.price is None:
            raise ValueError()
        if self.trackingId is None:
            raise ValueError()
        if self.order_status is None:
            raise ValueError()
        if self.failure_messages is None:
            raise ValueError()
        for i in self.items:
            self.price += i.subtotal
        return self
        
    def pay(self):
        self.order_status.Pay()
    
    def approve(self):
        self.order_status.Approve()
        
    def cancel(self, failure_messages: List[str] = ["Cancel"]) -> None:
        self.order_status.Cancel()