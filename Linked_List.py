class Node:
    def __init__(self,data_given):
        self.data= data_given
        self.next_location = None

class Linked_list:
    def __init__(self):
        #empty list
        self.head= None # loaction of 1 st node stored here
        #number of nodes
        self.n=0

    def __len__(self): # len() funtion 
        return self.n
    
    def insert_head(self,value):
        #creation of new node
        new_node=Node(value) # Node(value) this contains the storage loaction of new node with value as "value"
        # assieging next loaction from last node 
        new_node.next_location=self.head
        # assinigng new head
        self.head=new_node
        #incrementing the size 
        self.n+=1
    
    def __str__(self): # funtion for print 
        curr = self.head
        temp=""
        while curr!= None:
            temp+=str(curr.data) + "->" 
            curr = curr.next_location
        return temp[:-2]
    
    def append(self,value): # to append() funtion 
        curr=self.head
        while curr.next_location != None:
            curr = curr.next_location
        new_node=Node(value)
        curr.next_location = new_node
        

if __name__=="__main__":
    my_list=Linked_list()
    my_list.insert_head(10)
    my_list.insert_head(20)
    my_list.append(30)
    my_list.insert_head(40)
    print(my_list)
