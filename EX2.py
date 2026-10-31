# Selection Sort and Bubble Sort
# Employee Salary Management

def selection_sort(salaries):
    n = len(salaries)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j

        salaries[i], salaries[min_index] = \
            salaries[min_index], salaries[i]

    return salaries


def bubble_sort(salaries):
    n = len(salaries)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = \
                    salaries[j + 1], salaries[j]

    return salaries


# Input
salaries = []

n = int(input("Enter number of employees: "))

for i in range(n):
    salary = float(input("Enter salary of employee " + str(i + 1) + ": "))
    salaries.append(salary)

# Create copies for both sorting algorithms
selection_salaries = salaries.copy()
bubble_salaries = salaries.copy()

# Selection Sort
selection_sorted = selection_sort(selection_salaries)

# Bubble Sort
bubble_sorted = bubble_sort(bubble_salaries)

# Display results
print("\nOriginal Salaries:")
print(salaries)

print("\nSalaries using Selection Sort:")
print(selection_sorted)

print("\nSalaries using Bubble Sort:")
print(bubble_sorted)

# Top five highest salaries
top_five = sorted(salaries, reverse=True)[:5]

print("\nTop Five Highest Salaries:")

for salary in top_five:
    print(salary)