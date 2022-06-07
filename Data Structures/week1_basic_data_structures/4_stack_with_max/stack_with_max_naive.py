#python3
import sys
from copy import copy

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__stack) >= 2:
            if (self.__stack[-1] >= self.__stack[-2]) and (self.__stack[-1] >= self.__max_stack[-1]):
                self.__max_stack.append(self.__stack[-1])
        else:
            self.__max_stack.append(self.__stack[0])

    def Pop(self):
        assert(len(self.__stack))
        #self.__stack.pop()
        if self.__stack[-1] == self.__max_stack[-1]:
            self.__stack.pop()
            self.__max_stack.pop()
        else:
            self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        if len(self.__stack) >= 2:
            max_element = self.__max_stack[-1]
            return (max_element)
        else:
            return self.__stack[0]
        #return max(self.__stack)


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries =  int(sys.stdin.readline()) #int(input())
    for _ in range(num_queries):
        query = sys.stdin.readline().split() #input().split() 

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
