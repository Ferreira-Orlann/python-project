from services.food_ordering_service import FoodOrderingService

from valuesobjects.customer_id import CustomerId
from valuesobjects.restaurant_id import RestaurantId
from valuesobjects.street_address import StreetAddress
from valuesobjects.money import Money
from valuesobjects.order_id import OrderId
from valuesobjects.order_item_id import OrderItemId

from entities.order_item import OrderItem
from entities.product import Product

service = FoodOrderingService()

id = OrderId()
order = service.createOrder(CustomerId(), 
    RestaurantId(), 
    StreetAddress("422", "Rue George", "Tours"), 
    [OrderItem(OrderItemId(), 
        id, 
        Product("food", Money(2.99)),
        3)], 
    id)
service.payOrder(order)
service.validateOrder(order)

print(order)