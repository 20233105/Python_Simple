# Python - pymysql ----- Database

# DB: MariaDB
#   - type: 관계형 데이터베이스(DB)

# **root 계정
# - 신급 권한을 가지는 계정
# - RDB는 반드시 root 계정 생성
# - "DB 관리자" -> root 사용 X, NEW 계정(권한을 많이 부여함)

# 예) 문서확인 불가(엑세스 거부됨)
# 신입 사원 -> 회원 가입 개발 -> DB 계정 생성(권한: 회원 테이블 읽기, 쓰기)


import pymysql


def connection():
    try:
        conn = pymysql.connect(
            host="123.0.0.1",
            port=3306,
            user="root",
            password="12341234",
            db="simple",
            charset="utf8",
            autocommit=True,
            cursorclass=pymysql.cursoors.DictCursor
        )
    except pymysql.Error as e:
        print(f"MARIADB 연결 실패{e}")