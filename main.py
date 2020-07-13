#これがmain関数
import getdata
import Forward
w = [1,1,1.5]
a,b = getdata.get_data(4)
print(a)
print(b)
print(b[0])
print(w,b[0])
ForwardFunction_class = Forward.ForwardFunction(w,b[0])
c = ForwardFunction_class.forward()
print(c)

for i in b:#iが順番に読み出されるリスト。便利すぎんかpython
    print(i)
    ForwardFunction_class = Forward.ForwardFunction(w,i)
    d = ForwardFunction_class.forward()
    print(d)
