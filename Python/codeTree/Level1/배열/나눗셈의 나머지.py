"""
나눗셈의 나머지 갯수를 카운트 하고 그 값을 제곱한 뒤 합을 구하라
"""

arr = input().split()

a = int(arr[0])
b = int(arr[1])


count_arr = [0] * 10

while a >= 1:
    r = a % b
    count_arr[r] += 1
    a = a // b

val = 0
for i in range(10):
    if count_arr[i] > 0:
        val += count_arr[i] ** 2


print(val)