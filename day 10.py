from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing PayPal payment of {amount}")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.process(amount)

credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

processor1 = PaymentProcessor(credit_card_payment)
processor1.process_payment(100)

processor2 = PaymentProcessor(paypal_payment)
processor2.process_payment(200)
