#9
# ​正の整数の逆数の合計を出力する．(注：n=7)
from fractions import Fraction

sum=0
n = int(input('数字：'))
for i in range(n):
    x=Fraction(1,i+1)
    sum +=x
    print(str(x),end='')
    if not n == i+1 :
        print('+',end='')
print('='+str(sum))


