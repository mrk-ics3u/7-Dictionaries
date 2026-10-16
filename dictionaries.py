#-----------------------------------------------------------------------------
# Name:        Dictionaries (dictionaries.py)
# Purpose:     Demonstrating creating, accessing, changing and removing
#              dictionary items, looping with 'in', and nested dictionaries
#
# Author:      Mr. Kowalczewski
# Created:     28-Sept-2026
# Updated:     16-Oct-2026
#-----------------------------------------------------------------------------

# --- Lists compared to dictionaries ------------------------------------------
# list (elements)
fruits = ['apple', 'pear', 'peach', 'banana', 'pineapple', 'apple']
print(fruits[0])

# dictionary (key: value)
fruit_inventory = {'apple': 1, 'pear': 4, 'peach': 9, 'banana': 1, 'pineapple': 3}
print(fruit_inventory['pineapple'])

# adding a new key: value
fruit_inventory['grapes'] = 5
print(fruit_inventory)
print(fruit_inventory['grapes'])

# KeyError occurs if you try to access a key that doesn't exist
#print(fruit_inventory['mango'])


# --- Adding, changing, using and removing ------------------------------------
fruit_inventory = {'apple': 10, 'pear': 4, 'peach': 9, 'banana': 24, 'pineapple': 3}
print(fruit_inventory['apple'])

fruit_inventory['kiwi'] = 15    # adds a new key-value pair
fruit_inventory['apple'] += 12  # changes an existing value

if fruit_inventory['banana'] < 10:
    print("Time to order more bananas!")

del fruit_inventory['pear']
removed_fruit = fruit_inventory.pop('banana', 0)
print(removed_fruit)
print(fruit_inventory)


# --- Using in ----------------------------------------------------------------
fruit_inventory = {'apple': 10, 'pear': 4, 'peach': 9, 'banana': 24, 'pineapple': 3}

# 'in' checks whether a KEY exists (or not)
if 'apple' in fruit_inventory:
    print("There are apples!")
print()

if 'chicken' not in fruit_inventory:
    print("Are you sure you don't want chicken?")
print()

# loop through the KEYS ('fruit' holds each key one at a time)
for fruit in fruit_inventory:
    if fruit == 'peach':
        print("HAVE SOME MORE PEACHES")
        fruit_inventory[fruit] += 5
    print(f"{fruit}: {fruit_inventory[fruit]}")
print()

# same thing (.keys() gives all the keys)
print(fruit_inventory.keys())
for fruit in fruit_inventory.keys():
    print(f"{fruit}: {fruit_inventory[fruit]}")
print()

# loop through the VALUES
print(fruit_inventory.values())
for quantity in fruit_inventory.values():
    print(quantity)
print()

# loop through KEYS and VALUES, one pair at a time
print(fruit_inventory.items())
for fruit, quantity in fruit_inventory.items():
    quantity += 5
    print(f"{fruit}: {quantity}")

# changing 'quantity' did not change the dictionary
print(fruit_inventory)
print()


# --- Nested dictionaries -----------------------------------------------------
fruit_details = {
    'apple': {'color': 'red', 'taste': 'sweet', 'quantity': 10},
    'lemon': {'color': 'yellow', 'taste': 'sour', 'quantity': 5}
}

print(fruit_details['apple']['quantity'])
print()
