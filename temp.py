# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
import gorylla as gy
from gorylla import *


host = 'hijin.cn'
strq = 'SHOW TABLES;'
df = sql_to_df('test',strq,host = host)
#
#os.mkdir('backup')
#os.mkdir('conf')
#os.mkdir('dist')
#os.mkdir('www')
#os.mkdir('www/static')
#os.mkdir('www/templates')

os.mkdir('ios')

