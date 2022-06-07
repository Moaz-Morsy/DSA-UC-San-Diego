#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# # def IsBinarySearchTree(tree):
# #   # Implement correct algorithm here
# #   return True


# # def main():
# #   nodes = int(sys.stdin.readline().strip())
# #   tree = []
# #   for i in range(nodes):
# #     tree.append(list(map(int, sys.stdin.readline().strip().split())))
# #   if IsBinarySearchTree(tree):
# #     print("CORRECT")
# #   else:
# #     print("INCORRECT")

# # threading.Thread(target=main).start()

# class Tree:
#     def read(self):
#         self.n = int(sys.stdin.readline()) #int(input())
#         self.key = [0 for i in range(self.n)]
#         self.left = [0 for i in range(self.n)]
#         self.right = [0 for i in range(self.n)]
#         for i in range(self.n):
#             [a, b, c] = map(int, sys.stdin.readline().split()) #map(int, input().split())
#             self.key[i] = a
#             self.left[i] = b
#             self.right[i] = c
#     def inorder(self,root,result):
#         if self.left[root] != -1:
#             self.inorder(self.left[root],result)
#         result.append((self.key[root],self.left[root],self.right[root]))
#         if self.right[root] != -1:
#             self.inorder(self.right[root],result)            

#     def inOrder(self):
#         self.result = []
#     # Finish the implementation
#     # You may need to add a new recursive method to do that
#         self.inorder(0,self.result)
                
#         return self.result
    
#     def IsBinarySearchTree(self):
#         # Implement correct algorithm here
#         if self.n<=1: #(self.n==0) or (self.n==1):
#             return True
#         else:
#             l_bt = self.inOrder()
#             cond = True
#             i = 0
#             while cond and (i<len(l_bt)):
#               if (self.left[i]!=-1) and (self.key[i]==self.key[self.left[i]]):
#                 cond = False
#               else:
#                 i+=1
#             i = 0
#             while cond and (i+1<len(l_bt)):
#               if l_bt[i][0]<=l_bt[i+1][0]:
#                 i+=1
#               else:
#                 cond = False
#             return cond

# sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**25)  # new thread will get stack of such size

# class Node:
#     def __init__(self,a,b,c):
#         self.key = a
#         self.left= -1
#         self.right= -1
#         self.left_index= b
#         self.right_index= c
# class Tree:
#     def insert_node(self, root, key, b, c):
#         # Find the correct location and insert the node
#         if root == -1 :
#             return Node(key, b, c)
#         elif key < root.key:
#             root.left = self.insert_node(root.left, key, b, c)
#         else:
#             root.right = self.insert_node(root.right, key, b, c)
#         return root
    
#     def read(self):
#         self.n = int(sys.stdin.readline().strip())#int(input())
#         self.key = [0 for i in range(self.n)]
#         self.left = [0 for i in range(self.n)]
#         self.right = [0 for i in range(self.n)]
#         self.root = -1 #None
#         for i in range(self.n):
#             [a, b, c] = map(int, sys.stdin.readline().split())#map(int, input().split())
#             self.key[i] = a
#             self.left[i] = b
#             self.right[i] = c
#             self.root = self.insert_node(self.root, a, b, c)
            
#     def inorder(self,root):
#         if self.left[root] != -1:
#             self.inorder(self.left[root])
#         self.bt.append((self.key[root],self.left[root],self.right[root]))
#         if self.right[root] != -1:
#             self.inorder(self.right[root])     
#     def inorder_n(self,root):
#         if root != -1:
#           # # Traverse root
#           # self.bt_n.append((root.key,root.left_index,root.right_index))
#           # Traverse left
#           self.inorder_n(root.left)
#           # Traverse root
#           self.bt_n.append((root.key,root.left_index,root.right_index))
#           # Traverse right
#           self.inorder_n(root.right)
# #     def inOrder(self):
# #         self.bt = []
# #         self.bt_n = []
# #         self.inorder(0)
# #         self.inorder_n(self.root)
# #         return self.result
    
#     def IsBinarySearchTree(self):
#         # Implement correct algorithm here
#         if self.n<=1:
#           return True
#         else:
#           self.bt = []
#           self.bt_n = []
#           self.inorder(0)
#           self.inorder_n(self.root)
#           cond = True
#           i = 0
#           # 1st_root = self.bt_n[0]
#           while cond and (i+1<len(self.bt)):
#             if (self.bt[i][1]==self.bt_n[i][1]) and (self.bt[i][0]==self.bt_n[i][0]):
#               i+=1
#             else:
#               cond=False
#           return cond
#           # for i in range(len(self.bt)):
#           #   if self.bt[i][0]==self.bt_n[i][0]:
#           #     if (self.bt[i][1]==self.bt_n[i][1]) and (self.bt[i][2]==self.bt_n[i][2]):
#           #       continue
#           #     else:
#           #       cond=False
#           #       break
#           #   else:
#           #     cond=False
#           #     break
#           # return cond
    
            
# if __name__ == "__main__":
#     tree = Tree()
#     root = tree.read()
    
#     #print(tree.key, tree.left, tree.right)
#     #print(tree.IsBinarySearchTree())
# #     print(tree.IsBinarySearchTree())
#     if tree.IsBinarySearchTree():
#         print("CORRECT")
#     else:
#         print("INCORRECT")

# #threading.Thread(target=main).start()

class Node:
  def __init__(self,a,b,c):
    self.key = a
    self.left= b
    self.right= c

class Tree:
    
    def read(self):
        self.n = int(input())
        self.roots = [0 for i in range(self.n)]
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
            self.roots[i] = Node(a,b,c)
    def IsBinarySearchTree(self,root,mini,maxi):
        # Implement correct algorithm here
        if self.n<=1:
            return True
        else:
          if (root==-1):
              return True
          if (self.key[root]<mini) or (self.key[root]>=maxi):
            return False
          return self.IsBinarySearchTree(self.left[root],mini,self.key[root]) \
           and self.IsBinarySearchTree(self.right[root],self.key[root],maxi)
          
          # result = [(mini, self.roots[0], maxi)]
          # while result:
          #     mini, root, maxi = result.pop()
          #     if root.key < mini or root.key >= maxi:
          #         return False
          #     if root.left != -1:
          #         result.append((mini, self.roots[root.left], root.key))
          #     if root.right != -1:
          #         result.append((root.key, self.roots[root.right], maxi))
          # return True
          # cond = True
          # while cond:
          #   if self.key[root] < mini or self.key[root] >= maxi:
          #     cond = False
          #     break
          #   if (self.left[root] == -1) and (self.right[root] == -1):
          #     break
          #   if self.left[root] != -1:
          #     maxi = self.key[root]
          #     root = self.left[root]
          #   if self.right[root] != -1:
          #     mini = self.key[root]
          #     root = self.right[root]
          # return cond
        
# if __name__ == "__main__":
#     tree = Tree()
#     root = tree.read()
    
#     #print(tree.key, tree.left, tree.right)
#     #print(tree.IsBinarySearchTree())
#     print(tree.IsBinarySearchTree(0,float('-inf'),float('inf')))

            
def main(): #if __name__ == "__main__":
    tree = Tree()
    tree.read()
    #print(tree.key, tree.left, tree.right)
    #print(tree.IsBinarySearchTree())

    if tree.IsBinarySearchTree(0,float('-inf'),float('inf')): #tree.IsBinarySearchTree():
      print("CORRECT")
    else:
      print("INCORRECT")

threading.Thread(target=main).start()
