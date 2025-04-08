a = 1000
b = 4

count_arr = [0] * 10
while a/b >= 1 :
    a = a//b
    count_arr[a%b] += 1

print(count_arr)

