import time

class Medicine:
    def __init__(self, code, name, category, price, quantity):
        self.code = code
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.code} | {self.name} | {self.category} | RM{self.price:.2f} | Stock:{self.quantity}"

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        collisions = 0

        while self.table[index] is not None:
            collisions += 1

            # update if same key
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return collisions

            index = (index + 1) % self.size

        self.table[index] = (key, value)
        return collisions

    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]

            index = (index + 1) % self.size

            if index == start:
                break

        return None

    def delete(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return True

            index = (index + 1) % self.size
            if index == start:
                break

        return False

    def edit(self, key, name=None, category=None, price=None, quantity=None):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                med = self.table[index][1]

                if name:
                    med.name = name
                if category:
                    med.category = category
                if price is not None:
                    med.price = price
                if quantity is not None:
                    med.quantity = quantity

                return True

            index = (index + 1) % self.size
            if index == start:
                break

        return False

    def display(self):
        print("\n--- Hash Table Structure ---")
        for i in range(self.size):
            if self.table[i]:
                print(f"[{i}] {self.table[i][1]}")
            else:
                print(f"[{i}] Empty")

def linear_search(arr, key):
    for item in arr:
        if item.code == key:
            return item
    return None

def compare_search(hash_table, medicine_list, key):
    start = time.perf_counter_ns()
    hash_table.search(key)
    hash_time = time.perf_counter_ns() - start

    start = time.perf_counter_ns()
    linear_search(medicine_list, key)
    array_time = time.perf_counter_ns() - start

    print("\n===== Performance Comparison =====")
    print("Search Key:", key)
    print("Hash Table Time :", hash_time, "ns")
    print("Array Search Time:", array_time, "ns")

def main():
    inventory = HashTable(23)
    medicine_list = []

    sample_data = [
        Medicine("M101", "Panadol", "Tablet", 8.50, 50),
        Medicine("M102", "Actifed", "Syrup", 12.00, 30),
        Medicine("M103", "VitaminC", "Supplement", 18.90, 40),
        Medicine("M104", "Aspirin", "Tablet", 9.90, 20),
        Medicine("M105", "CoughMix", "Syrup", 14.50, 15),
        Medicine("M106", "ZincPlus", "Supplement", 22.50, 25),
        Medicine("M107", "Paracetamol", "Tablet", 7.90, 60),
        Medicine("M108", "FishOil", "Supplement", 35.00, 18),
        Medicine("M109", "Antacid", "Tablet", 6.50, 45),
        Medicine("M110", "HerbalTea", "Supplement", 16.00, 12)
    ]

    # insert sample data
    for med in sample_data:
        inventory.insert(med.code, med)
        medicine_list.append(med)

    while True:
        print("\n===== Pharmacy Inventory System =====")
        print("1. Display Medicines")
        print("2. Insert Medicine")
        print("3. Search Medicine")
        print("4. Edit Medicine")
        print("5. Delete Medicine")
        print("6. Compare Performance")
        print("7. Exit")

        choice = input("Enter choice: ")

        # DISPLAY
        if choice == "1":
            inventory.display()

        # INSERT
        elif choice == "2":
            code = input("Code: ")
            name = input("Name: ")
            category = input("Category: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))

            med = Medicine(code, name, category, price, qty)
            collisions = inventory.insert(code, med)
            medicine_list.append(med)

            print("Added successfully. Collisions:", collisions)

        # SEARCH
        elif choice == "3":
            key = input("Enter Code: ")
            result = inventory.search(key)

            if result:
                print("Found:", result)
            else:
                print("Not found")

        # EDIT
        elif choice == "4":
            key = input("Enter Code: ")
            name = input("New Name (or blank): ") or None
            category = input("New Category (or blank): ") or None

            price_input = input("New Price (or blank): ")
            price = float(price_input) if price_input else None

            qty_input = input("New Quantity (or blank): ")
            qty = int(qty_input) if qty_input else None

            if inventory.edit(key, name, category, price, qty):
                print("Updated successfully")
            else:
                print("Not found")

        # DELETE
        elif choice == "5":
            key = input("Enter Code: ")
            if inventory.delete(key):
                print("Deleted successfully")
            else:
                print("Not found")

        # COMPARE
        elif choice == "6":
            key = input("Enter Code (try M101 or M999): ")
            compare_search(inventory, medicine_list, key)

        elif choice == "7":
            print("Exit program")
            break

        else:
            print("Invalid choice")


main()