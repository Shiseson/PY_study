# 數字運算
# In[1] 乘法--------------------
x=3*6
print(x)
# In[2] 除法multiplication----------------------
y=3/6           #1.小數除法
print(y)
z=3//6          #2.整除integer
print(z)
j=7%3           #3.取餘數remainder(dividend % divisor = remainder.)
print(j)
# In[3] 次方運算------------------
x=2**3.54
print(x)
# In[4] 數字運算-------------------------
x=6
x=x+5 #x+=5
print(x)
# In[5] 字串運算-------------------------
s="Hello"+" "+"World"       #Python supports concatenating strings using the addition operator
s="Hello" "World"           #空白處等同於+ 是PYTHON的特殊用法
s="Hello\nWorld"            #換行
s="Hello\nWorld"*3+"World"  #用乘法可以倍數輸出Python also supports multiplying strings to form a string with a repeating sequence
s="""Hello
          World"""          #也是換行的特殊技巧 三個雙引號內的使用 會如程式書寫被呈現出去
print(s)
# In[6] 字串內的字元編號(索引)，從0開始算起----------------------
s="Hello"
print(s[1])     # e     #字元編號1
print(s[1:3])   #el     #字元編號12
print(s[1:])    #ello   #字元編號1234
print(s[:2])    #He     #字元編號01

# In[7] Using two multiplication symbols makes a power relationship.
# 用兩個乘號製造平方
squared = 7 ** 2    #2次方
cubed = 2 ** 3      #3次方
print(squared)
print(cubed)
remainder = 11 % 3
print(remainder)

#In[8] Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator
print([1,2,3] * 3)

#In[9] Exercise--------------------
x = object()
y = object()

# TODO: change this code
x_list = [x]*10
y_list = [y]*10
big_list = x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# %%
