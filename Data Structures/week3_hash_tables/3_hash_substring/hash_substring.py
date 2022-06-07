# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

def RabinKarb(P,T):
    def AreEqual(s1,s2):
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return False
        return True

    def PolyHash(s,p,x):
        Hash = 0
        for c in reversed(s):
            Hash = (Hash * x + ord(c)) % p
        return Hash

    def PrecomputeHashes(T,P,p,x):
        H = [0]*(len(T)-len(P)+1)
        s = T[(len(T)-len(P)):]
        H[(len(T)-len(P))] = PolyHash(s,p,x)
        y = 1
        for i in range(len(P)):
            y=(y*x)%p
        for i in reversed(range(len(T)-len(P))):
            H[i] = (((x*H[i+1]+ord(T[i])-y*ord(T[i+len(P)]))%p)+p)%p
            # if (H[i]<0):
            #     H[i]+=p
            # H[i]=H[i]%p
        return H
    
    x = 263
    p = 1000000007
    result = []
    PHash = PolyHash(P,p,x)
    THash = PrecomputeHashes(T,P,p,x)
    for i in range(len(T)-len(P)+1):
        if THash[i]==PHash:
            if T[i:(i+len(P))] == P:
                result.append(i)
    return result

if __name__ == '__main__':
    # print_occurrences(get_occurrences(*read_input()))
    print_occurrences(RabinKarb(*read_input()))

