#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    This method that determines if a given
    data set represents a valid UTF-8 encoding.
    """

    validation = False
    continue_flag = 0

    for element in data:

        byte = format(element, '#010b')[-8:]
        if continue_flag == 0:
            if byte[0] == '1':
                continue_flag = len(byte.split('0')[0])
            # If is UTF-8 encoding this should be greater or
            # equal than 2 and less than 5
            if continue_flag > 4 or continue_flag == 1:
                return False
            if continue_flag == 0:
                continue
        else:
            if not byte.startswith('10'):
                return False
        continue_flag = continue_flag - 1

    if continue_flag == 0:
        return True
    return validation
