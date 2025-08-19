class ListNode: 
    def __init__(self, val= 0, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)
    

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        current = self.head
        print("Elements in List:")
        while current:
            print(current.val, end=" ")
            current = current.next
        print("")
    
    def append(self, val):
        # create a node 
        node = ListNode(val,None)
        if not self.head:
            self.head = node 
        else:
            ptr = self.head 
            next = ptr.next
            while next is not None:
                ptr = next
                next = next.next
            ptr.next = node
        

    def append_many(self, vals):
        for v in vals:
            self.append(v)   

    def search_linked_list(self, target):
        current = self.head
        
        while current and current.val !=  target:
            current = current.next
        
        if current is None: 
            return False
        else: 
            return True
        
    def find_length(self):
        counter = 0
        current = self.head
        while current != None: 
            counter += 1
            current = current.next
        return counter 
    
    def insert_at_beginning(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
    
    def insert_at_end(self, val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            current = self.head.next
            prev = self.head
            while current != None:
                prev = current
                current = current.next
            prev.next = node

    def delete_beginning(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
    
    #delete a particular element
    def delete_an_element(self, value):
        prev = None
        current = self.head
        while current != None and current.val != value:
            prev = current
            current = current.next
        if current != None:
             prev.next = current.next





        

def main():
    print("Hello Main")
    ll = LinkedList()
    ll.append_many([11,12,41,143])
    print("12 is present in system  {result}".format(result = ll.search_linked_list(12)))
    print("10 is present in system  {result}".format(result = ll.search_linked_list(10)))
    print("Length of List {0}".format(ll.find_length()))
    ll.insert_at_beginning(5)
    ll.insert_at_end(14)
    ll.print()
    ll.delete_beginning()
    ll.print()
    ll.delete_an_element(14)
    ll.print()
    

if __name__ == "__main__":
    main()





             

