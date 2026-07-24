# Simple Calculator

A basic command-line calculator written in Python. Supports addition,
subtraction, multiplication, division, exponentiation, and modulo.

## Features

- Interactive loop — keep calculating without restarting the program
- Supports six operators: `+` `-` `*` `/` `**` `%`
- Handles division/modulo by zero gracefully (no crash)
- Type `q` at any prompt to quit

## Usage

```bash
python3 calculator.py
```

Example session:

```
=== Simple Calculator ===
Operators: + - * / ** %
Type 'q' at any prompt to quit.

Enter first number: 5
Enter operator (+ - * / ** %): +
Enter second number: 3
Result: 5.0 + 3.0 = 8.0

Enter first number: q
Goodbye!
```

## Operators

| Operator | Meaning         | Example    |
|----------|-----------------|------------|
| `+`      | Addition        | `2 + 3 = 5` |
| `-`      | Subtraction     | `5 - 2 = 3` |
| `*`      | Multiplication  | `4 * 3 = 12` |
| `/`      | Division        | `10 / 2 = 5` |
| `**`     | Exponentiation  | `2 ** 3 = 8` |
| `%`      | Modulo          | `10 % 3 = 1` |

## Error Handling

- Dividing or taking modulo by `0` raises a clear error message instead of
  crashing.
- Entering an unsupported operator raises a `ValueError` with the invalid
  operator shown.
- Non-numeric input (e.g. letters) raises a `ValueError` caught by the
  program and printed as a friendly error, then re-prompts.

## Requirements

- Python 3.6+
- No external dependencies

## License

MIT
