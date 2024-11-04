#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data: List of integers representing bytes

    Returns:
        bool: True if valid UTF-8, False otherwise
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Loop through each integer in the data
    for num in data:
        # Get the 8 least significant bits of the number
        byte = num & 255

        # If we're starting a new character
        if n_bytes == 0:
            # Count how many bytes this character uses
            if byte >> 7 == 0:  # 1 byte character (0xxxxxxx)
                continue
            elif byte >> 5 == 0b110:  # 2 byte character
                n_bytes = 1
            elif byte >> 4 == 0b1110:  # 3 byte character
                n_bytes = 2
            elif byte >> 3 == 0b11110:  # 4 byte character
                n_bytes = 3
            else:  # Invalid starting byte
                return False
        else:
            # Check if the byte is a valid continuation byte
            if byte >> 6 != 0b10:  # Should be 10xxxxxx
                return False
            n_bytes -= 1

    # All characters should be complete
    return n_bytes == 0
