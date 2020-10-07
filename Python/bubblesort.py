def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(n-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]

a = [10,6,15,45,2 ,33] 

print(a)
bubbleSort(a)
print(a)
