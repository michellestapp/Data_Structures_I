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

            while True:
                if current_node.next_node == None:
                    current_node.next_node = new_node
                    break

                else:
                    current_node = current_node.next_node
                        



    def find_node(self, data_to_find):

        current_node = Node(list)

        in_list = False
        if self.root_node == None:
            print(f" Search for node with value of {data_to_find}  \n")
            print(f"          Node Found: {in_list} \n")
        else:
            current_node  = self.root_node
            while in_list == False:
            
                if current_node.list == data_to_find:
                    in_list = True
                    
                    

                else:
                    current_node = current_node.next_node
                    if current_node == None:
                        break



            print(f"          Node Found: {in_list} \n")
            return in_list


        class BinaryNode:
            def __init__(self) -> None:
                self.root_node = None    


            def append_node(self,list):
                new_node = Node(list)

                if self.root_node == None:
                    self.root_node = new_node

                else:
                    current_node  = self.root_node

                    while True:

                        holding_node = new_node

                        if holding_node <= current_node: 

                            current_node.next_node = holding_node       

                        if current_node.next_node == None:
                            current_node.next_node = new_node
                            break

                        else:
                            current_node = current_node.next_node
                                
                        


         
