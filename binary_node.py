

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
                    
    def search_for_node(self,search_value):

        current_node = Node(search_value)
        current_node = self.root_node
        in_data_set = False
        while in_data_set == False:

            if current_node.data == search_value:
                print('Node Found')
                in_data_set = True

            elif search_value < current_node.data:
                # Look left
                current_node = current_node.left
            
                if current_node == None:
                    # Not found
                
                    print(current_node)
                    
                    break
                
            else:
                current_node = current_node.right

                if current_node == None:
                    print(f' No more right numbers in list:  {current_node.data}')
                    break


 
