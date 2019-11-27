# n = 2
# arr = [2]


n = int(input())
str = input()
arr = []

for i in range(0 , len(str)):
	arr.append(int(str[i]))


def reverseMergeSort(arr , n):
	indexes = []
	for i in range(1,n+1):
		indexes.append(i)

	temp = mergeSort(arr, indexes, 0 , n-1)

	a = [0] * n
	for i in range(0 , len(temp)):
		a[temp [i] - 1] = i+ 1
	checkSum(a)

def checkSum(arr):
	result = 1
	for i in range(0 , len(arr)):
		result = (31 * result + arr[i]) % 1000003
	print(result)

def merge(arr, indexes, l, m, r): 
	n1 = m - l + 1
	n2 = r - m 

	L = [0] * (n1) 
	R = [0] * (n2) 

	for i in range(0 , n1): 
		L[i] = indexes[l + i] 
  
	for j in range(0 , n2): 
		R[j] = indexes[m + 1 + j]

	i = 0
	j = 0

	k = l

	while i < n1 and j < n2 :
		if arr[0] == 1:
			indexes[k] = L[i]
			i += 1
		if arr[0] == 2:
			indexes[k] = R[j]
			j += 1
		k += 1
		del arr[0]

	while i < n1: 
		indexes[k] = L[i]
		k += 1
		i += 1

	while j < n2: 
		indexes[k] = R[j]
		k += 1
		j += 1

def mergeSort(arr, indexes, l,r): 
	if l < r: 
		m = int((l+(r-1))/2)
		mergeSort(arr,indexes, l, m) 
		mergeSort(arr,indexes, m+1, r) 
		merge(arr, indexes, l, m, r) 
	return indexes
  

reverseMergeSort(arr , n)