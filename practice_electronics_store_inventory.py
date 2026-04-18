# enter your code here

from peewee import *
# import sqlite3

db = SqliteDatabase("inventory.db")
class InventoryItem(Model):
    item_id = AutoField(primary_key = True)
    name = TextField()
    category = TextField()
    price = FloatField()
    stock = IntegerField()

    class Meta:
        database = db

    @classmethod
    def create(cls, **kwargs):
        price = kwargs.get("price", "")
        if price >= 0: # if price is good move on to check stock...idk
            name = kwargs.get("name", "")
            stock = kwargs.get("stock", "")
            mod_stock = stock % 10
            if mod_stock == 0:
                print(f"Item {name} added successfully.")
                return super().create(**kwargs)
            else:
                print("Invalid stock! Stock must be 0 or in increments of 10.")
                return None
        else:
            print("Invalid price! Price must be greater than or equal to $0.")
    
    def get_info(self):
        return f"ID: {self.item_id} | Name: {self.name} | Category: {self.category} | Price: ${self.price} | Stock: {self.stock}"
    
    def average_price(self):
        all_items = InventoryItem.select()
        total = 0
        item_count = 0
        for item in all_items:
            item_count += 1
            price = item.price
            total += price
        average = total/item_count
        if average == 0:
            return f"There are no items in your inventory"
        elif average > 0:
            return f"Average price of all items: {average:.2f}"
        
    def update_stock_by_10(self):
        item.stock += 10
        item.save()
        return f"Stock for {item.name} updated to {item.stock}"
    
db.connect()
db.create_tables([InventoryItem])

menu = ("1. Add an inventory item\n2. View all items\n3. View average price of all items\n4. Delete an item by ID\n5. Add stock to an item by ID\n6. Exit")
# Start of Program
while True:
    print("Electronics Store Inventory Manager:")
    print(menu)
    choice = int(input("Choose an option (1-6): "))

    if choice == 1: # Add an inventory item
        name = input("Enter the item name: ")
        category = input("Enter the category: ")
        price = float(input("Enter the price: ").replace(",", "").strip())
        stock = int(input("Enter the stock (in increments of 10): "))
        InventoryItem.create(name = name, category = category, price = price, stock = stock)
        print()
    elif choice == 2: # View all items
        all_items = InventoryItem.select()
        for item in all_items:
            print(InventoryItem.get_info(item))
        print()
    elif choice == 3: #V iew the average price of all items
        print(InventoryItem.average_price(all_items))
        print()
    elif choice == 4: # Delete an item by ID
        item_id_input = int(input("Enter the ID of the item to delete: "))
        to_delete = InventoryItem.get_by_id(item_id_input)
        to_delete.delete_instance()
        print("Item 'Apple Watch' deleted successfully.")
        print()
    elif choice == 5: # Add stock to an item by ID
        item_id_input = int(input("Enter the ID of the item to add stock to: "))
        item = InventoryItem.get_by_id(item_id_input)
        print(item.update_stock_by_10())
        print()
    elif choice == 6: # Exit
        print("Goodbye.")
        print() 
        exit()
    else:
        print('Invalid choice. Please try again.')
        print()