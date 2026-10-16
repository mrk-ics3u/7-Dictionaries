# Optional Challenges - Lab 7

**This challenge is optional.** Try it once Lab 7 passes every test. It is not
assessed, and it does not affect your lab result.

## Store Inventory

Open `inventory.py` and write a program that manages a store's inventory. Each
item has a price and a quantity.

1. Create an empty dictionary.
2. In a loop, ask for an item name with the prompt `Item: `
   - If the item is new, ask for its price with `Price: ` (use `float()`), then
     its quantity with `Quantity: ` (use `int()`). Store both.
   - If the item already exists, ask only `Quantity to add: ` and add it to the
     item's stock. Do not ask for the price again.
   - Stop when the user enters `done`.
3. Print the heading `Item | Price | Quantity | Total Value`
4. Loop through the dictionary. For each item, work out its total value (price
   times quantity) and print one row, with the parts separated by ` | `, and the
   total value rounded to 2 decimal places with `round()`. Add each total to a
   grand total.
5. Print `Grand total: ` followed by the grand total, rounded to 2 decimal places.
6. Ask for the inflation increase with the prompt `Inflation %: ` (use `float()`).
   Increase every item's price by that percentage.
7. Print `New grand total: ` followed by the new grand total, rounded to 2
   decimal places.

Hint: each item can be a dictionary itself, with the keys `price` and `quantity`.

For example, this input:

```
apple
1.50
10
pear
2
5
apple
4
done
10
```

prints this (prompts not shown):

```
Item | Price | Quantity | Total Value
apple | 1.5 | 14 | 21.0
pear | 2.0 | 5 | 10.0
Grand total: 31.0
New grand total: 34.1
```

`apple` appears twice, so the second time only `Quantity to add: ` is asked.

## Running your program

Open the challenge file and press the Run button in the top right corner of VS
Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B**, the same as for the lab. The Lab 7 results appear first.
Scroll down to the **OPTIONAL CHALLENGES** section for this.

`SKIP` means you have not started the challenge yet. It is not an error.

## Reminders

- This is optional. Finish Lab 7 first.
- Comment as you go.
- Output is matched exactly, the same as the lab. Copy the prompts exactly,
  including the space after the colon.
