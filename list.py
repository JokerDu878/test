'''
创建列表
 格式： 列表名=[列表选项1，列表选项2，....]

'''

list1=[]
print(list1)

#创建带元素的列表
list2=[12,22,55,4]
list3=[12,55,"good"]


#列表元素的访问
list4=[1,2,3,4,5]
print(list4[2])

#替换
list4[4]=300
print(list4[4])

list2=[15,22,20,19,18]
i=0
sum=0
while i<5:
    sum+=list2[i]
    i+=1
    if i==5:
        print("平均年龄：%d"%(sum/5))
#列表操作
#列表组合
list5=[1,2,3]
list6=[4,5,6]
list7=list5+list6
print("列表的相加:")
print(list7)

list8=[1,2,3]
print("列表的乘")
print(list8*3)

#判断元素是否在列表中
list9=[1,2,3,4,5]

print(3 in list9)
print(6 in list9)
#返回的是真假值

#列表截取
list10=[1,2,3,4,5,6,7,8,9]
print(list10[2:6])
print(list10[3:])
print(list10[:5])

#二维列表 （会拿数据就行）
list11=[[1,2,3],[4,5,6],[7,8,9]]
print(list11[1][1])
print(list11[2])
print("")
#列表方法
#append  在列表中末尾添加新的元素
list12=[1,2,3,4,5]
list12.append(6)
list12.append([7,8,9])
print(list12)
print("")

#extend 在末尾一次性追加一个列表中的多个值
list13=[1,2,3,4,5,6]
list13.extend([6,7,8])
print(list13)

#在下表处添加一个元素，不覆盖原数据
list14=[1,2,3,4,5]
list14.insert(2,100)
print(list14)
print("")
list14.insert(2,[200,300])
print(list14)

#删除 pop(x) 删除下表x的元素 默认为最后一个
#并返回删除的数据
list15=[1,2,3,4,5]
list15.pop()
print(list15)
list15.pop(2)
print(list15)
print(list15.pop(1))
print(list15)

#remove 一处列表中的某个元素 第一个匹配的结果
list16=[1,2,3,4,5,4,5,4]
list16.remove(4)
print(list16)

#清除列表中所有的数据
list17=[1,2,3,4,5]
list17.clear()
print(list17)


#从列表中找出某个值第一个匹配的索引值
list18=[1,2,3,4,5,3,4,5,6]
i18=list18.index(3)
print(i18)
#index 选定范围查找
i19=list18.index(3,3,8)
print(i19)

#列表中元素个数 len
list20=[1,2,3,4,5]
print(len(list20))

#获取列表中的最大值
list21=[1,2,3,4,5]
print(max(list21))

#计数
list23=[1,2,3,4,5,3,3,6,5,6,1,2]
print(list23.count(3))

i=0
n=list23.count(3)
while i<n:
    i+=1
    list23.remove(3)
print(list23)

#倒序
list25=[1,2,3,4,5]
list25.reverse()
print(list25)

#排序
#sort 升序
list26=[1,2,6,8,4,5,3]
list26.sort()
print(list26)

#拷贝
#浅拷贝 只是拷贝地址
list27=[1,2,3,4,5]
list28=list27
list28[1]=200
print(list28)
print(list27)
print(id(list28))
print(id(list27))

#深拷贝
list29=[1,2,3,4,5]
list30=list29.copy()
list29[1]=200
print(list29)
print(list30)
print(id(list29))
print(id(list30))
