# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:45:15 2024

@author: noton
"""

import pandas as pd
import numpy as np

df = pd.read_csv('data/data_AuCd.csv')
print(df)
df['Class'] = np.where((df['ratio_AuCd'] >= 90) & (df['H'] == 'Y') & (df['V'] >= 6) & (df['C'] <= 6), '1', '0')
print(df)

df_bool = (df == '1')
print(df_bool.sum())

df.to_csv('data/data_AuCd2.csv', index = False)
