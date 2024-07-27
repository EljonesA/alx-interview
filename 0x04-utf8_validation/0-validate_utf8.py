#!/usr/bin/python3
""" This module contains method to validate if dataset is valid UTF-8 encoding
"""


def validUTF8(data):
    """ validates that a dataset is valid UTF-8 encoding
    """
    # Number of bytes in the current UTF-8 character
    remaining_bytes = 0

    # Masks to check the significant bits of the byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Only consider the 8 least significant bits of each integer
        byte = byte & 0xFF

        if remaining_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 | mask2)) == mask1:
                return False  # Invalid leading byte (0b10xxxxxx)
            elif (byte & (mask1 | mask2 | (1 << 5))) == (mask1 | mask2):
                remaining_bytes = 1  # 2-byte character
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4))) == (mask1 | mask2 | (1 << 5)):
                remaining_bytes = 2  # 3-byte character
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4) | (1 << 3))) == (mask1 | mask2 | (1 << 5) | (1 << 4)):
                remaining_bytes = 3  # 4-byte character
            else:
                return False  # Invalid leading byte
        else:
            # Check if it is a valid continuation byte
            if (byte & (mask1 | mask2)) != mask1:
                return False  # Invalid continuation byte
            remaining_bytes -= 1

    return remaining_bytes == 0


if __name__ == "__main__":
    validUTF8()
