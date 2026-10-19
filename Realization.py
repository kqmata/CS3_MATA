from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

# GCashPayment realizes/implements PaymentProcessor
class GCashPayment(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ₱{amount} via GCash.")
        return True

# --- Running the code ---
# 1. Instantiate the concrete implementation class
gateway = GCashPayment()

# 2. Invoke the realized method
success = gateway.process_payment(250.75)
print(f"Payment Status: {success}")