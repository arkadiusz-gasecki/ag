#only first data set

def is_palindromic(block):
    freq = {}
    for b in block:
        freq[b] = freq.get(b,0) + 1
        odd_values = 0
    for k,v in freq.items():
        if v % 2 != 0:
            odd_values += 1
            if odd_values > 1:
                return 0
    return 1

T = int(input())
answers = {}

for t in range(0,T):
    N,Q = map(int,input().split())
    block = input()
    for q in range(0,Q):
        L,R = map(int,input().split())
        #correct L and R to have actual index of the string
        #R does not need to be corrected as it will be used in slicing
        L -= 1
        #take substring
        answers[t] = answers.get(t,0) + is_palindromic(block[L:R])

for i in range(0,len(answers)):
    print("Case #{}: {}".format(i+1,answers[i]))
