#!/usr/bin/python3
""" This program checks if all boxes can be opened """


def checkBox(box, matrix, keys_checked, keys, boxes_checked):
    """ This method checks all elements in a box """

    if len(matrix) is 1 and len(matrix[0]) is 1:
        return True
    if type(box) is not list:
        return False

    if len(box) > 0:
        for element in box:
            if element < len(matrix):
                keys_checked[element] = 'Opened'
                if element not in boxes_checked:
                    boxes_checked.append(element)
                    if len(boxes_checked) == len(matrix):
                        return True
                    checkBox(matrix[element], matrix, keys_checked, keys,
                             boxes_checked)
                else:
                    pass
            else:
                if len(boxes_checked) == len(matrix):
                    return True
                return False
    else:
        return


def canUnlockAll(boxes):
    """ This method determines if all boxes can be opened """

    keys = ['Opened' for i in range(len(boxes))]
    keys_checked = ['Closed' for i in range(len(boxes))]
    keys_checked[0] = 'Opened'
    boxes_checked = [0]

    value = checkBox(boxes[0], boxes, keys_checked, keys, boxes_checked)
    if type(boxes) is not list or len(boxes) == 0:
        return False
    if value is False:
        return False
    if value is True:
        return True

    return (all(elem in keys for elem in keys_checked))
