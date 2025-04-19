from vending_machine_state import VendingMachineState
from product import Product
from coin import Coin
from note import Note

class ReadyState(VendingMachineState):
    def __init__(self, instance):
        self.vending_machine = instance
    
    def select_product(sefll, product: Product):
        print("[ERROR] Product is already selecte. Please completed payment.")
    
    def insert_coin(self, coin: Coin):
        self.vending_machine.add_coin(coin)
        print(f"Coint inserted: {coin.name}")
        self.check_payment_status()
    
    def insert_note(self, note: Note):
        self.vending_machine.add_note(note)
        print(f"Inserted note: {note.name}")
        self.check_payment_status()
        
    def dispense_product(self, product: Product):
        print("[ERROR] Please complete payment first")
    
    def return_change(self):
        change = self.vending_machine.total_payment - self,vending_machine.selected_product.price
        
        if change > 0: 
            print(f"Change returned: ₹{change:.2f}")
            self.vending_machine.reset_payment()
        else:
            print("No change to return")
        
        self.vending_machine.reset_payment()

    def check_payment_status(self):
        if self.vending_machine.total_payment >= self.vending_machine.selected_product.price:
            self.vending_machine.set_state(self.vending_machine.dispense_state)
    