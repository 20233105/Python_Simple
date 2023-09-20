# 컬렉션 타입
# - 변수 하나에 값을 여러개 저장
# - 실질적으로 변수에 컬렉션 1개가 저장
# - 리스트(list), 튜플(tuple), 딕트(dictionary), 세트(set)

# 1.리스트(list)
# - 시퀀스 자료형(연속 된 값 저장)
# - index 사용(Slicing 가능)
# - 대괄호 사용 []
# - 정렬 가능
# - mutable(생성 된 후 변경 가능)
# - packing과 unpacking 가능
# - 멤버함수: append(), extend(), insert(), remove(), pop(), index(), sorted(), 등등
# * 2차원 리스트는 표(table)과 동일한 형태

list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 5, 3.14, [1, 2, 3]]

# packing and unpacking
list_d = ["A", "B", "C"]    # packing
a, b, c = list_d    # unpacking

# append(값) : 리스트의 맨 마지막에 값을 추가
a = [1, 2, 3]
a.append(4)
print(a)
# insert() : 리스트의 원하는 인덱스에 값을 추가
b = [1, 2, 3]
b.insert(1, 9)
print(b)

# extend(리스트) : 리스트와 리스트를 병합
a = [1, 2, 3]
b = [3, 4, 5]
# a.extend(b)
# print(a)
c = a+b
print(c)

# remove(값) : 리스트 내 원소를 값으로 삭제
# pow(인덱스) : 리스트 내 원소를 인덱스로 삭제
abc = [1, 2, 3, 4, 5]
abc.remove(3)   # 3이라는 값을 의미
print(abc)
abc.pop(0)  # 0번째 인덱스를 의미
print(abc)
e = abc.pop(0)
print(abc)
print(e)

# index() : ()안의 값의 인덱스를 출력
a = ["A", "B"]
print(a.index("B"))

# sort() and sorted() : 리스트 안의 원소들을 정렬
# - sort() : 원본값 자체를 정렬(원본값 상실) X
# - sorted() : 원본값을 복제해서 정렬(원본값 유지)
a = [95, 1, 3, 55, 27, 45]
b = sorted(a)   # 디폴트: 오름차순
c = sorted(a, reverse=True)
print(a)
print(b)
print(c)