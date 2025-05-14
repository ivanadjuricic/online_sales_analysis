from product import Product
from product_manager import ProductManager

def main_program ():
    p_manager = ProductManager()
    
    p_manager. add_product(Product("Headphones", 6500, 10))
    p_manager. add_product(Product("Mouse", 2000, 10))
    p_manager. add_product(Product("Monitor", 100.050, 7))
    p_manager. add_product(Product("Keyboard", 11.100, 5))
    
    p_manager.product_name_remove("Mouse")
    
    print("Available Products:")
    p_manager.display_products()