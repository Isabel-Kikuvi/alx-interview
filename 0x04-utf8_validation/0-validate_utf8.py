#!/usr/bin/python3

"""Checks if given data set represents a valid UTF-8 encoding """


def validUTF8(data):
    def is_start_of_char(byte):
        return (byte & 0b10000000) == 0b00000000

    def is_continuation(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        current_byte = data[i]

        if is_start_of_char(current_byte):
            num_bytes = 1
        elif (current_byte & 0b11100000) == 0b11000000:
            num_bytes = 2
        elif (current_byte & 0b11110000) == 0b11100000:
            num_bytes = 3
        elif (current_byte & 0b11111000) == 0b11110000:
            num_bytes = 4
        else:
            return False  # Invalid starting byte

        if i + num_bytes > len(data):
            return False

        for j in range(1, num_bytes):
            if not is_continuation(data[i + j]):
                return False

        i += num_bytes

    return True
