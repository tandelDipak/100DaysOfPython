#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('load_ext', 'pycodestyle_magic')


# In[ ]:


get_ipython().run_line_magic('flake8_on', '')


# In[ ]:


from datetime import datetime
from datetime import date
from datetime import timedelta


# In[ ]:


today = datetime.today()
print(today)
today


# In[ ]:


today_date = date.today()
print(today_date)
today_date


# In[ ]:


today.month


# In[ ]:


today.day


# In[ ]:


christmas = date(2020, 12, 25)
print(christmas)


# In[ ]:


days = christmas - today_date
days


# In[ ]:


print(f'Sorry still {days.days} days left for christmas')


# In[ ]:


t = timedelta(days=4, hours=10)
print(t.days)
print(t.seconds)


# In[ ]:


eta = timedelta(hours=6)
today = datetime.today()
print(eta)
print(today)


# In[ ]:


print(today + eta)


# In[ ]:




