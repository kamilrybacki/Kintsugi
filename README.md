# Basic Python Project

<img
    src="https://raw.githubusercontent.com/kamilrybacki/BasicPythonProject/media/banner.webp"
    alt="Basic Python Project"
    width="100%"
/>

## Overview

This project is a basic Python application designed to provide a template for building Python-based projects. It includes essential configurations for code linting, testing, and dependency management. The repository is structured to facilitate easy project setup and maintain good coding practices.

## Project Structure

```bash
..
│
├── LICENSE # License file for the project
├── README.md # Project README file
├── .gitignore # Specifies files and directories to be ignored by Git
├── .pylintrc # Configuration for pylint (code analysis)
├── .flake8 # Configuration for flake8 (style guide enforcement)
├── pytest.ini # Configuration for pytest (testing framework)
├── mypy.ini # Configuration for mypy (type checking)
├── requirements.txt # List of dependencies for the project
├── src/
│ └── main.py # Main Python source file
├── tests/
│ └── requirements.txt # List of dependencies for testing
│ └── test_main.py # Test file for main.py
└── .github/
  └── workflows/
    └── lint-code.yml # GitHub Actions workflow for code linting
    └── code-tests.yml # GitHub Actions workflow for running tests
```

## Getting Started

### Prerequisites

- Python 3.12 or higher
- `pip` (Python package installer)
- `virtualenv` (optional but recommended)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/BasicPythonProject.git
   cd BasicPythonProject
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the main application script:

```bash
python src/main.py
```

### Running Tests

This project uses `pytest` for testing. To run tests:

```bash
pip install -r tests/requirements.txt  # Install test dependencies (together with pytest!)
pytest
```

## Code Quality and Linting

- **Pylint** and **Flake8** are used for code linting. Configuration files are provided (`.pylintrc` and `.flake8`).
- **Mypy** is used for static type checking.

To run linters manually:

```bash
pylint src/
flake8 src/
mypy src/
```

Any auxiliary libraries that are used **only** for purposes of type-checking and/or linting, should be placed
in the [`.github/workflows/requirements.txt` file].

## Enforced code quality standards

## Code Quality Standards

The project enforces several code quality standards to ensure consistent and high-quality code.
The standards are defined through the use of tools such as Flake8, Pylint, and Mypy.
In other cases - the official Python style guide (PEP 8) is followed.

Below are the details of the enforced standards:

### Flake8

Flake8 is used to enforce coding style guidelines. The key configuration from the `.flake8` file includes:

- **Maximum Line Length**: The maximum allowed line length is set to 192 characters.
  
  ```ini
  [flake8]
  max-line-length = 192
  ```

### Pylint

Pylint is used for static code analysis to identify errors and enforce a coding standard. The `.pylintrc` file specifies several rules and conventions:

- **Disabled Checks**:
  - `missing-module-docstring`: Modules do not require a docstring.
  - `missing-function-docstring`: Functions do not require a docstring.
  - `logging-fstring-interpolation`: Allows the use of f-strings in logging statements.

- **Maximum Line Length**: Consistent with Flake8, the maximum allowed line length is set to 192 characters.
  
- **Naming Conventions**:
  - **Function and Method Names**: Must follow the pattern `[a-z][a-z0-9_]{2,72}` or `_[a-z0-9_]*`.
  - **Variable Names**: Must follow the pattern `[a-z][a-z0-9_]{2,72}` or `_[a-z0-9_]*`.

  **Note**: The pattern corresponds to the so-called "snake_case" naming convention.

  ```ini
  [MESSAGES CONTROL]
  disable=
    missing-module-docstring,
    missing-function-docstring,
    logging-fstring-interpolation

  [FORMAT]
  max-line-length=192

  [BASIC]
  function-rgx=(([a-z][a-z0-9_]{2,72})|(_[a-z0-9_]*))$
  method-rgx=(([a-z][a-z0-9_]{2,72})|(_[a-z0-9_]*))$
  variable-rgx=(([a-z][a-z0-9_]{2,72})|(_[a-z0-9_]*))$
  ```

### Mypy

Mypy is used for type checking to ensure that the code adheres to the specified type annotations. The `mypy.ini` file includes:

- **Python Version**: The code is checked against Python version 3.12.
- **Exclusions**: Directories like `env/` and `build/` are excluded from type checking.

  ```ini
  [mypy]
  python_version = 3.12
  exclude = ['env/', 'build/']
  ```

These configurations help maintain a clean, readable, and consistent codebase while ensuring compliance with specified coding standards.

## Continuous Integration

The project includes a GitHub Actions workflow (`.github/workflows/lint-code.yml`) to automatically lint code on every push or pull request.

Additionally, the project includes a GitHub Actions workflow (`.github/workflows/test-code.yml`) to automatically run tests on every push or pull request.

## License

This project is licensed under the MIT License. See the [LICENSE] file for details.

[`.github/workflows/requirements.txt` file]: .github/workflows/requirements.txt
[LICENSE]: LICENSE
