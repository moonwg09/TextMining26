import myTest

name = "hello"

print(name)

myTest.hello()
myTest.prnMsg(name)
print(myTest.myTest_msg)

from myTest2 import hello

hello()
# myTest2.prnMsg("good!!!") 특정함수만 가져왔기 때문에 실행안된다

