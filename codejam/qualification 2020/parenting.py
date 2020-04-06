#python2.7
T = int(raw_input())

for t in range(1,T+1):
        N = int(raw_input())
        activities = list()
        for n in range(N):
                activity = tuple(map(int,raw_input().split()))
                activities.append((n,activity))

        original = activities[:]
        activities.sort(key = lambda x: x[1][0])
        activ_dict = dict()
        #print(original)
        #print(activities)

        C = 0
        J = 0
        output = ""

        while len(activities) > 0:
                a = activities.pop(0)
                #print(a)
                if a[1][0] >= C: C = 0
                if a[1][0] >= J: J = 0

                if C == 0:
                        C = a[1][1]
                        activ_dict[a] = "C"
                        #output += "C"

                elif J == 0:
                        J = a[1][1]
                        activ_dict[a] = "J"
                        #output += "J"
                else:
                        output = "IMPOSSIBLE"
                        break

        if output == "":
                for elem in original:
                        output += activ_dict[elem]

        print("Case #{}: {}".format(t,output))
