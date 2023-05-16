from valuesobjects.customer_id import CustomerId

class Customer():
    def __init__(self, cuustomer_id: CustomerId, first_name: str, last_name: str) -> None:
        self.cuustomer_id = cuustomer_id
        self.first_name = first_name
        self.last_name = last_name