# manual_sort.py
# This is my manual implementation of the sorting function.

def sort_list_of_dicts_manual(data, sort_key):
    """
    Sorts a list of dictionaries by a specified key.
    """
    # Using the built-in sorted() function with a lambda function.
    # This is the standard, efficient Python way.
    return sorted(data, key=lambda x: x[sort_key])

# --- Example Usage ---
if __name__ == "__main__":
    employees = [
        {'name': 'Charlie', 'age': 35},
        {'name': 'Alice', 'age': 28},
        {'name': 'Bob', 'age': 42},
    ]

    print("--- Sorted by Name (Manual) ---")
    print(sort_list_of_dicts_manual(employees, 'name'))