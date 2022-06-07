# python3

class Dequeue:
    def __init__(self):
        self.items = []

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class StackWithMax():
    def __init__(self):
        self.stack = []
        self.max_stack = []
        
    def getstack(self):
        return self.stack

    def Push(self, a):
        if len(self.stack) >= 1:
            self.stack.append(a)
            if self.stack[-1] >= self.stack[-2]:
                if (self.stack[-1] > self.max_stack[0]):
                    #while (self.max_stack!=[]):
                    #    self.max_stack.pop()
                    #self.max_stack.clear()
                    del self.max_stack[:]
                    self.max_stack.append(self.stack[-1])
                elif (self.stack[-1] == self.max_stack[0]):
                    if len(self.max_stack)==1:
                        self.max_stack.append(self.stack[-1])
                    else:
                        while (self.stack[-1] > self.max_stack[-1]):
                            self.max_stack.pop()
                        self.max_stack.append(self.stack[-1])
                elif (self.stack[-1] < self.max_stack[0]):
                    while (self.stack[-1] > self.max_stack[-1]):
                        self.max_stack.pop()
                    self.max_stack.append(self.stack[-1])
            else:
                self.max_stack.append(self.stack[-1])
        else:
            self.stack.append(a)
            self.max_stack.append(a)
        
    def Pop(self):
        if self.stack[0] == self.max_stack[0]:
            self.stack.pop(0)
            self.max_stack.pop(0)
        else:
            self.stack.pop(0)
    
    def Max(self):
        return self.max_stack[0]



# def max_sliding_window(Q, sequence, w):
#     maximums = []
    
#     for i in range(0, w):
#         while (Q.items!=[]) and sequence[i] >= sequence[Q.items[-1]]:
#             Q.removeFront()
#         Q.addRear(i)
        
#     for i in range(w, len(sequence)):
        
#         maximums.append(sequence[Q.items[0]])
        
#         while (Q.items!=[]) and (Q.items[0] <= i-w):
#             Q.removeRear()
    
#         while (Q.items!=[]) and sequence[i] >= sequence[Q.items[-1]]:
#             Q.removeFront()
#         Q.addRear(i)

#     maximums.append(sequence[Q.items[0]])  

#     return maximums

def max_sliding_window(sequence, m):
    maximums = []
    i = 0
    Stack = StackWithMax()
    while i<len(sequence):
        if len(Stack.stack)!=m:
            Stack.Push(sequence[i])
            i += 1
        elif len(Stack.stack)==m:
            maximums.append(Stack.Max())
            Stack.Pop()
            Stack.Push(sequence[i])
            i += 1
    maximums.append(Stack.Max())

    return maximums

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    Queue = Dequeue()

    print(*max_sliding_window(input_sequence, window_size))
    #print(*max_sliding_window(Queue, input_sequence, window_size))
    #print(*max_sliding_window_naive(input_sequence, window_size))

