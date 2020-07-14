#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ffunction
class ForwardFunction:
    #float w 　重みとしきい値
    #float e 　入力のデータセット
    def __init__(self, w_int, e_int):
        self.w = w_int
        self.e = e_int
        print("Initialized!")

    def forward(self):
        #u  入力値
        #o  出力値
        w = self.w
        e = self.e

        o = 100.0
        u = 0.0   #入力値の初期化
        #float
        threshold = 100.0    #しきい値
        for i in range(len(e)):
            print(i)
            u= u+w[i]*e[i]
            threshold = w[i+1] #しきい値はリストwの最後の値
            print("これはfor文の中です。")
        print("これはForward関数の中です。")
        print(threshold)
        print(u)
        u=u-threshold     #しきい値の処理
        o = f(u)           
        return o


# In[ ]:




