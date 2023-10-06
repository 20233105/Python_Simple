# 문제 2) 1~100까지 더해서 총합을 계산하세요.
# - for문
sum = 0
for a in range(1, 101):
    sum += a
print(f"총합(for): {sum}")
# - while문
b = 0
sum2=0
while(b<=100):
    sum2 += b
    b+=1
print(f"총합(while): {sum2}")