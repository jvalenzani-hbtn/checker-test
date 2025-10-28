## Bug 1 – `bug1.py`

**Intended Behavior**: Read a text file and count the number of non-empty lines.
**Issue Type**: Syntax errors.
**Notes**: Missing colons and unmatched parentheses prevent execution entirely.

## Bug 2 – `bug2.js`

**Intended Behavior**: Compute the average rating (0–5) from an array of numbers.
**Issue Type**: Logical error.
**Notes**: The function divides by `(length - 1)` instead of `length`, producing inflated averages.

## Bug 3 – `bug3.java`

**Intended Behavior**: Retrieve the `"limit"` query parameter, trim it, and convert it to an integer.
**Issue Type**: Runtime exception.
**Notes**: Calls `.trim()` on a possibly null value, leading to a `NullPointerException` when `"limit"` is missing.

## Bug 4 – `bug4.js`

**Intended Behavior**: Return a new array containing only the positive numbers from the input.
**Issue Type**: Off-by-one / loop logic issue.
**Notes**: The loop uses `i <= arr.length`, iterating one step too far and evaluating `undefined > 0`.

## Bug 5 – `bug5.py`

**Intended Behavior**: Fetch a JSON response from an API and return its `"title"` field.
**Issue Type**: Misuse of data types/libraries.
**Notes**: Uses `resp.status` instead of `resp.status_code` and incorrectly applies `json.loads()` to an already parsed object.

## Bug 6 – `bug6.java`

**Intended Behavior**: Compute a subtotal using `BigDecimal` and validate a promo code.
**Issue Type**: Misuse of data types/libraries.
**Notes**: Creates `BigDecimal` from floating-point literals (causing precision errors) and compares strings with `==` instead of `.equals()`.
