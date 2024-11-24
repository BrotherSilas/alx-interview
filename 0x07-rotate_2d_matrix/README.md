Rotate 2D Matrix
This project focuses on implementing a function to rotate a 2D matrix 90 degrees clockwise in place, adhering to the specified constraints.

Description
Given an n x n 2D matrix, this program modifies it in place to rotate it 90 degrees clockwise. The solution avoids creating additional copies of the matrix and performs all transformations within the original data structure.

Requirements
Language: Python 3.8.10 (or compatible version)
Environment: Ubuntu 20.04 LTS
Coding Style: PEP 8 compliant (checked with pycodestyle version 2.8.0)
No additional libraries or modules are used.
Includes in-place operations to optimize space complexity.

Files
0-rotate_2d_matrix.py :	Contains the function rotate_2d_matrix that performs the rotation.
main_0.py : Test script to demonstrate the functionality of the rotate_2d_matrix function.
README.md : Documentation for the project.

Usage
Clone the Repository
git clone https://github.com/your-username/alx-interview.git
cd alx-interview/0x07-rotate_2d_matrix
Run the Test Script
Make the script executable:
chmod +x main_0.py
Run the test:
./main_0.py

Expected Output
For the sample input matrix:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

The output after rotation will be:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Function Prototype
python
def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of lists): The n x n 2D matrix to rotate.

    Returns:
        None: The matrix is modified in-place.
    """

Constraints
The matrix will always be 2D and non-empty.
The matrix will be a square matrix (n x n).

Testing and Validation
Run the provided test script main_0.py to verify the rotation functionality.
Ensure code style compliance:
bash
pycodestyle 0-rotate_2d_matrix.py

Author
Silas Edet

GitHub: BrotherSilas
Email: silasedetsnr@gmail.com

