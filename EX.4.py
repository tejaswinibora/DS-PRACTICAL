from collections import deque

# Create an empty event queue
event_queue = deque()


# Add a new event
def add_event(event_id, event_name):
    event = (event_id, event_name)
    event_queue.append(event)
    print("Event added successfully.")


# Process the event waiting the longest
def process_event():
    if event_queue:
        event = event_queue.popleft()

        print("\nProcessing Event:")
        print("Event ID:", event[0])
        print("Event Name:", event[1])
    else:
        print("No pending events.")


# Display all pending events
def display_events():
    if event_queue:
        print("\nPending Events:")

        for event in event_queue:
            print("Event ID:", event[0],
                  "| Event Name:", event[1])
    else:
        print("No pending events.")


# Cancel an event
def cancel_event(event_id):
    for event in event_queue:

        if event[0] == event_id:
            event_queue.remove(event)
            print("Event", event_id, "cancelled successfully.")
            return

    print("Event not found.")


# Main program
while True:

    print("\n----- EVENT PROCESSING SYSTEM -----")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        event_id = input("Enter Event ID: ")
        event_name = input("Enter Event Name: ")

        add_event(event_id, event_name)

    elif choice == "2":

        process_event()

    elif choice == "3":

        display_events()

    elif choice == "4":

        event_id = input("Enter Event ID to cancel: ")

        cancel_event(event_id)

    elif choice == "5":

        print("Program ended.")
        break

    else:

        print("Invalid choice.")