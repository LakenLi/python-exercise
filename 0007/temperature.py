# enncoding: utf-8
"""
提示：华氏温度到摄氏温度的转换公式为：$C = (F - 32) / 1.8
"""

f = float(input('请输入华氏温度:'))
c = (f -32) / 1.0

print('%.1f 华氏温度 = %.1f 摄氏温度' % (f, c))