# 集合運算
# In[0]
s1={3, 4, 5}
print(10 not in s1)

# In[1]
s2={3, 4, 5}
s3={5, 6, 7, 8}
s4=s2&s3        # 交集
s5=s2|s3        # 聯集
s6=s2-s3        # 差集
s7=s2^s3        # 反交集:起兩個集合中，不重疊的部分
print(s4,s5,s6,s7)

# In[2]
s=set("Hello")  # 把字串中的字母拆解成集合 set(字串)
print("A" in s)
print(s)

#In[3]
dic={"apple":"蘋果", "bug":"蟲蟲"}
print(dic["apple"])     # 印出蘋果
dic["apple"]="青蘋果 LEVEL UP"
print(dic["apple"])
print("apple" in dic)
print(dic)
del dic["apple"]        #刪除鍵質對(key-value pair)
print(dic)

# In[4]
dic={x:x*2 for x in [3, 5, 6]}
print(dic)

# %%
