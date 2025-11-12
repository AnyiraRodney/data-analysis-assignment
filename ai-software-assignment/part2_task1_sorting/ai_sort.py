# ai_sort.py
# This file represents the code suggested by GitHub Copilot.

def sort_list_of_dicts_ai(data, sort_key):
    """
    Sorts a list of dictionaries by a specified key.
    """
    # --- START OF AI-SUGGESTED CODE ---
    # I typed the function definition and docstring, and
    # GitHub Copilot suggested the following line:
    return sorted(data, key=lambda x: x[sort_key])
    # --- END OF AI-SUGGESTED CODE ---


# --- Example Usage ---
if __name__ == "__main__":
    employees = [
        {'name': 'Charlie', 'age': 35},
        {'name': 'Alice', 'age': 28},
        {'name': 'Bob', 'age': 42},
    ]

    print("--- Sorted by Age (AI) ---")
    print(sort_list_of_dicts_ai(employees, 'age'))