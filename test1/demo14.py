'''
@File    :   demo14.py
@Time    :   2022/12/20 17:57:34
@Author  :   大马 
@Version :   1.0
@Contact :   123456@qq.com
'''

'''BUG'''
#python中异常处理情况
#try-except结构
'''
try:
    a=int(input('请输入一个整数'))
    b =int(input('请输入一个整数'))
    result=a/b
    print('结果为：',result)
except ZeroDivisionError:#zerodivisionerror是错误类型
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入字符串')
print('程序结束')
'''

#try...except...else结构 若try中没有抛出异常块，则执行else块。若try中抛出异常块，则执行except块
'''
try:
    a = int(input('请输入一个整数'))
    b = int(input('请输入一个整数'))
    result = a/b

except BaseException as e:  #不知道可能出现什么异常 e是别名
    print('出错了',e)
else:
    print('结果为：', result)
'''

#try...except...else...finally结构 finally中无论是否发生异常都会被执行，能常用来释放try块中申请的资源
try:
    a = int(input('请输入一个整数'))
    b = int(input('请输入一个整数'))
    result = a/b

except BaseException as e:  # 不知道可能出现什么异常 e是别名
    print('出错了', e)
else:
    print('结果为：', result)
finally:
    print('谢谢您的使用!')

'''
常见的异常类型
(报错的时候会提示)
'''

