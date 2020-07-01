#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ForwardFunction:
    #float w 　重みとしきい値
    #float e 　入力のデータセット
    def forward(*w, *e):
        float u   #入力値
        float o   #出力値
        u= 0   #入力値の初期化
        float threshold    #しきい値
        for i, j in zip(*w, *e):
            u=u+i*j
            threshold=i    #しきい値はリストwの最後の値
        u=u-threshold     #しきい値の処理
        o = f(u)
        return o


# In[ ]:




