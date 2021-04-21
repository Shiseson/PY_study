#In[1]
#有序可變動列表 List
grades=[12, 15, 60, 70, 90]
print(grades)

#指定列表單一位置數值
print(grades[0])

#更改列表單一位置數值
grades[0]=55
print(grades)

#指定列表範圍
print(grades[1:4]) #只包含[1][2][3]

#清空列表範圍
grades[1:4]=[]
print(grades)

#列表串接
grades=grades+[12,33]
print(grades)

# 列表長度
length=len(grades)
print(length)

#巢狀
data=[[3, 4, 5],[6, 7, 8]]
print(data[0][2])
data[0][0:2]=[5, 5, 5, 9]
print(data)

#In[2] 有序不可變動列表 Tuple
data=(3, 5, 4)
# data[0]=5 #錯誤打法：Tupple資料不可更動
print(data[0:2])