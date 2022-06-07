#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

# def IsBinarySearchTree(tree):
#   # Implement correct algorithm here
#   return True


# def main():
#   nodes = int(sys.stdin.readline().strip())
#   tree = []
#   for i in range(nodes):
#     tree.append(list(map(int, sys.stdin.readline().strip().split())))
#   if IsBinarySearchTree(tree):
#     print("CORRECT")
#   else:
#     print("INCORRECT")

# threading.Thread(target=main).start()

# import sys, threading
# sys.setrecursionlimit(10**6) # max depth of recursion
# threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:
    def read(self):
        self.n = int(sys.stdin.readline()) #int(input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split()) #map(int, input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
            
    def inorder(self,root,result):
        if self.left[root] != -1:
            self.inorder(self.left[root],result)
        result.append(self.key[root])
        if self.right[root] != -1:
            self.inorder(self.right[root],result)            

    def inOrder(self):
        self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
        self.inorder(0,self.result)
                
        return self.result
    
    def IsBinarySearchTree(self):
        # Implement correct algorithm here
        if self.n==0:
            return True
        else:
            l_bt = self.inOrder()
            cond = True
            i = 0
            while cond and (i+1<len(l_bt)):
                if l_bt[i]<=l_bt[i+1]:
                    i+=1
                else:
                    cond = False
            return cond 
    
            
def main(): #if __name__ == "__main__":
    tree = Tree()
    tree.read()
    #print(tree.key, tree.left, tree.right)
    #print(tree.IsBinarySearchTree())

    if tree.IsBinarySearchTree():
      print("CORRECT")
    else:
      print("INCORRECT")

threading.Thread(target=main).start()
