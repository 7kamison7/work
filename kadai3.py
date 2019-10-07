#(3) 
# 1. キーボードから入力した 10 個の数の中に 5 がなければ Boo と表示する．
print('10個の数値を入力してください')
num = [int(input())for i in range(10)]

if 5 in num:
    pass
else:
    print ('Boo')

# 2. 入力した 10 個の数の中に負の数があるかどうかを表示するようにしましょう．
x=1
for i in num:
    if i < 0:
        x=0
        break
    else:
        pass

if x ==0:
    print('負の数はあります')
else:
    print('負の数はありません')