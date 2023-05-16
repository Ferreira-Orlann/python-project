from statemachine import StateMachine, State

class OrderStatus(StateMachine):
    PENDING = State(initial=True)
    PAID = State()
    APPROVED = State()
    CANCELLED = State()
    
    Pay = PENDING.to(PAID)
    Approve = PAID.to(APPROVED)
    Cancel = PENDING.to(CANCELLED) | PAID.to(CANCELLED)