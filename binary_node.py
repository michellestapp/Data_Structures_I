

class BinaryNode:
    def __init__(self) -> None:
        self.data = {}
        self.left = ''
        self.right = ''

    def insert_node(self,list):
        new_node = BinaryNode(list)

        if self.root_node == None:
            self.root_node = new_node
            print(f" Root node is {self.root_node.data}")

        else:
            current_node  = self.root_node

            while True:
                if new_node >= current_node:
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