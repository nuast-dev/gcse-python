# What does `::` do in list slicing?

In Python slicing, `::` means:

```python
sequence[start:stop:step]
```

The **second colon introduces the step**.

## Examples

```python
nums = [10, 20, 30, 40, 50, 60]

print(nums[::1])   # [10, 20, 30, 40, 50, 60]
print(nums[::2])   # [10, 30, 50]
print(nums[1::2])  # [20, 40, 60]
print(nums[::-1])  # [60, 50, 40, 30, 20, 10]
```

## How to read it

- `[:]` → everything
- `[::2]` → everything, taking every 2nd item
- `[1::2]` → start at index `1`, then every 2nd item
- `[::-1]` → go backwards one step at a time, so it reverses the list

## Simple way to remember it

- first part = where to start
- second part = where to stop
- third part = how big each jump is

So `::` does not mean something special on its own — it just means the `start` and `stop` parts have been left blank, and only the `step` is being given.
