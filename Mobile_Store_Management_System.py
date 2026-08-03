# Mobile Store Management System
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.category = self.categorize()
    def categorize(self):
        if self.price >= 50000:
            return "Premium"
        elif 20000 <= self.price < 50000:
            return "Mid-range"
        else:
            return "Budget"
    def __str__(self):
        return f"{self.brand} {self.model} - ₹{self.price} ({self.category})"
class Store:
    def __init__(self, name):
        self.name = name
        self.mobiles = []
    def add_mobile(self, mobile):
        self.mobiles.append(mobile)
        print(f"Added: {mobile}")
    def display_mobiles(self):
        print(f"\nMobiles in {self.name}:")
        for mobile in self.mobiles:
         print(mobile)
store = Store("Tanishka's Mobile Store")
store.add_mobile(Mobile("Apple", "iPhone 14 Pro", 120000))
store.add_mobile(Mobile("Samsung", "Galaxy S21", 45000))
store.add_mobile(Mobile("Redmi", "Note 11", 15000))
store.display_mobiles()
