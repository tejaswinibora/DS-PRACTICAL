from collections import Counter

# Read number of library members
n = int(input("Enter number of library members: "))

# Create an empty list
borrow = []

# Read borrow count of each member
for i in range(n):
    count = int(input(f"Enter books borrowed by member {i+1}: "))
    borrow.append(count)

# Calculate average
average = sum(borrow) / n

# Highest borrow count
highest = max(borrow)

# Lowest borrow count
lowest = min(borrow)

# Count members with zero borrowings
zero = borrow.count(0)

# Find mode
frequency = Counter(borrow)
mode = frequency.most_common(1)[0][0]

# Display report
print("\n========== LIBRARY REPORT ==========")
print("Borrow Counts:", borrow)
print("Average Borrow Count:", average)
print("Highest Borrow Count:", highest)
print("Lowest Borrow Count:", lowest)
print("Members with No Borrowings:", zero)
print("Most Frequent Borrow Count (Mode):", mode)