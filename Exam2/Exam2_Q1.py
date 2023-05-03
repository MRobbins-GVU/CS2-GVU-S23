
class SortedList:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items = [item] + self.items
        # TODO: add to this method so that it item goes to the correct location in the list. 
        #       you may use any of the sorting algorithms we have discussed, but do not use 
        #       the built in list.sort() method in Python
        
        
    def remove_item(self, item):
        # TODO: update this method so that it removes the item that is passed as a parameter,
        #       without using the existing list.remove() method in Python.
        self.items = self.items[:-1]
        
    def __str__(self):
        return str(self.items)
        
        


def main():
    #TODO: update main to test add and remove item multiple times (remember, you will not be able to call __init__ or __str__ directly).
    sortedList1 = SortedList()
    sortedList1.add_item(13)
    
    print(sortedList1)
    
    
    
    
main()
