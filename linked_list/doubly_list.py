class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleyLinkedList:
    def __init__(self):
        self.head : ListNode = None

    def print(self):
        current = self.head
        while current is not None:
            print(current.val, end= " ")
            current = current.next
        print("")

    def insert_at_beggining(self, val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else: 
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, val):
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None: 
                current = current.next
            current.next = node
            node.prev = current
    
    def delete_at_beginning(self):
        if self.head is not None:
            self.head = self.head.next

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
        
    
def main():
    dd = DoubleyLinkedList()
    dd.insert_at_beggining(19)
    dd.insert_at_beggining(20)
    dd.insert_at_beggining(2)
    dd.insert_at_beggining(3)
    dd.insert_at_end(12)
    dd.insert_at_end(11)
    print("Size {0}".format(dd.length()))
    dd.print()
    print("Size {0}".format( dd.length()))
    dd.delete_at_beginning()
    dd.delete_at_beginning()
    print("Size {0}".format( dd.length()))



if __name__ == "__main__":
    main()
        

        

