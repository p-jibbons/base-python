# Python Functions Reference

A comprehensive reference repository for basic Python functions and utilities.

## Table of Contents

- [String Functions](#string-functions)
- [List Functions](#list-functions)
- [Dictionary Functions](#dictionary-functions)
- [Math Functions](#math-functions)
- [File Operations](#file-operations)
- [Date and Time Functions](#date-and-time-functions)
- [Utility Functions](#utility-functions)
- [Data Processing](#data-processing)

## Structure

```
├── src/
│   ├── string_functions.py      # String manipulation utilities
│   ├── list_functions.py        # List operations and utilities
│   ├── dict_functions.py        # Dictionary operations
│   ├── math_functions.py        # Mathematical calculations
│   ├── file_operations.py       # File I/O operations
│   ├── datetime_functions.py    # Date and time utilities
│   ├── utility_functions.py     # General utility functions
│   └── data_processing.py       # Data processing utilities
├── tests/
│   └── test_*.py               # Unit tests for each module
├── examples/
│   └── *.py                    # Usage examples
└── docs/
    └── *.md                    # Additional documentation
```

## Usage

Each module contains well-documented functions with examples. Import the functions you need:

```python
from src.string_functions import reverse_string, count_vowels
from src.list_functions import find_duplicates, merge_sorted_lists
```

## Running Tests

```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your function with proper documentation and tests
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
