# AI-SUGGESTED VERSION (From GitHub Copilot)
def sort_list_of_dicts(data, key):
    """
    Sorts a list of dictionaries by the specified key.
    
    Parameters:
        data (list): A list of dictionaries to sort.
        key (str): The key in the dictionaries to sort by.
        
    Returns:
        list: The sorted list of dictionaries.
    """
    return sorted(data, key=lambda x: x.get(key))

# MANUAL IMPLEMENTATION
def sort_list_of_dicts_manual(data, key):
    """
    Sorts a list of dictionaries by a specific key using manual implementation.
    """
    sorted_data = data.copy()
    n = len(sorted_data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_data[j].get(key, "") > sorted_data[j + 1].get(key, ""):
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
    return sorted_data

# TEST CODE
test_data = [
    {"name": "Charlie", "age": 35},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

print("AI version:", sort_list_of_dicts(test_data, "age"))
print("Manual version:", sort_list_of_dicts_manual(test_data, "age"))
