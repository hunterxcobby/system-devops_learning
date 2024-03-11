Sorting a dictionary by value involves rearranging its key-value pairs based on the values in ascending or descending order. Here's a step-by-step guide on how to do it:

1. **Define the Dictionary**:
   - Start with a dictionary that you want to sort based on its values.

2. **Use the `sorted()` Function**:
   - Use the `sorted()` function in Python, which can sort any iterable, including dictionaries.
   - Pass the dictionary's `items()` method as the iterable to be sorted.

3. **Specify the Sorting Key**:
   - Provide a `key` parameter to the `sorted()` function to specify the criterion for sorting.
   - Set the `key` parameter to `lambda x: x[1]` to sort the dictionary by its values. Here, `x[1]` refers to the second element of each key-value pair, which is the value.

4. **Specify the Order (Optional)**:
   - By default, the `sorted()` function sorts in ascending order.
   - To sort in descending order, set the `reverse` parameter to `True`.

5. **Convert the Result to a List of Tuples**:
   - The `sorted()` function returns a sorted list of tuples containing the key-value pairs.
   - If you need the result as a dictionary, you can convert the sorted list of tuples back into a dictionary using a dictionary comprehension or the `dict()` constructor.

Here's an example code demonstrating how to sort a dictionary by its values:

```python
# Define the dictionary
my_dict = {'apple': 3, 'banana': 2, 'orange': 5, 'mango': 1}

# Sort the dictionary by value in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# Sort the dictionary by value in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

# Print the sorted dictionaries
print("Sorted dictionary by value in ascending order:", sorted_dict_asc)
print("Sorted dictionary by value in descending order:", sorted_dict_desc)
```

This code will output:

```
Sorted dictionary by value in ascending order: {'mango': 1, 'banana': 2, 'apple': 3, 'orange': 5}
Sorted dictionary by value in descending order: {'orange': 5, 'apple': 3, 'banana': 2, 'mango': 1}
```