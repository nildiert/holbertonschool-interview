#!/usr/bin/python3
""" This program checks if all boxes can be opened """


def checkBox(index, key, boxes):
    """ This method determines if all boxes can be opened  """
    return (key in boxes[index] and key != index)


def canUnlockAll(boxes):
    """ This method determines if all boxes can be opened """

    for key in range(1, len(boxes) - 1):
        flag = False
        for index in range(len(boxes)):
            flag = checkBox(index, key, boxes)
            if flag:
                break
        if flag is False:
            return flag
    return True
