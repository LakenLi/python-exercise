## 循环结构

### for-in 循环
如果明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到），那么我们推荐使用for-in循环，例如下面代码中计算1~100求和的结果（$\displaystyle \sum \limits_{n=1}^{100}n$）。

```python

sum = 0
for x in range(101):
	sum += x
print(sum)

```

需要说明的是上面代码中的range(101)可以用来构造一个从0到100的取值范围，这样就可以构造出一个整数的序列并用于循环中，例如：
- range(101)可以产生一个0到100的整数序列。
- range(1, 100)可以产生一个1到99的整数序列。
- range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。

### while 循环
如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True循环继续，表达式的值为False循环结束。
举个例子：
```python

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

import random

answer = random.randint(1, 100)
counter = 0

while True:
	counter += 1
	number = int(input('请输入：'))

	if number < answer:
		print('大一点')
	elif number > answer:
		print('小一点')
	else:
		print('你猜对了!')
		break

print('总共猜了%d次' % counter)
if counter > 7:
	print('hahahahh')	

```

上面的代码中使用了break关键字来提前终止循环，需要注意的是break只能终止它所在的那个循环，这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。除了break之外，还有另一个关键字是continue，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。

和分支结构一样，循环结构也是可以嵌套的，也就是说在循环中还可以构造循环结构。