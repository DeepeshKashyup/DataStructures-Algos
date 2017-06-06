class queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        x=""
        for i in self.items:
            x=x+str(i)+" "
        return x
    
q = queue()

print q.isEmpty()

q.enqueue(4)

print q

q.enqueue('dog')

print q

q.enqueue(True)

print q

print q.size()

print q.isEmpty()

q.enqueue(8.4)

print q

print q.dequeue()

print q

print q.size()
