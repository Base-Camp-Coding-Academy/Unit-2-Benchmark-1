from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: list[str] = field(default_factory=list)
    
    def total_value(self):
        return self.price * self.quantity
    
@dataclass
class Inventory:
    products: list[Product] = field(default_factory=list)

    def add_product(self, product):

        self.products.append(product)

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.total_value()
        return total
            

    def low_stock(self, threshold=5):
        low = []
        for product in self.products:
            if product.quantity < threshold:
                low.append(product.name)
        return low
    
def main():
        inventory = Inventory()
        product1 = Product("Batman", 32.50, 4)
        inventory.add_product(product1)
        product2 = Product("Big Shoe", 14.14, 10)
        inventory.add_product(product2)
        product3 = Product("Jack's Knife Figurine", 50.02, 17)
        inventory.add_product(product3)
        print(f"Total Inventory Value: {inventory.total_inventory_value():.2f}")
        print(f"Low Stock Products {inventory.low_stock()}")
        print(product1)
        
if __name__ == "__main__":
    main()    