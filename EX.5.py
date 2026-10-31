TABLE_SIZE = 10

# Create hash table
hash_table = [[] for _ in range(TABLE_SIZE)]


# Division Method Hash Function
def hash_function(key):
    return key % TABLE_SIZE


# Insert Operation
def insert(key, value):
    index = hash_function(key)

    # Check if key already exists
    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            print("Key already exists. Value updated.")
            return

    # Add new key-value pair
    hash_table[index].append([key, value])

    print("Key-value pair inserted successfully.")


# Search Operation
def search(key):
    index = hash_function(key)

    for pair in hash_table[index]:
        if pair[0] == key:
            print("Value found:", pair[1])
            return pair[1]

    print("Key not found.")
    return None


# Delete Operation
def delete(key):
    index = hash_function(key)

    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            print("Key-value pair deleted successfully.")
            return

    print("Key not found.")


# Display Hash Table
def display():
    print("\n----- HASH TABLE -----")

    for index in range(TABLE_SIZE):
        print(index, ":", hash_table[index])


# Main Program
while True:

    print("\n===== HASH TABLE =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        key = int(input("Enter key: "))
        value = input("Enter value: ")

        insert(key, value)

    elif choice == "2":

        key = int(input("Enter key to search: "))

        search(key)

    elif choice == "3":

        key = int(input("Enter key to delete: "))

        delete(key)

    elif choice == "4":

        display()

    elif choice == "5":

        print("Program ended.")
        break

    else:

        print("Invalid choice.")