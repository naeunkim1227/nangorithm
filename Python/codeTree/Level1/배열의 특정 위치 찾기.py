
"""
1.짝수 번째로 입력된 값의 합
2.3의 배수 번째로 입력된 값의 평균
"""

#slice 사용
arr = list(map(int,input().split()))
filter_arr = arr[1::2]
filter_arr2 = arr[2::3]

print(f"{sum(filter_arr)} {sum(filter_arr2)/len(filter_arr2):.1f}")


#for문 사용
n = len(arr)
sum_val = 0
sum_val2 = 0
idx = 0;

for i in range(10):
    if (i+1)%2 == 0:
        sum_val+=arr[i]
    elif (i+1)%3 == 0:
        idx += 1
        sum_val2 += arr[i]

print(f"{sum_val} {sum_val2/idx:.1f}")