"""
# In[1]
x=2
print(x==2)     #true
print(x==3)     #false
print(x>3)      #false
print(x<3)      #true

# In[2]
 name = "John"
 age = 23
if name =="John" and age == 23:
    print("your name is John, and you are also 23 years old")
if name == "John" or name == "Rick":
    print("your name is either John or Rick")

# In[3]
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# In[4]
statement = False
another_statement =True
if statement is True:
    # do something
    pass
elif another_statement is True: #else if
    # do something
    pass
else:
    # do something
    pass

# In[5]
x = 2
if x ==2:
    print("x equals two.")
else:
    print("xdose not equal to two.")

# In[6] The "is" operator
x = [1, 2, 3]
y = [1, 2, 3]
z = y
print(x == y)   #T
print(x is y)   #F
print(y is z)   #T

# In[7] The "not" operator
print(not False) #print out True
print((not False) == (False)) #print out False

# In[8]# change this code
number = 16
second_number = 0
first_array = ()
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# In[9]
first_array = [1, 2, 3]
print(first_array)

# In[10] 判斷式
if True:
    print("True 執行")
else:
    print("False 執行")

# In[11] 使用者輸入取得字串
x=input("請輸入數字: ")
x= int(x)       # 將字串型態轉換成數字型態
if x>200:       # if elif else 只會觸發一種狀況
    print("大於100")
elif x>100
    print("大於100，小於等於200")
else:
    print("小於等於100")
"""
# In[12] 四則運算
n1= int(input("請輸入第一格數字: "))
n2= int(input("請輸入第二格數字: "))
op= input("請輸入運算符號: +, -, *, / : ")
if op== "+" :
    add = n1+ n2
    print("n1+ n2 = %s" % add)
elif op== "-" :
    print("n1- n2 ")
elif op== "*" :
    print("n1* n2 ")
elif op== "/" :
    print("n1/ n2 ")
else :
    print("不支援此運算符號")

# %%
