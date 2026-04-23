# 두개의 정수를 입력받아서 두 정수의 사칙연산을 출력

num1 = input('숫자를 입력하세요 : ') #입력함수인 input을 이용해서 숫자를 입력받는다(num1)
num1 = int(num1) # input함수는 문자열만 반환하여서 정수형(int)으로 변경해 주어야한다


num2 = input('숫자를 입력하세요 : ') #입력함수인 input을 이용해서 숫자를 입력받는다(num1)
num2 = int(num2) # input함수는 문자열만 반환하여서 정수형(int)으로 변경해 주어야한다


addNum = num1 + num2
subNum = num1 - num2
mulNum = num1 * num2
divNum = num1 / num2

print(num1, '+', num2, '=', addNum, sep="", end=' ') # sep는 쉼표 사이 구분(기본값은 띄어쓰기), end는 줄간의 띄어쓰기 enter값이 기본
print(num1, '-', num2, '=', subNum)
print(num1, '*', num2, '=', mulNum)
print(num1, '/', num2, '=', divNum) # 사칙 연산 출력하기

#split()는 문자열 구분하기 위한 함수 ex '12 6' => '12' '6'
