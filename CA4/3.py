from ctypes import c_longlong as ll

def SumOfSubsets(arr): 
    Allsums = []
    for number in arr:
        Placeholder = Allsums[:]
        Allsums.append(number)
        for sum in Placeholder:
            Allsums.append(sum + number)
    return(Allsums)

acid = []
base = []

n = int(input())
for i in range(n):
    inp = list(input().split())
    temp = int(inp[1]) * int(inp[2])

    if(inp[0] == "acid"):
        acid.append(temp)
    else:
        base.append(temp)
    
AcidList = SumOfSubsets(acid)
BaseList = SumOfSubsets(base)

# print(AcidList)
# print(BaseList)

found = False
for acids in AcidList:
    if acids in BaseList:
        found = True
        print("yes")
        break

if(found == False):
    print("no")



