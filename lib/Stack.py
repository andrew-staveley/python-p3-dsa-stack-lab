class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        else:
            return True

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
            return self.items
    

    def pop(self):
        if len(self.items) > 0:
            return (self.items).pop(-1)
        else:
            return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        else:
            return False

    def search(self, target):
        counter = 0
        end_result = False
        stack = reversed(self.items)
        for number in stack:
            if number == target:
                end_result = True
                return counter
            else:
                counter += 1
        if end_result == False:
            return -1
        else:
            pass
            