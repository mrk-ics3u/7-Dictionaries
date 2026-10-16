# Lesson 7 - Dictionaries

The example code for this lesson is in `dictionaries.py`. Open it alongside
these notes and run it as we go.

Dictionaries are a collection type in Python. They are similar to lists, with
some key differences:

| Aspect | Lists | Dictionaries |
|---|---|---|
| Access | By index (integer) | By key (string, int, float, boolean) |
| Order | Ordered | Keep insertion order (Python 3.6+), but don't rely on it |
| Creating | Square brackets `[]` | Curly braces `{}` |
| Items | Elements | Key-value pairs |
| Duplicates | Allowed | Keys must be unique; values can repeat |
| Mutable | Yes | Yes (add, remove or change key-value pairs) |

Comparing a list of fruit to a dictionary of fruit inventory:

```python
# list (elements)
fruits = ['apple', 'pear', 'peach', 'banana', 'pineapple', 'apple']
print(fruits[0])  # apple

# dictionary (key: value)
fruit_inventory = {'apple': 1, 'pear': 4, 'peach': 9, 'banana': 1, 'pineapple': 3}
print(fruit_inventory['pineapple'])  # the value for the key 'pineapple' (3)

# adding a new key: value
fruit_inventory['grapes'] = 5
print(fruit_inventory)
print(fruit_inventory['grapes'])

# KeyError occurs if you try to access a key that doesn't exist
#print(fruit_inventory['mango'])
```

Dictionaries:

- store key-value pairs
- need unique, unchangeable keys (usually strings; ints, floats and booleans
  also work, but not lists or dictionaries)
- can hold any type as a value, including lists or other dictionaries
- can be changed

## Creating a dictionary

Put key-value pairs inside curly braces:

```python
fruit_inventory = {'apple': 10, 'pear': 4, 'peach': 9, 'banana': 24, 'pineapple': 3}
```

## Accessing values

Use the key:

```python
print(fruit_inventory['apple'])  # 10
```

## Adding, changing and using values

```python
fruit_inventory['kiwi'] = 15    # adds a new key-value pair
fruit_inventory['apple'] += 12  # changes an existing value

if fruit_inventory['banana'] < 10:
    print("Time to order more bananas!")
```

## Removing values

```python
del fruit_inventory['pear']
removed_fruit = fruit_inventory.pop('banana', 0)  # removes and returns the value, or 0 if the key doesn't exist
```

## Using in

```python
fruit_inventory = {'apple': 10, 'pear': 4, 'peach': 9, 'banana': 24, 'pineapple': 3}

# 'in' checks whether a KEY exists (or not)
if 'apple' in fruit_inventory:
    print("There are apples!")

if 'chicken' not in fruit_inventory:
    print("Are you sure you don't want chicken?")

# loop through the KEYS ('fruit' holds each key one at a time)
for fruit in fruit_inventory:
    if fruit == 'peach':
        print("HAVE SOME MORE PEACHES")
        fruit_inventory[fruit] += 5
    print(f"{fruit}: {fruit_inventory[fruit]}")

# same thing (.keys() gives all the keys)
print(fruit_inventory.keys())
for fruit in fruit_inventory.keys():
    print(f"{fruit}: {fruit_inventory[fruit]}")

# loop through the VALUES
print(fruit_inventory.values())
for quantity in fruit_inventory.values():
    print(quantity)

# loop through KEYS and VALUES, one pair at a time
print(fruit_inventory.items())
for fruit, quantity in fruit_inventory.items():
    quantity += 5
    print(f"{fruit}: {quantity}")

# changing 'quantity' did not change the dictionary
print(fruit_inventory)
```

## Which keys are allowed?

- Unchangeable (immutable) types can be keys: strings (the usual choice),
  numbers (ints, floats) and tuples that contain only unchangeable items.
- Changeable (mutable) types such as lists and dictionaries cannot be keys.

Anything can be a value.

## Nested dictionaries

A dictionary can hold other dictionaries (or lists) as values:

```python
fruit_details = {
    'apple': {'color': 'red', 'taste': 'sweet', 'quantity': 10},
    'lemon': {'color': 'yellow', 'taste': 'sour', 'quantity': 5}
}

print(fruit_details['apple']['quantity'])  # 10
```

## Lab

That is it for the lesson. Move on to Lab 7, in `README.md`.
