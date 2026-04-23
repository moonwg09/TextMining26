# 1~100점 사이의 성적을 입력받아 학점을 출력하는 코드를 작성

#성적입력()
def inputScore():
    num = int(input())
    return num

#성적으로학점구하는()
def getGrade(num):
    if num < 0 or num>100:
        print("잘못입력하셨습니다.")
        return 0
    else:
        if 90<=num<100:
            grade = 'A'
        elif 80<=num<90:
            grade = 'B'
        elif 70<=num<80:
            grade = 'C'
        elif 60<=num<70:
            grade = 'D'
        else:
            grade = 'F'

        return grade
    
#성적학점출력()
def printResult(num,grade):
    if grade == 0 : pass
    else:
        print(f'{num} 성적의 학점은 {grade} 이다')

# 리스트로 전달하는 것은 shallow copy의 형태를 취해서 주소값만 가지고 있다
def printStudent(list):
    print(f'{list[0]} 성적의 학점은 {list[1]}다')

num = inputScore()
grade = getGrade(num)
stuData = [num, grade]
printResult(num,grade)
printStudent(stuData)