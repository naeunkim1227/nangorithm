"""
1.짝수일 때 2로 나눈 나머지,홀수일 때 3을 더해 출력하라, 단 배열을 사용할 것.
"""

arr = list(map(int,input().split()))

arr2 = []
for elem in arr :
    if elem == 0 :
        break
    arr2.append(elem)


for elem in arr2 :
    if elem % 2 == 0 :
        print(elem // 2,end =" ")
    else :
        print(elem + 3,end=" ")