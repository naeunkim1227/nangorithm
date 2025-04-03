"""
1-9 까지 각 몇번 나왔는지를 출력하시오.
"""

n = int(input())
arr = list(map(int,input().split()))

count_arr = [0 for _ in range(9)]

for i in range (9) :
    for elem in arr :
        if i + 1 == elem :
            count_arr[i] += 1

for i in range (9) :
    print(count_arr[i])
