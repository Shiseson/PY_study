# In[0] break
n= 0
while n< 5:
    if n==3:
        break
    print(n)
    n+=1
print("最後的 n :", n)

# In[1] coutinue

L= 0
for x in [0, 1, 2, 3, 4] :
    if x% 2 == 0:
        continue
    print(x)
    L+=1
print("最後的L: ", L)

# In[2] else
sum= 0
for n in range(11):
    sum+=n
else:
    print(sum)

# In[3] 綜合題目: 找出整數平方根
#輸入 9，得到 3
#輸入 11，得到【沒有】整數的平方根
k= input("輸入一個正整數: ")
k= int(k)
for i in range(k):
    if i*i==k:
        print("整數平方根", i)
        break
else:
    print("沒有整數平方根")
# %%
