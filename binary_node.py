

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None





class BinaryNode:
    def __init__(self,root_node) -> None:
        self.root_node = Node(root_node)

    def insert_node(self,data):
        new_node = Node(data)

        current_node = self.root_node
        while True:
            if new_node.data <= current_node.data:
                print('Add left node')
            
                if current_node.left == None:
                    current_node.left = new_node
                    print(current_node.left.data)
                    break

                else:
                    current_node = current_node.left
                
            else:
                print('Add right node')
                if current_node.right == None:
                    current_node.right= new_node
                    print(current_node.right.data)
                    break

                else:
                    current_node = current_node.right
                    
    def search_for_node():
        None

 
