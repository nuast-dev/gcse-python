# Using a Function with `sorted()`

Sometimes we do not want Python to sort items in the usual way.  
Instead, we want to tell it **what value to use for sorting**.

We can do this with the `key` parameter.

## Using a built-in function as a key

```python
words = ["banana", "fig", "apple", "kiwi"]

sorted_words = sorted(words, key=len)
print(sorted_words)
```

Output:

```python
['fig', 'kiwi', 'apple', 'banana']
```

Here, `sorted()` uses the `len` function on each word first, so the words are sorted by **length**.

## Using your own function as a key

You can also write your **own function** and give that to `sorted()`.

```python
def get_count(word_count_tuple):
    """Returns the count from a word/count tuple."""
    return word_count_tuple[1]
```

This function takes a tuple such as `("python", 4)` and returns the count part, which is at index `1`.

## Example: sorting word counts by frequency

```python
word_counts = [("python", 4), ("code", 2), ("bug", 7), ("debug", 3)]

sorted_counts = sorted(word_counts, key=get_count)
print(sorted_counts)
```

Output:

```python
[('code', 2), ('debug', 3), ('python', 4), ('bug', 7)]
```

Python looks at each tuple, calls `get_count()` on it, and sorts using the value returned.

## Reverse order

If you want the highest counts first:

```python
word_counts = [("python", 4), ("code", 2), ("bug", 7), ("debug", 3)]

sorted_counts = sorted(word_counts, key=get_count, reverse=True)
print(sorted_counts)
```

Output:

```python
[('bug', 7), ('python', 4), ('debug', 3), ('code', 2)]
```

## Important point

When we write:

```python
sorted(word_counts, key=get_count)
```

we are giving Python the **function itself**.

- `key=get_count` means “use this function when sorting”
- `key=get_count()` would be wrong, because that tries to run the function immediately

## Summary

- `sorted()` can take a `key`
- the `key` is a **function**
- Python uses that function on each item before sorting
- the function can be built-in, such as `len`
- the function can also be one you wrote yourself, such as `get_count`
