import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def compare(self, newValue):
        if self.value == newValue:
            return True
        #if the node length is longer
        elif len(self.value) > len(newValue):
            shortest = newValue
        #if the values are the same length
        elif len(self.value) == len(newValue):
            shortest = newValue
        #if the new value is longer
        else:
            shortest = self.value
        index = 0
        #loop while index is less than shortest
        while index + 1 < len(shortest):
            #if the node value is closer to a return it
            if self.value[index] < newValue[index]:
                return self.value
            #if the new value is closer to a return it
            elif self.value[index] > newValue[index]:
                return newValue
            #otherwise move on to the next letter
            else:
                index += 1
        return shortest

    def insert(self, value):
        #Dim current node and whether or not the loop should continue
        loop = True
        node = self
        while loop:
            compareResult = node.compare(value)
            if type(compareResult) == bool:
                return
            elif compareResult == node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = BSTNode(value)
            elif compareResult == value:
                if node.right:
                    node = node.right
                else:
                    node.right = BSTNode(value)

    def checkForDupes(self, value):
        loop = True
        node = self
        while loop:
            compareResult = node.compare(value)
            if type(compareResult) == bool:
                return node.value
            elif compareResult == node.value:
                if node.left:
                    node = node.left
                else:
                    return
            elif compareResult == value:
                if node.right:
                    node = node.right
                else:
                    return

namesTree1 = BSTNode("Root Value")
for name in names_1:
    namesTree1.insert(name)
for name in names_2:
    dupe = namesTree1.checkForDupes(name)
    if dupe:
        # duplicates.append(dupe)
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
