# 패키지 만들기 실습(package_test.py 파일 및 my_package 패키지 생성 후 실습)
# from 패키지 import 모듈 (ex. from my_package import sum)
from my_package import sum, sub

x = sum.sum_ab(1, 2)
print(x)

y = sub.sub_ab(3, 1)
print(y)


# from 패키지.모듈 import 함수, 클래스 (ex. from my_package.sum import sum_ab)
# 이때 모든 py파일을 읽어와서, 그 안의 구문들을 모두 읽어온다
#
from my_package.sum import sum_ab, Calculator, print_name
from my_package.sub import sub_ab


# __name__ ? => 현재 모듈의 이름을 담고 있는 (내장) 변수 -> 모듈의 이름이 저장되는 변수
# 현재 모듈 이름은 package_test인데 왜 __main__?
# -> 현재 실행한 파일 이름은 package_test라서 실제 모듈의 이름이 아닌 __main__이 담겨져있음
# if __name__ == '__main__':처럼 __name__ 변수의 값이 '__main__'인지 확인하는 코드는 현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업입니다.
# 즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도입니다.
# https://dojang.io/mod/page/view.php?id=2448
if __name__ == '__main__':
    x2 = sum_ab(3, 4)
    y2 = sub_ab(4, 1)
    print(f"x2: {x2}, y2: {y2}")

    c = Calculator(1, 2)
    print(f"c.sum = {c.sum()}")

    print(f"package_test.py의 __name__: {__name__}")
    print_name()


