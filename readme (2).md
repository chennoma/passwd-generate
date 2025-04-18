# Random Password Generator

This is a simple and powerful random password generator that can generate strong passwords containing uppercase and lowercase letters, numbers and special symbols.

## Features

- Generate a random password of a specified length (32 bits by default)
- Customizable character types (uppercase letters, lowercase letters, numbers, special symbols)
- Use Python's `secrets` module to ensure the randomness and security of the password
- Simple and easy-to-use API for easy calling in other projects

## Running environment

- Python 3.6+ (Python 3.8 or higher is recommended)
- No need to install additional third-party libraries, only use Python standard libraries

## Usage

### Run directly

```bash
# Run the script directly to generate a 32-bit strong password
python passwd_generate.py
# Don't want special symbols?
python alphanumeric_passwd_generate.py
```

### Import as a module

```python
# Import password generation function
from passwd_generate import generate_password, generate_strong_password

# Generate a default 32-bit strong password (including all character types)
password = generate_strong_password()
print(password)

# Generate a password of custom length
password = generate_strong_password(length=16)
print(password)

# Custom character type
password = generate_password(
length=20,
include_uppercase=True,
include_lowercase=True,
include_digits=True,
include_symbols=False # Does not include special symbols
)
print(password)
```

## Function description

### generate_password

```python
generate_password(length=32, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True)
```

**Parameter description:**

- `length`: password length, default is 32 bits

- `include_uppercase`: whether to include uppercase letters, default is True

- `include_lowercase`: whether to include lowercase letters, default is True

- `include_digits`: whether to include numbers, default is True

- `include_symbols`: whether to include special symbols, default is True

**Return value:**

- Generated random password string

### generate_strong_password

```python
generate_strong_password(length=32)
```

**Parameter description:**

- `length`: password length, default is 32 bits

**Return value:**

- Generated strong password string (including all character types)

## Security tips

- It is recommended to use a 16-character or longer password to improve security
- For important accounts, it is recommended to use a 32-character or longer password
- Different accounts should use different passwords
- It is recommended to use a password manager to safely store generated passwords
- Change passwords for important accounts regularly