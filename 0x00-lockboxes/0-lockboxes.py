#!/usr/bin/python3
""" This program checks if all boxes can be opened """


def checkBox(box, matrix, keys_checked):
    """ This method checks all elements in a box """

    if len(box) >= 0:
        for element in box:
            if element not in keys_checked:
                if element < len(matrix):
                    keys_checked.append(element)
                    checkBox(matrix[element], matrix, keys_checked)
                else:
                    return False
            else:
                pass
        return
    else:
        return


def canUnlockAll(boxes):
    """ This method determines if all boxes can be opened """

    keys_checked = [0]
    keys = [i for i in range(len(boxes))]

    if len(boxes) is 1:
        return True
    value = checkBox(boxes[0], boxes, keys_checked)
    if value is False:
        return False
    else:
        return (all(elem in keys_checked for elem in keys))
