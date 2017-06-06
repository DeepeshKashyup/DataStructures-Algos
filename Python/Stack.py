class stack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items == []
        
    def push(self,item):
        return self.items.append(item)

    def pop(self):
        n= len(self.items)-1
        return self.items.pop(n)


    def peek(self):
        n= len(self.items)-1
        return self.items[n]

    def size(self):
        return len(self.items)

    def __str__(self):
        x = ""
        for i in self.items:
            x=x+str(i)+" "
        return x
obj = stack()

obj.push(1)

obj.push("Hi")

obj.push(2)

print obj.size()

obj.push(3)
print obj

print obj.pop()

print obj
