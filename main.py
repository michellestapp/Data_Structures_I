# Task 1: Dictionary, Set and Tuple
# Given the following three scenarios, choose the best data structure
# (between a dictionary, set, or tuple) to efficiently store the data. 
# Each scenario ties directly to one data structure. Each data structure will be used only once. 
# You will need to determine which data structure is best for which scenario, and then implement the data structure in Python.
#
# 1)   Store the months of the year as strings. Determine the month in the data structure in which 
#      National Pi Day (March 14th ) exists and print that month to the console. 
#       HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.

# 2)  Store five fruits or vegetables.
#       Add two of your favorite fruits and two of your favorite vegetables to the collection.
#       Iterate over the collection and print each one to the console. 

# 3)  Store information about a user profile. Use literal string interpolation to print the user’s profile information to the console. The profile should consist of the following information:
#       First Name
#       Last Name
#       Email Address
#       Phone Number

from implementation import Implementation
from linked_list import LinkedList

# class RunMain:
#     def __init__(self) -> None:
#         self.list = LinkedList()

#     def append_nodes(self):
#         print("\n Add a new node with the value of 5")
#         self.list.append_node(5)
#         print("\n Add a new node with the value of 10")
#         self.list.append_node(10)
#         print("\n Add a new node with the value of 24")
#         self.list.append_node(24)

#     def find_values(self):
#         print("\n Search for a node with the value of 10")
#         print(self.list.find_node(10))
#         print("\n Search for a node with the value of 22")
#         print(self.list.find_node(22))

# if __name__ == '__main__':
#     main = RunMain()
#     main.append_nodes()
#     main.find_values()

from binary_node import BinaryNode

run_binary = BinaryNode(list)
run_binary.insert_node(5)
run_binary.insert_node(3)
run_binary.insert_node(15)


# task_1 = Implementation()
# task_1.tuple()
# task_1.set()
# task_1.dictionary()
# task_2 = Implementation()
# task_2.family()

# my_linked_list = LinkedList()
# my_linked_list.append_node(5)
# my_linked_list.append_node(10)
# my_linked_list.append_node(43)
# my_linked_list.append_node(52)
# my_linked_list.append_node(25)

# my_linked_list.find_node(5)
# my_linked_list.find_node(24)
# my_linked_list.find_node(25)
# my_linked_list.find_node(52)

