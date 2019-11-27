# arr = [5, 5, 10, 100, 10, 5]
# n = 6


n = int(input())
inp = input().strip().split()
arr = []
for i in inp:
	arr.append(int(i))

def prettyFlowers(arr , n):
	result = [[1 for i in range(2)] for i in range(n)] 
	res = 1

	for i in range(1 , n):
		for j in range(i):

			if (arr[j] < arr[i] and result[i][0] < result[j][1] + 1): 
				result[i][0] = result[j][1] + 1

			if( arr[j] > arr[i] and result[i][1] < result[j][0] + 1): 
				result[i][1] = result[j][0] + 1

	if (res < max(result[i][0], result[i][1])): 
		 res = max(result[i][0], result[i][1])

	return res

result = prettyFlowers(arr , n)
print( n - result)