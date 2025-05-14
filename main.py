from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main_program ():
    p_manager = ProductManager()
    
    p_manager. add_product(Product("Headphones", 6500, 10))
    p_manager. add_product(Product("Mouse", 2000, 10))
    p_manager. add_product(Product("Monitor", 100.050, 7))
    p_manager. add_product(Product("Keyboard", 11.100, 5))
    
    p_manager.product_name_remove("Mouse")
    
    print("Available Products:")
    p_manager.display_products()
    
    cart = Cart()
    
     # Nasumično biramo 3 proizvoda i dodajemo ih u korpu ako su dostupni
    products = p_manager.products
    for _ in range(3):
        product = random.choice(products)  # Izaberi nasumičan proizvod
        max_quantity = min(product.quantity, 3)  # Maksimum koji možemo da kupimo (ne više od 3)
        if max_quantity > 0:
            quantity = random.randint(1, max_quantity)  # Biramo količinu od 1 do max
            cart.add_to_cart(product, quantity)  # Dodajemo u korpu

    # Prikaz sadržaja korpe
    print("\nCart Contents:")
    cart.display_cart()

    # Računanje ukupne vrednosti korpe
    cart_total = cart.calculate_total()
    print(f"\nTotal Cart Value: ${cart_total:.2f}")

# Ova linija pokreće funkciju main() samo ako direktno pokrenemo fajl
if __name__ == "__main__":
    main_program()
    
    