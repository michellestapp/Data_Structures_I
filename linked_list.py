class Node:
    def __init__(self, list) -> None:
        self.list = list
        self.next_node = None


class LinkedList:
    def __init__(self) -> None:
        self.root_node = None

    def append_node(self,list):
        new_node = Node(list)

        if self.root_node == None:
            self.root_node = new_node
        else:
            current_node  = self.root_node
            print(f" {self.root_node.list} ")
            while True:
                current_node.next_node = new_node
                print(f" {current_node.next_node.list}")

                if current_node.next_node == None:
                    current_node.next_node = new_node
                    break

                else:
                    current_node = current_node.next_node
                    break
                    


# Defining the root_node value
        if self.root_node == None:
            self.root_node = self.new_node

        



    def find_node():
        None