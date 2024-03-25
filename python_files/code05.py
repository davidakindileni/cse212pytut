# removing and returning the item from the front of the queue -code05.py
myQueue = [4, 15, 26, 78, 134, "Jade", "Kirk", "Lily", [True, True, False], (78, 84, 92)]

# return the item in the front of the queue
front_element = myQueue[0]

# removing the element at index 0
del myQueue[0]

print(myQueue)