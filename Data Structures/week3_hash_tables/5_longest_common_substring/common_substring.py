# python3

import sys
# from collections import namedtuple

# Answer = namedtuple('answer_type', 'i j len')

# def solve(s, t):
# 	ans = Answer(0, 0, 0)
# 	for i in range(len(s)):
# 		for j in range(len(t)):
# 			for l in range(min(len(s) - i, len(t) - j) + 1):
# 				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
# 					ans = Answer(i, j, l)
# 	return ans

# for line in sys.stdin.readlines():
# 	s, t = line.split()
# 	ans = solve(s, t)
# 	print(ans.i, ans.j, ans.len)

def PrecomputeHashes(s, p, x):
        H = [0]*(len(s)+1)
        for i in range(1,len(s)+1):
            H[i] = (x*H[i-1]+ord(s[i-1]))%p#(((x*H[i-1]+ord(s[i-1]))%p)+p)%p
        return H

def check_hash_value(h_S, h_T, p, x, l):
    
    # x = 263
    # p_1 = (10**12)+7
    # p_2 = (10**9)+9
    # y_1 = pow(x, l, p)
    # y_2 = pow(x, l, p)
    y = pow(x, l, p)
    a = 0
    b = 0
    H_S = {}#[]
    H_T = 0
    while a+l<len(h_S):
        H_S[(h_S[a+l]-((y)*h_S[a]))%p] = a#H_S.append((h_S[a+l]-((y)*h_S[a]))%p)
        a += 1
    while b+l<len(h_T):
        #H_T_p_2.append((h_T[b+l]-((y_2)*h_T[b]))%p_2)
        H_T = (h_T[b+l]-((y)*h_T[b]))%p
        if H_S.get(H_T)!=None:
            return(True, H_S.get(H_T), b)
        else:
            b+=1
        #b += 1
        # for a in range (len(H_S)):
        #     if H_S[a] == H_T:
        #         return (True, a, b)
        # b += 1
        # if H_T_p_2 in H_S_p_1:
        #     return (True, H_S_p_1.index(H_T_p_2), b)
        # else:
        #     b += 1
    
    return (False, 0, 0)#(H_S_p_1, H_T_p_2)#(False, 0, 0)#((H_a_p_1==H_b_p_1) and (H_a_p_2==H_b_p_2), a, b)

def solve(h_S_1, h_T_1, h_S_2, h_T_2,  l):
    x = 263
    p_1 = (10**12)+7
    p_2 = (10**12)+9
    ans = Answer(0, 0, 0)
    low = 0
    high = l
    while low <= high:
        mid = low + ((high-low) // 2)
        check_1, i, j = check_hash_value(h_S_1, h_T_1, p_1, x, mid)
        check_2, i, j = check_hash_value(h_S_2, h_T_2, p_2, x, mid)
        if (check_1 and check_2): #and (i_1==i_2) and (j_1==j_2):
            ans = Answer(i, j, mid)
            low = mid+1
        else:
            high = mid-1
    return ans
    

from collections import namedtuple
Answer = namedtuple('answer_type', 'i j len')

x = 263
p_1 = (10**12)+7
p_2 = (10**12)+9
    
# while True:
#     two_strings = input().split()
#     if two_strings == []:
#         break
#     else:
#         s ,t = two_strings[0],two_strings[1]
#         if len(s)<=len(t):
#             l = len(s)
#             h_S_1 = PrecomputeHashes(s, p_1, x)
#             h_T_1 = PrecomputeHashes(t, p_1, x)
#             h_S_2 = PrecomputeHashes(s, p_2, x)
#             h_T_2 = PrecomputeHashes(t, p_2, x)
#             ans = solve(h_S_1, h_T_1, h_S_2, h_T_2, l)
#             print(ans.i, ans.j, ans.len)
#             #print(check_hash_value(h_S, h_T, 1))#(ans.i, ans.j, ans.len)
#             #print(h_S)
#             #print(h_T)
#         else:
#             l = len(t)
#             h_S_1 = PrecomputeHashes(t, p_1, x)
#             h_T_1 = PrecomputeHashes(s, p_1, x)
#             h_S_2 = PrecomputeHashes(t, p_2, x)
#             h_T_2 = PrecomputeHashes(s, p_2, x)
#             ans = solve(h_S_1, h_T_1, h_S_2, h_T_2, l)
#             print(ans.i, ans.j, ans.len)

for line in sys.stdin.readlines():
    s, t = line.split()
    if len(s)<=len(t):
        l = len(s)
        h_S_1 = PrecomputeHashes(s,p_1,x)
        h_T_1 = PrecomputeHashes(t,p_1,x)
        h_S_2 = PrecomputeHashes(s,p_2,x)
        h_T_2 = PrecomputeHashes(t,p_2,x)
        ans = solve(h_S_1,h_T_1,h_S_2,h_T_2,l)
        print(ans.i,ans.j,ans.len)
    else:
        l = len(t)
        h_S_1 = PrecomputeHashes(t,p_1,x)
        h_T_1 = PrecomputeHashes(s,p_1,x)
        h_S_2 = PrecomputeHashes(t,p_2,x)
        h_T_2 = PrecomputeHashes(s,p_2,x)
        ans = solve(h_S_1,h_T_1,h_S_2,h_T_2,l)
        print(ans.j,ans.i,ans.len)


# for line in sys.stdin.readlines():
# 	s, t = line.split()
# 	if len(s)<=len(t):
# 		l = len(s)
# 		h_S = PrecomputeHashes(s,p_1,x)
#         h_T = PrecomputeHashes(t,p_2,x)
#         ans = solve(h_S, h_T, l)
#         print(ans.i, ans.j, ans.len)
#     else:
#         l = len(t)
#         h_S = PrecomputeHashes(t, p_1, x)
#         h_T = PrecomputeHashes(s, p_2, x)
#         ans = solve(h_S, h_T, l)
#         print(ans.i, ans.j, ans.len)
# 	# ans = solve(s, t)
# 	# print(ans.i, ans.j, ans.len)