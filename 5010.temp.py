from abc import ABC, abstractmethod

# Abstract interface for any payment method
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Stripe implements the interface
class StripePayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} using Stripe")

# PayPal implements the same interface
class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal")

# Store depends on abstraction, not concrete classes
class Store:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount):
        self.payment_processor.pay(amount)

# Usage
store1 = Store(StripePayment())
store1.checkout(100)

store2 = Store(PayPalPayment())
store2.checkout(200)
