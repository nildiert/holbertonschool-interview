#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print("Expected: True")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print("Expected: True")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print("Expected: False")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)

boxes = [[1, 4], [2]]
print("Expected: False..")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)

boxes = [[]]
print("Expected: True")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)

boxes = [[1],[]]
print("Expected: True")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)

boxes = [[0],[0]]
print("Expected: False")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)


boxes = [[1, 4, 6], [2], [0, 4, 1], [6, 2], [3], [4, 1], [6, 0, 1, 2, 3, 4, 5]]
print("Expected: True")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)


boxes = [[0]]
print("Expected: True")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)

boxes = [[1]]
print("Expected: True")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)

boxes = [[1], [1], [1]]
print("Expected: False")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)


boxes = [[1], [6], [1], [], [], [], [3, 4, 5, 2]]
print("Expected: True")
print(boxes)
print(canUnlockAll(boxes))
print("*"*20)
