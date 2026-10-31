TABLE_SIZE = 10

# Create hash table
hash_table = [None] * TABLE_SIZE


# Hash function using division method
def hash_function(key):
    return key % TABLE_SIZE


# Insert operation
def insert(key):
    index = hash_function(key)

    for i in range(TABLE_SIZE):

        new_index = (index + i) % TABLE_SIZE

        if hash_table[new_index] is None:
            hash_table[new_index] = key
            print("Key inserted successfully.")
            return

        if hash_table[new_index] == key:
            print("Key already exists.")
            return

    print("Hash table is full.")


# Search operation
def search(key):
    index = hash_function(key)

    for i in range(TABLE_SIZE):

        new_index = (index + i) % TABLE_SIZE

        if hash_table[new_index] == key:
            print("Key found at index:", new_index)
            return

        if hash_table[new_index] is None:
            break

    print("Key not found.")


# Delete operation
def delete(key):
    index = hash_function(key)

    for i in range(TABLE_SIZE):

        new_index = (index + i) % TABLE_SIZE

        if hash_table[new_index] == key:
            hash_table[new_index] = None
            print("Key deleted successfully.")
            return

        if hash_table[new_index] is None:
            break

    print("Key not found.")


# Display hash table
def display():
    print("\n----- HASH TABLE -----")

    for i in range(TABLE_SIZE):
        print(i, ":", hash_table[i])


# Main menu
while True:

    print("\n----- HASH TABLE MENU -----")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        key = int(input("Enter key: "))
        insert(key)

    elif choice == "2":

        key = int(input("Enter key: "))
        search(key)

    elif choice == "3":

        key = int(input("Enter key: "))
        delete(key)

    elif choice == "4":

        display()

    elif choice == "5":

        print("Program ended.")
        break

    else:

        print("Invalid choice.")