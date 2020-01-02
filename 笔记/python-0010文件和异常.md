## 文件和异常
在Python中实现文件的读写操作其实非常简单，通过Python内置的open函数，我们可以指定文件名、操作模式、编码信息等来获得操作文件的对象，接下来就可以对文件进行读写操作了。这里所说的操作模式是指要打开什么样的文件（字符文件还是二进制文件）以及做什么样的操作（读、写还是追加），具体的如下表所示。

|  操作模式  	| 具体含义      				|
|  :---:   	| :---:    					|
|  'r'	    | 读取(默认)   	  		 	|
|  'w'  	| 写入(会先截断之前的内容)   	|
|  'x'      | 写入,如果文件已经存在会产生异常|
|  'a'		| 追加,将内容写入到已有文件的末尾|
|  'b' 		| 二进制模式					|
|  't' 		| 文本模式(默认)				|
|  '+' 		| 更新(既可以读也可以写)		|

下面图片来源于菜鸟教程
![文件操作](https://raw.githubusercontent.com/jackfrued/Python-100-Days/master/Day01-15/res/file-open-mode.png)

### 读写文本文件
读取文本文件时，需要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设置为'r'（如果不指定，默认值也是'r'），然后通过encoding参数指定编码（如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码），如果不能保证保存文件时使用的编码方式与encoding参数指定的编码方式是一致的，那么就可能因无法解码字符而导致读取失败。
举个例子:
```python
def main():
    f = open('haha.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()

if __name__ == '__main__':
    main()

```
请注意上面的代码，如果open函数指定的文件并不存在或者无法打开，那么将引发异常状况导致程序崩溃。为了让代码有一定的健壮性和容错性，我们可以使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理，如下所示。
```python
def main():
    f = None
    try:
        f = open('haha.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    main()



"""
在Python中，我们可以将那些在运行时可能会出现状况的代码放在try代码块中，在try代码块的后面可以跟上一个或多个except来捕获可能出现的异常状况。例如在上面读取文件的过程中，文件找不到会引发FileNotFoundError，指定了未知的编码会引发LookupError，而如果读取文件时无法按指定方式解码会引发UnicodeDecodeError，我们在try后面跟上了三个except分别处理这三种不同的异常状况。最后我们使用finally代码块来关闭打开的文件，释放掉程序中获取的外部资源，由于finally块的代码不论程序正常还是异常都会执行到（甚至是调用了sys模块的exit函数退出Python环境，finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），因此我们通常把finally块称为“总是执行代码块”，它最适合用来做释放外部资源的操作。如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，代码如下所示。
"""

def main():
    try:
        with open('haha.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()
    

```
除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中，代码如下所示。
```python
import time


def main():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()
```
要将文本信息写入文件文件也非常简单，在使用open函数时指定好文件名并将文件模式设置为'w'即可。注意如果需要对文件内容进行追加式写入，应该将模式设置为'a'。如果要写入的文件不存在会自动创建文件而不是引发异常.
```python
from math import sqrt


def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')


if __name__ == '__main__':
    main()
```

### 读写二进制文件
知道了如何读写文本文件要读写二进制文件也就很简单了，下面的代码实现了复制图片文件的功能。
```python
def main():
    try:
        with open('wa.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('hah.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')


if __name__ == '__main__':
    main()
```




