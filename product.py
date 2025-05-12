class Product:
    def __init__(self, name, price, quantity):
        self. name = name
        self. price = price
        self. quantity = quantity
        
    def display_info (self):
        return f"Product name: {self.name}, Price: EUR{self.price}, Quantity: {self.quantity}"
    
    def adding_quantity (self, product_unit):
        self.quantity += product_unit
        if self.quantity < 0:
            self.quantity = 0
            print (f"Quantity for {self.name} shouldn't be less then 0.")
            
