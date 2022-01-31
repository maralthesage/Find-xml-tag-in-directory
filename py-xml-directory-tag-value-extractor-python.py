#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from bs4 import BeautifulSoup
import glob

## Remember you should save and load this script from the same folder as your data
for filename in glob.glob("*.xml"):
    
    with open(filename) as open_file:
        
        soup = BeautifulSoup(open_file, 'xml')  
        
        ## instead of 'Content' add the tag name inside your xml which you are interested in
    for tag in soup.find_all('Content'):
        
        ## instead of 'LeafScan' add the tag value that you are looking for
        if tag.get_text() == 'LeafScan':
            
#             print(filename) 


# In[ ]:




