# 문제1) 사용자가 입력한 단수를 출력하는 코드
#dan = int(input("단수: "))
#for i in range(1, 10):
#    print(f"{dan}x{i}={dan*i:}")
# 문제2) 2단부터 9단까지 출력(중첩 for문)
# for i in range(2, 10):
    # for j in range(1, 10):
        # if(j == 1):
           # print(f"===={i}단====")
        # print(f"{i}x{j}={i*j}")
# 문제3) list a 의 평균값을 계산하세요.
# a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
# sum = 0
# for i in range(0, len(a)):
  #   sum += a[i]
# result = sum/len(a)
# print(round(result, 2))

# 문제4) list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]
num_min = b[0]
for num in b:
    if(num<num_min):
        num_min=num
num_min=b[0]    #22
for x in b:
    if(x < num_min):
        num_min = x

print(f"최솟값: {num_min}")  # 1 출력

# 문제 5)list c의 최솟값, 최댓값 찾기

c = [2, 5, 7, 1, 8]
num_min = c[0]
for x in c:
    if(x < num_min):
        num_min = x
num_max = c[0]
for y in c:
    if(num_max < y):
        num_max = y
print(f"최솟값:{num_min}")
print(f"최댓값:{num_max}")
