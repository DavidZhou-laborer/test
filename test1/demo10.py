'''
@File    :   demo10.py
@Time    :   2022/12/12 10:05:07
@Author  :   大马 
@Version :   1.0
@Contact :   123456@qq.com
'''

'''集合'''
'''集合的创建方式1:使用{}'''
s = {1, 2, 3, 4, 5, 6, 1, 2}
print(s)  # 集合的元素不允许重复

'''集合的创建方式2：使用内置函数set'''
s1 = set(range(6))
print(s1, type(s1))
s2 = set([1, 2, 3, 4, 5, 6])
print(s2, type(s2))
s3 = set((1, 2, 3, 4, 5, 6))  # 元组方式输出
print(s3, type(s3))
s4 = set('python')
print(s4, type(s4))
s5 = set()
print(s5, type(s5))


'''集合的相关操作'''
s = {10, 20, 30}
print(10 in s)
print(10 not in s)
print(100 in s)


'''集合元素的新增操作'''
s.add(80)#add表示一次添加一个元素
print(s,type(s))
s.update({200,300,400})#update表示一次至少添加一个元素
print(s,type(s))
s.update([100020,1212])
print(s, type(s))


'''集合元素的删除操作'''
'''使用remove()，指定删除的元素不存在就会抛出异常'''
s.remove(400)
print(s)
#s.remove(100)
#print(s)#指定的元素不存在，会抛出异常
'''discard(),指定的元素不存在就不会抛出异常'''
s.discard(80)
print(s)
'''pop()随机删除一个元素,无法指定一个元素'''
s.pop()
print(s,type(s))
'''clear()清空元素'''
s.clear()
s={10,20,30}
s1={30,20,10,100,112}
'''两个元素是否相等，若元素相同'''
print(s==s1)
'''一个元素是另一个元素的子集'''
print(s.issubset(s1))

'''集合的数学操作'''
'''交集'''
s1={10,20,12,122}
s2={10,20,1234,111}
print(s1.intersection(s2))#intersection和&等价
print(s1&s2)
'''并集操作'''
print(s1.union(s2))
print(s1| s2)#union和|等价
'''差集操作'''
print(s1.difference(s2))#difference和-等价
print(s1-s2)
'''对称差集'''