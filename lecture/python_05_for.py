# 제어문
# 1.조건문(if) switch, case(잘 안씀)
# 2.반복문(for, while)

# 반복문(Loop)
# -반복적인 작업을 가능하게 해주는 도구
# -list, str, tuple 등 컬렉션 아비의 아이템을 하나씩
#   순회하면서 사용 가능
# -특정 조건을 만족하는 경우(while)

# 반복 횟수 알고 있음 -> for
# 반복 횟수 모름 -> while

# for문 기본문법(list 활용)
for num in[1, 2, 3]:
    print(num)

# for(int i =0; i <= 9; i++)
# {
#   printf(i);
# }

# range() 함수
# -range(시작, 끝, 증감)
# -default 시작(0), 증감(+1)
# -range(3):        0, 1, 2
# -range(1, 10):        1, 2, 3, 4, 5, 6, 7, 8, 9
# -range(2, 5, 2):      2, 4

# range()함수를 활용해서 1~9까지 출력하는 for문
for i in range(1, 10):
    print(i)

# List를 활용한 for문
temp = ["A", "B", "C", "D", "E"]
for alpha in temp:
    print(alpha)

# enumerate() 함수
# - 반복 횟수(index) 정보를 사용 하고 싶을 때
# - 0번부터 시작
for i, alpha in enumerate(temp):
    print(i+1, alpha)

# dict를 활용한 for문
# -dict를 for로 출력 -> key 값만 출력
# -dict.keys(), dict.values(), dict.items()
temp = {"A": 1, "B": 2, "C": 3, "D": 4}
print("="*100)
for element in temp.values():
    print(element)
for key, value in temp.items():
    print(key)   # key
    print(value)   # value

# break: 즉시 반복문 탈출
# a를 출력하다가 3을 만나면 정지
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        break
    print(i)


# continue: 즉시 다음 반복으로 넘어가기
# 1~10까지 중 홀수만 출력

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print("="*100)
# 구구단 2단 코드
# 2x1=2... 2x9=18
for i in range(1,10):
    print(f"2x{i}={2*i}")

