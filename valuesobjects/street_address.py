from uuid import UUID, uuid4

class StreetAddress():
    def __init__(self,street: str, postal_code: str, city: str, id: UUID = uuid4()) -> None:
        self.street = street
        self.postal_code = postal_code
        self.city = city
        self.id = id
        pass
    
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, StreetAddress):
            return __value.id == self.id
        pass