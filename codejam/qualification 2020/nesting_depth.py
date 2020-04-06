#python2.7
T = int(raw_input())

for t in range(1,T+1):
        S = map(int, list(raw_input()))

        output = "(" * S[0] + str(S[0])
        for i,s in enumerate(S[1:]):
                prev = S[i]
                if s > prev:
                        output += "(" * (s-prev)
                elif s < prev:
                        output += ")" * (prev-s)
                output += str(s)
        output += ")" * S[-1]
        print("Case #{}: {}".format(t,output))
