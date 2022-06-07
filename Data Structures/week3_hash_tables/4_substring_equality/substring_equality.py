# python3

# import sys

# class Solver:
# 	def __init__(self, s):
# 		self.s = s
# 	def ask(self, a, b, l):
# 		return s[a:a+l] == s[b:b+l]

# s = sys.stdin.readline()
# q = int(sys.stdin.readline())
# solver = Solver(s)
# for i in range(q):
# 	a, b, l = map(int, sys.stdin.readline().split())
# 	print("Yes" if solver.ask(a, b, l) else "No")


class Solver:
    def __init__(self, s):
        self.s = s
    def PrecomputeHashes(self, p, x):
            H = [0]*(len(self.s)+1)
            for i in range(1,len(self.s)+1):
                # H[i] = (((x*H[i-1]+ord(self.s[i-1]))%p)+p)%p
                H[i] = (x*H[i-1]+ord(self.s[i-1]))%p
            return H
    def ask(self, h_a, h_b, a, b, l):
        x = 263
        p_1 = (10**9)+7
        p_2 = (10**9)+9
        # h_a = self.PrecomputeHashes(p_1, x)
        # h_b = self.PrecomputeHashes(p_2, x)
        y_1 = pow(x, l, p_1)
        y_2 = pow(x, l, p_2)
        H_a_p_1 = (h_a[a+l]-((y_1)*h_a[a]))%p_1
        H_b_p_1 = (h_a[b+l]-((y_1)*h_a[b]))%p_1
        H_a_p_2 = (h_b[a+l]-((y_2)*h_b[a]))%p_2
        H_b_p_2 = (h_b[b+l]-((y_2)*h_b[b]))%p_2
        return (H_a_p_1==H_b_p_1) and (H_a_p_2==H_b_p_2)
    
s = input()
q = int(input())
x = 263
p_1 = (10**9)+7
p_2 = (10**9)+9
solver = Solver(s)
h_a = solver.PrecomputeHashes(p_1, x)
h_b = solver.PrecomputeHashes(p_2, x)
# print(solver.PrecomputeHashes(p_1, x))
# print(solver.PrecomputeHashes(p_2, x))
for i in range(q):
    a, b, l = map(int, input().split())
    print("Yes" if solver.ask(h_a, h_b, a, b, l) else "No")
    
   