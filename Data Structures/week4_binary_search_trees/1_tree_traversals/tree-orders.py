# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    # if self.n>=2:
    #   self.key[0] = self.key[0] + (2**31)

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

  def preorder(self,root,result):
    result.append(self.key[root])
    if self.left[root] != -1:
      self.preorder(self.left[root],result)
    if self.right[root] != -1:
      self.preorder(self.right[root],result)

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preorder(0,self.result)
                
    return self.result

  def postorder(self,root,result):
    if self.left[root] != -1:
      self.postorder(self.left[root],result)
    if self.right[root] != -1:
      self.postorder(self.right[root],result)
    result.append(self.key[root])

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postorder(0,self.result)
                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
