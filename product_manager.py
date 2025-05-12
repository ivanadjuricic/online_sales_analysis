from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product (self, product):
        self.products.append (product)
        
    def display_products (self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
               print(product.display_info())
               
    def total_amount_all_products(self):
        total = sum(product.price * product.quantity for product in self.products)
        return total
    
