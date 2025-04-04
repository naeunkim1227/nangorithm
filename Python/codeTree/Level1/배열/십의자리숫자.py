"""
0이 나오기 전까지 무작위로 주어진 두자리 숫자에 대하여, 일의 자리 숫자가 몇개씩 나왔는지 카운트하는 코드를 작성하라.
"""
arr = list(map(int,input().split()))

count_arr = [0] * 10
for i in range (len(arr)) :
    if arr[i] == 0 :
        break
    elif arr[i] >= 10 :
        count_arr[arr[i]//10] += 1

for i in range(1,10) :
    print(f"{i} - {count_arr[i]}")