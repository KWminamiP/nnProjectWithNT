#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ForwardFunction:
    #float w 　重みとしきい値
    #float e 　入力のデータセット
    def __init__(self, w_int, e_int):
        self.w = w_int
        self.e = e_int
        print("Initialized!")

    def forward(self):
        #float u   #入力値
        #float o   #出力値
        w = self.w
        e = self.e

        o = 100.0
        u = 0.0   #入力値の初期化
        #float
        threshold = 100.0    #しきい値
        for i, j in zip(*w, *e):
            u=u+i*j
            threshold=i    #しきい値はリストwの最後の値
        u=u-threshold     #しきい値の処理
        o = u              #= f(u)
        return o


# In[ ]:
