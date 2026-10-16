# Lab 7 - Grocery List

Write a program that keeps a grocery list in a dictionary.

Open `main.py` and complete the following:

1. Update the header with your information (Name, Purpose, Author, Created, Updated).
2. Create an empty dictionary.
3. Ask for an item with the prompt `Item: `. If the item is `done`, stop asking.
4. Otherwise ask for a quantity with the prompt `Quantity: ` (a whole number). Assume it is positive.
5. If the item is already in the dictionary, add the quantity to what is there. If not, add the item with that quantity.
6. Repeat steps 3 to 5 until `done` is entered.
7. Print the list, one item per line, as `item: quantity` (for example `milk: 2`).
8. If there is no `apples` item, print `Are you sure you don't want apples?`
9. If there are more than 10 `apples`, print `That's too many apples!`
10. If there is an `oranges` item, take away 5 oranges. If that leaves 0 or fewer, delete `oranges` from the dictionary.
11. Print the list again, in the same format as step 7.

Items are typed in lowercase, exactly as they should appear. Print the items in
the order they were first entered.

## Running your program

Open `main.py` and press the Run button in the top right corner of VS Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B** to run the tests. You will see one line per test:

```
[PASS] 1. Header is filled in
[FAIL] 2. Repeated apples, oranges reduced
```

When a test fails it shows what was expected and what your program printed. Fix your code and press Ctrl+Shift+B again. Keep going until all tests pass.

## Reminders

- Fill in every field of the header before you write any code.
- Write comments as you go.
- Tests check your output exactly, including the apostrophes in `don't` and `That's`. Use a plain `'` on your keyboard.
- The prompts share a line with the next output, so the first list line prints right after the last `Item: ` prompt.

## Optional challenges

Finished early? Try the optional challenges in the `challenges` folder. Open `challenges/CHALLENGES.md` for instructions. They are not assessed and do not affect your lab result.
