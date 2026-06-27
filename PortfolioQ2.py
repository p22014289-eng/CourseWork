import time

class Transaction:
    def __init__(self, transactionID, customerName, productName, amount, transactionDate):
        self.transactionID = transactionID
        self.customerName = customerName
        self.productName = productName
        self.amount = amount
        self.transactionDate = transactionDate

    def __str__(self):
        return f"{self.transactionID} | {self.customerName} | {self.productName} | RM{self.amount} | {self.transactionDate}"

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # Divide
    right = merge_sort(arr[mid:])     # Divide

    return merge(left, right)         # Conquer + Combine


def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].transactionID < right[j].transactionID:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Add remaining items
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid].transactionID == target:
            return arr[mid]
        elif arr[mid].transactionID < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

def linear_search(arr, target):
    for item in arr:
        if item.transactionID == target:
            return item
    return None

def display(arr):
    for item in arr:
        print(item)



def main():

    transactions = [
        Transaction("T105", "Ali", "Shoes", 120.50, "2026-01-10"),
        Transaction("T101", "Sara", "Bag", 80.00, "2026-01-01"),
        Transaction("T110", "John", "Watch", 250.00, "2026-01-15"),
        Transaction("T102", "Lily", "Book", 40.00, "2026-01-02"),
        Transaction("T108", "Ahmad", "Phone", 999.00, "2026-01-12"),
        Transaction("T103", "Kumar", "Laptop", 3000.00, "2026-01-03"),
        Transaction("T107", "Aina", "Headset", 150.00, "2026-01-11"),
        Transaction("T104", "Ben", "Mouse", 60.00, "2026-01-05"),
        Transaction("T109", "Chen", "Keyboard", 120.00, "2026-01-13"),
        Transaction("T106", "David", "Monitor", 700.00, "2026-01-09")
    ]

    sorted_transactions = transactions

    while True:
        print("\n===== Transaction System =====")
        print("1. Display Transactions")
        print("2. Sort (Merge Sort)")
        print("3. Binary Search")
        print("4. Linear Search")
        print("5. Exit")

        choice = input("Enter choice: ")

        # DISPLAY
        if choice == "1":
            display(sorted_transactions)

        # MERGE SORT
        elif choice == "2":
            print("\nBefore Sorting:")
            display(sorted_transactions)

            start = time.perf_counter()
            sorted_transactions = merge_sort(sorted_transactions)
            end = time.perf_counter()

            print("\nAfter Sorting:")
            display(sorted_transactions)

            print(f"\nMerge Sort Time: {end - start:.6f} seconds")

        # BINARY SEARCH
        elif choice == "3":
            key = input("Enter Transaction ID: ")

            start = time.perf_counter()
            result = binary_search(sorted_transactions, key)
            end = time.perf_counter()

            if result:
                print("Found:", result)
            else:
                print("Transaction not found")

            print(f"Binary Search Time: {end - start:.6f} seconds")

        # LINEAR SEARCH
        elif choice == "4":
            key = input("Enter Transaction ID: ")

            start = time.perf_counter()
            result = linear_search(transactions, key)
            end = time.perf_counter()

            if result:
                print("Found:", result)
            else:
                print("Transaction not found")

            print(f"Linear Search Time: {end - start:.6f} seconds")

        elif choice == "5":
            print("Program ended.")
            break

        else:
            print("Invalid choice")


main()