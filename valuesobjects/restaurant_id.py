from uuid import UUID, uuid4

class RestaurantId:
    def __init__(self, value: UUID = uuid4()) -> None:
        self.value = value
        pass
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, RestaurantId):
            return self.value == __value.value
        return False