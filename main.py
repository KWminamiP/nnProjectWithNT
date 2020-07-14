#これがmain関数
import getdata
import Forward
w = [1,1,1.5]
print("データ読み込み開始")
a,b = getdata.get_data(4)
#print(a)
#print(b)
print("=======================")
print("読み込んだデータの計算開始")
for i in b:#iが順番に読み出されるリスト。便利すぎんかpython
    print(i)
    ForwardFunction_class = Forward.ForwardFunction(w,i)
    d = ForwardFunction_class.forward()
    print(i,"の計算結果")
    print(d)
    print("=====================")
