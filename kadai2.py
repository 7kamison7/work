#数を 10個入力してその合計を表示するプログラムを作りなさい
#2
print('10個の数値を入力してください')
num = [int(input())for i in range(10)]

print('合計値:',end="")
print(sum(num))