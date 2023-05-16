class Money():
    def __init__(self, value: float = 0.0) -> None:
        self.value = value
        self.currency = "EUR"
        
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Money):
            return self.value == __value.value
        return False
    
    def __add__(self, __value: object):
        if isinstance(__value, Money):
            return Money(self.value + __value.value)
        if isinstance(__value, float):       
            return Money(self.value + __value)
        return NotImplementedError
    
    def __mul__(self, __value: object):
        if isinstance(__value, Money):
            return Money(self.value * __value.value)
        if isinstance(__value, float) or isinstance(__value, int):
            return Money(float(self.value * __value))
    
    def __str__(self) -> str:
        return "{:,.2f} {}".format(self.value, self.currency)