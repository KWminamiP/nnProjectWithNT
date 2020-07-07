#これがmain関数
import getdata
import Forward
w = [1,1,1.5]
a,b = getdata.get_data(4)
print(a)
print(b)
print(w)
ForwardFunction_class = Forward.ForwardFunction()
c = ForwardFunction_class.forward(*w,*b)


print(c)
