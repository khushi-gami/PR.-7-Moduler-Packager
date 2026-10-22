PR.-7-Moduler-Packager (Multi-Utility Toolkit) (VIDEO)
https://drive.google.com/file/d/1fHf0bzcMtWYQJw7IMMK1HACVQiw391iz/view?usp=sharing

# PR.-7-Moduler-Packager (Multi-Utility Toolkit)

A beginner-friendly Python project that combines multiple useful utilities into a single menu-driven application. This project demonstrates how to organize Python code using **modules, packages, functions, and reusable helper methods**.

The toolkit provides date and time operations, mathematical calculations, random data generation, UUID generation, file handling, and module exploration.

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Python Concepts Demonstrated](#-python-concepts-demonstrated)
- [Feature Details](#-feature-details)
- [Learning Objectives](#-learning-objectives)

## 📖 Project Overview

The Multi-Utility Toolkit is a command-line application developed using Python. It brings several common programming utilities together through an interactive menu.

The project is designed to practice Python fundamentals and understand how to divide a larger program into smaller, reusable modules and packages.

Instead of writing all functionality in a single file, the project uses separate files for mathematical operations, random utilities, UUID generation, date and time operations, and file handling.

## ✨ Features

### 1. Date and Time Operations

- Display the current date and time.
- Calculate the difference between two dates.
- Calculate the duration between two times.
- Format dates into different formats.
- Display the month name and weekday.
- Use a stopwatch with start, stop, reset, and exit options.
- Run a countdown timer.

### 2. Mathematical Operations

- Calculate the factorial of a number.
- Calculate compound interest and the final amount.
- Perform trigonometric calculations:
  - Sine
  - Cosine
  - Tangent
- Calculate the area of geometric shapes:
  - Circle
  - Triangle

### 3. Random Data Generation

- Generate a random integer within a specified range.
- Generate a list of random integers.
- Generate a random password using letters, digits, and punctuation.
- Generate a numeric OTP of a specified length.

### 4. UUID Generation

- Generate a UUID using Python's `uuid` module.
- Display a unique identifier for demonstration purposes.

### 5. File Operations

- Create a new file using exclusive creation mode (`x`).
- Write content to a file using write mode (`w`).
- Read the contents of a file.
- Append new content using append mode (`a`).
- Handle common file errors such as missing files and existing files.

### 6. Module Exploration

- Explore module attributes using Python's built-in `dir()` function.
- Practice working with Python modules and their available names.

_Note: The module explorer is currently limited to the module names configured in `helper.py`._

## 📂 Project Structure

```text
moduler & packager/
│
├── geometry/
│   ├── __init__.py
│   ├── circle.py
│   └── triangle.py
│
├── utilities/
│   ├── __init__.py
│   ├── date_utils.py
│   └── file_utils.py
│
├── helper.py
├── main.py
├── math_utils.py
├── random_utils.py
├── uuid_utils.py
└── README.md
```

### Folder and File Description

| File / Folder             | Purpose                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------ |
| `main.py`                 | Contains the main menu and connects the different utilities.                         |
| `helper.py`               | Provides reusable input-validation functions and module exploration.                 |
| `math_utils.py`           | Contains factorial, compound interest, and trigonometric calculations.               |
| `random_utils.py`         | Generates random numbers, lists, passwords, and OTPs.                                |
| `uuid_utils.py`           | Generates UUIDs using Python's `uuid` module.                                        |
| `geometry/`               | Groups functions related to geometric calculations.                                  |
| `geometry/__init__.py`    | Exposes the circle and triangle area functions through the package.                  |
| `geometry/circle.py`      | Calculates the area of a circle.                                                     |
| `geometry/triangle.py`    | Calculates the area of a triangle.                                                   |
| `utilities/`              | Groups date/time and file-handling utilities.                                        |
| `utilities/__init__.py`   | Exposes selected functions from the utility modules.                                 |
| `utilities/date_utils.py` | Contains date formatting, date/time differences, stopwatch, and countdown functions. |
| `utilities/file_utils.py` | Contains file creation, reading, writing, and appending functions.                   |

## 🧰 Technologies Used

- **Python 3** — Main programming language.
- **Standard Library Modules:**
  - `math` — Mathematical operations.
  - `random` — Random number and sequence generation.
  - `string` — Character sets for password generation.
  - `datetime` — Date and time calculations.
  - `time` — Stopwatch timing and countdown delays.
  - `uuid` — UUID generation.
- **Built-in Functions:** `input()`, `print()`, `open()`, `dir()`, `range()`, `round()`, and `abs()`.

No third-party packages are currently required.

## 🧠 Python Concepts Demonstrated

This project provides practical experience with:

- Functions and function arguments.
- Modules and packages.
- Importing functions and modules.
- The `__init__.py` file in Python packages.
- Conditional statements and loops.
- Input validation and type conversion.
- Exception handling using `try`, `except`, and `ValueError`.
- File handling and file modes (`x`, `r`, `w`, and `a`).
- Working with dates and times.
- Random data generation.
- Mathematical formulas and calculations.
- String formatting and manipulation.
- The `if __name__ == "__main__":` execution guard.
- Code organization and reusability.

## 🖥️ Feature Details

### Main Menu

The application provides these main options:

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations
6. Explore Module Attributes (`dir()`)
7. Exit

### Example: Compound Interest

The toolkit calculates compound interest using the formula:

**Final Amount:**

`A = P × (1 + R/100)^T`

**Compound Interest:**

`CI = A − P`

Where:

- `P` = Principal amount.
- `R` = Annual interest rate in percent.
- `T` = Time in years.
- `A` = Final amount.

### Example: Area of a Circle

The area of a circle is calculated using:

`Area = π × r²`

Where `r` is the radius of the circle.

### Example: Area of a Triangle

The area of a triangle is calculated using:

`Area = ½ × base × height`

### Example: UUID Generation

The project uses `uuid.uuid4()` to generate a random UUID.

UUIDs are useful for demonstrating unique identifiers in applications. They should not be treated as authentication secrets.

## 🎯 Learning Objectives

The main objectives of this project are to:

- Understand how to divide a Python application into modules and packages.
- Build a menu-driven command-line application.
- Reuse functions across different files.
- Practice input validation and exception handling.
- Work with Python's standard library.
- Understand file operations and common file errors.
- Improve problem-solving skills through practical implementation.

## 👩‍💻 Author

**Developed as a Python learning project** to practice modular programming, packages, reusable functions, exception handling, and standard library utilities.
