#!/usr/bin/env python
# coding: utf-8

# In[13]:


nums = list(range(30, 65, 5))
nums.append(65)
print(nums[::-1])


# In[35]:


nums = list()
nums.extend(range(0, 21))
nums.remove(0)
print(len(nums))
print(max(nums))
print(min(nums))
sum(nums)


# {'Sunny': 'play', 'Rainy': 'watch TV', 'Cloudy': 'walk'}
# print(dictionary)

# In[77]:


d = {'Sunny': 'play', 'Rainy': 'watch TV', 'Cloudy': 'walk'}
for key, value in d.items():
    print("When", key, "let us", value)  
d.update({'Snowy': 'ski'})
for key, value in d.items():
    print("When", key, "let us", value) 

