# Undo and Redo System using Stack

undo_stack = []
redo_stack = []

document = ""


def make_change(new_text):
    global document

    # Store current state before making a change
    undo_stack.append(document)

    # Make the new change
    document = new_text

    # Clear redo stack because a new change is made
    redo_stack.clear()

    print("Change made successfully.")


def undo():
    global document

    if len(undo_stack) == 0:
        print("Nothing to undo.")
    else:
        # Store current state in redo stack
        redo_stack.append(document)

        # Get previous state from undo stack
        document = undo_stack.pop()

        print("Undo performed successfully.")


def redo():
    global document

    if len(redo_stack) == 0:
        print("Nothing to redo.")
    else:
        # Store current state in undo stack
        undo_stack.append(document)

        # Get the most recently undone state
        document = redo_stack.pop()

        print("Redo performed successfully.")


def display_document():
    print("\nCurrent Document State:")
    print(document)


# Main program

while True:

    print("\n----- TEXT EDITOR -----")
    print("1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_text = input("Enter new document text: ")
        make_change(new_text)

    elif choice == "2":
        undo()

    elif choice == "3":
        redo()

    elif choice == "4":
        display_document()

    elif choice == "5":
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")