A = list(map(int, input().split()))

min_value = float('inf')
max_value = float('-inf')
min_index = -1
max_index = -1

for i in range(len(A)):
    if A[i] < min_value:
        min_value = A[i]
        min_index = i
    if A[i] > max_value:
        max_value = A[i]
        max_index = i
subarray_size = abs(max_index - min_index) + 1
print(subarray_size)
