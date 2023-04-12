

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


        # if self.root_node == None:
        #     self.root_node = new_node
        #     print(f" Root node is {self.root_node.data}")
        current_node = self.root_node
        while True:
            if new_node.data <= current_node.data:
                print('Add left node')
            
                if current_node.left == None:
                    current_node.left = new_node
                    print(current_node.left.data)
                    print(f' Node {new_node.data} updated with a left of {current_node.left.data} and a right of {current_node.data} ')
                    break

                else:
                    current_node = current_node.left
                
            else:
                print('Add right node')
                if current_node.right == None:
                    current_node.right= new_node
                    print(current_node.right.data)
                    print(f' Node {new_node.data} updated with a left of {current_node.data} and a right of {current_node.right.data} ')
                    break

                else:
                    current_node = current_node.right

        

# class BinaryNode:
#     def __init__(self,root_node) -> None:
#         self.root_node = Node(root_node)

#     def insert_node(self,data):
#         new_node = Node(data)

#         current_node = self.root_node

#         while True:
#             if new_node.data <= current_node.data:
            
#                 if current_node.left == None:
#                    current_node.left = new_node
#                    new_node.right = current_node.data
                   
#                    print(f" Node with data {new_node.data} created")
                
#                    break

#                 else:
                    
#                     current_node = current_node.left
                
#             else:

#                 if current_node.right == None:
#                    current_node.right = new_node
#                    new_node.left = current_node.data
                 
#                    print(f" Node with data {new_node.data} created")
#                    break

#                 else:
                   
#                     current_node = current_node.right
                

#         print(f' Node {new_node.data} updated with a left of {new_node.left} and a right of {new_node.right} ')  

                  
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
                    
                    break
            return in_data_set


 
