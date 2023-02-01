# 打 工 日 志 #
# 打工人：大马
# 打工时间：2022/10/29 17:23
r=range(1,10)#从1开始，到10结束（不包含10），默认步长为1 ,(a,b]
print(list(r))

#变量是存储一个对象的引用 列表是存储多个变量的引用
#创建方式：1 []
fst=['hello','world',999]
#创建方式：2 使用内置函数list()
sst=list(['hello','world',999])
print(type(fst))
print(type(sst))
#列表特点：1有序排序 2索引映射唯一一个元素（有两种索引方式 一种是正向索引带0，一种是反向索引从-1开始） 3可以存储重复数据 4任意数据类型可以混存 5根据元素多少进行分配内存
lst11=list(['hello','world',9])
print(lst11[0])
print(lst11[-3])

lst22=list(['hello','world',91,'hello'])
print(lst22.index('hello'))#如果列表中有相同元素，只返回列表中第一个元素的索引
print(lst22.index('hello',1,4))#可以设置start和stop标志位

#切片
print(sst[::])