# UTF-8 Validation

## Overview
This project implements a method that determines if a given data set represents a valid UTF-8 encoding. The method validates whether a sequence of bytes follows UTF-8 encoding rules.

## Table of Contents
* [Requirements](#requirements)
* [Files](#files)
* [Function Description](#function-description)
* [Installation](#installation)
* [Usage](#usage)
* [Test Files](#test-files)
* [Examples](#examples)

## Requirements
### Python Scripts
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A `README.md` file at the root of the folder of the project is mandatory
* Code should use the `PEP 8` style (version 1.7.x)
* All files must be executable

## Files
* `0-validate_utf8.py`: Contains the `validUTF8` function implementation
* `0-main.py`: Test file to verify the function's functionality

## Function Description
### `validUTF8(data)`
Determines if a given data set represents a valid UTF-8 encoding.

#### Parameters
* `data`: List of integers where each integer represents 1 byte of data

#### Returns
* `True` if data is a valid UTF-8 encoding
* `False` otherwise

#### Rules
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* Each integer represents 1 byte of data
* Only the 8 least significant bits of each integer need to be considered

## Installation
```bash
git clone https://github.com/your_username/alx-interview.git
cd 0x04-utf8_validation
```

## Usage
```python
validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # Should print: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Should print: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Should print: False
```

## Test Files
Execute the test file using:
```bash
./0-main.py
```

## Examples
```python
# Example 1: Valid single ASCII character
data = [65]  # Represents 'A'
validUTF8(data)  # Returns: True

# Example 2: Valid string "Python is cool!"
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
validUTF8(data)  # Returns: True

# Example 3: Invalid UTF-8 sequence
data = [229, 65, 127, 256]
validUTF8(data)  # Returns: False
```

## Repository
* GitHub repository: `alx-interview`
* Directory: `0x04-utf8_validation`
* File: `0-validate_utf8.py`
